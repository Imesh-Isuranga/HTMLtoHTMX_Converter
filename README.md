# HTMLtoHTMX_Converter
## Milestones Summary:
<ol>
  <li>Set Up Project</li><i class="fa-duotone fa-solid fa-bell-ring"></i>
  <li>Parse the HTML</li>
  <li>Identify AJAX Requests</li>
  <li>Identify Form Tags</li>
  <li>Identify HTMX Attributes</li>
  <li>Implement Conversion Logic</li>
  <li>Build a User Interface (Optional)</li>
  <li>Testing and Validation</li>
  <li>Documentation and User Guide</li>
  <li>Deployment (Optional)</li>
</ol>

<p>In this HTML to HTMX convertor I have done below tasks so far.I have used python <i>soup</i> library to extract html tags fromuser input html code.Also whole code you can see <i>regular expressions</i>.I have used regular expressions to find all code parts which can able to convert to HTMX.Then I have wrote some codes for to convert that html code to HTMX.They are :-</p>

<ol>
  <li>Created new script tag in head section and append HTMX dependency via CDN</li>
  <li>If there are form tags in html then find them all and converted to HTMX by adding relevant HTMX tags.</li>
  <li>Find all document.addEventListener('DOMContentLoaded'),document.getElementById,etc code and convert them using relevant HTMX tags.</li>
  <li>If there are input tags inside form tag I also have wrote code to convert them to HTMX.</li>
  <li>If there are <a> tags insde div tags then find them all and converted them to HTMX.</li>
</ol>

You can find above all 5 functions in my code.I have commented all the things I have mentioned.

<b>If you like to implement any of below function plz help.</b>

<a href="https://htmx.org/docs/#inheritance">Inheritance</a>
<a href="https://htmx.org/docs/#synchronization">Synchronization</a>
<a href="https://htmx.org/docs/#validation">Validation</a>
<a href="https://htmx.org/docs/#websockets-and-sse">Websockets-and-sse</a>




