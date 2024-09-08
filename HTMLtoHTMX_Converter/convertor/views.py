import re
from django.shortcuts import render
from convertor.forms import HtmlConvertorForm
from bs4 import BeautifulSoup

def Convertor(request):
    if request.method == 'POST':
        form = HtmlConvertorForm(request.POST)
        if form.is_valid():
            htmlInput = form.cleaned_data['htmlInput']
            if request.headers.get('Hx-Request'):  # Check if the request is an HTMX request
                #soup = BeautifulSoup(htmlInput).prettify()
                soup = convert_form_to_htmx(htmlInput)
                return render(request, 'converted_htmx.html', {'htmlInput': soup})
            return render(request, 'convertor.html', {'form': form})
    else:
        form = HtmlConvertorForm()

    return render(request, 'convertor.html', {'form': form})


def convert_form_to_htmx(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Create a new <script> tag-----------------------------------------------------------------------------------
    new_div = soup.new_tag("script", 
                        src="https://unpkg.com/htmx.org@2.0.2", 
                        integrity="sha384-Y7hw+L/jvKeWIRRkqWYfPcvVxHzVzn5REgzbawhxAuQGwX1XWe70vji+VSeHOThJ", 
                        crossorigin="anonymous")

    # Append the new <script> tag to the <head> section of the HTML
    soup.html.head.append(new_div)
 
    # Find all form elements--------------------------------------------------------------------------------------------
    forms = soup.find_all('form')

    for form in forms:
        # Convert the method to HTMX
        if form.has_attr('method'):

            #check csfr token
            if 'csrf' in form.decode_contents():
                print("CSRF found in form:")
            else:
                print("CSRF not found in form.")

            method = form['method'].lower()
            action = form['action'] if form.has_attr('action') else ''
            if form.has_attr('action'):
                 del form['action']  # Remove the 'action' attribute

            if method == 'post':
                form['hx-post'] = action
            elif method == 'get':
                form['hx-get'] = action
            del form['method']  # Remove the old method attribute

            if form.has_attr('id'):
                form_id = form['id']
                script_tag = soup.find('script', text=lambda x: x and f"#{form_id}" in x)

                if script_tag:
                    script_content = script_tag.string
                    
                    # Step 3: Check for the success handler
                    if 'success:' in script_content:
                        success_index = script_content.index('success:')
                        start_index = script_content.find("$('#", success_index)
                        end_index = script_content.find("').html", start_index)
                        
                        # Extract the target div ID
                        if start_index != -1 and end_index != -1:
                            target_div_id = script_content[start_index + 4:end_index]
                            print(f"Target div ID: {target_div_id}")
                            
                            # Step 4: Extract the content of the target div
                            target_div = soup.find(id=target_div_id)
                            if target_div:
                                form['hx-target'] = f'#{target_div_id}'
                                form['hx-swap'] = 'innerHTML'
                                print("Content of the success target div:", target_div.prettify())
                            else:
                                form['hx-target'] = 'this'
                                form['hx-swap'] = 'innerHTML'
                                print("Target div not found in the HTML.")
                        else:
                            print("Could not find the target div in the success handler.")
                    else:
                        print("No success handler found in the AJAX request.")
                else:
                    print("No script found that handles the form submission.")


    # HTMX to scripts elements--------------------------------------------------------------------------------------------
    # Define a regular expression pattern that matches the target string with optional spaces
    pattern_DOM_LOAD = re.compile(r'document\.addEventListener\s*\(\s*"\s*DOMContentLoaded\s*"\s*,\s*(\(\s*\)\s*(?:=>|=>)|(?:function|fun|func)\s*\(\s*\))\s*{',re.IGNORECASE)
    pattern_getElement = re.compile(r'document\.getElementById\("')
    pattern_click = re.compile(r'(\b\w+)\.addEventListener\(\s*"\s*(\w+)\s*"\s*,\s*(?:function|func|fun)\s*\(\)\s*{[^}]*\}\)',re.IGNORECASE)


    # Find all <script> tags containing the pattern
    script_tags_DOM_LOAD = soup.find_all(lambda tag: tag.name == "script" and pattern_DOM_LOAD.search(tag.text))
    script_tags_id_tags = soup.find_all(lambda tag: tag.name == "script" and pattern_getElement.search(tag.text))
    script_tags_id_clicks = soup.find_all(lambda tag: tag.name == "script")


    # Replace the matched pattern with '...' in each script tag
    for script_tag_DOM_LOAD in script_tags_DOM_LOAD:
        script_tag_DOM_LOAD.string = pattern_DOM_LOAD.sub('htmx.onLoad(function(elt){', script_tag_DOM_LOAD.string)
    
    for script_tag_id_tags in script_tags_id_tags:
        script_tag_id_tags.string = pattern_getElement.sub('htmx.find("#', script_tag_id_tags.string)

    for script_tag_id_clicks in script_tags_id_clicks:
        # Extract and replace the patterns
        script_text = script_tag_id_clicks.string
        if script_text:
            # Find all matches
            new_script_text = pattern_click.sub(lambda m: f'htmx.on({m.group(1)},"click", function(evt)', script_text)
            
            # Replace `anyText` with the new variable assignment
            #new_script_text = re.sub(r'(\b\w+)\s*=\s*document\.getElementById\("demo"\);', r'newText = document.getElementById("demo");', new_script_text)
            
            # Update the script tag with the new content
            script_tag_id_clicks.string = new_script_text



    # Finding input after form tag replace it with HTMX--------------------------------------------------------------------------------------------
    
    # Find the 'input' tag inside the 'form' tag
    form_tags = soup.find_all('form')

    for form_tag in form_tags:
        if form_tag is not None:
            inner_tag = form_tag.find('input')

            if inner_tag is not None:
                # Add new attribute to the 'input' tag
                inner_tag['hx-trigger'] = 'change'
                inner_tag['hx-sync'] = 'closest form:abort'
            else:
                print("Input tag with class 'inner' not found.")
        else:
            print("Form tag with class 'outer' not found.")


    #print(soup.prettify())
    return str(soup)
