# AutoWordpressCreator-BASH
This will create a new wordpress instance on a server. In order for this script to run successfully it is expected that mySQL or PHP be installed, alongside NGINX!

<br>
This script is meant to make it easier for first time users of a web server to install a wordpress creator. That way they don't have to pay for expensive CPANEL hosting, and can do it themselves for free!
<br>

<h2>Requirements</h2>
<li>NGINX</li>
<li>Python3</li>
<li>Ubuntu/Debian/Linux based OS</li> 
<li>Sudo Privileges</li>
<li>mySQL or MariaDB</li>
<li>Certbot Package (Optional: For SSL only)</li>

<br>
<h2>How to Run</h2>

`sudo bash finalScript.sh (database name / folder name) (domain) (email)`

Example:

`sudo bash finalScript.sh wordpress kavipatel.xyz kavipatel@kavipatel.xyz`

If you need help or have any questions, feel free to reach out to me with the information from above! 

<br>
<h2>How Much of the Process Will This Take Care of</h2>
If ran in it's entirety, this script will take care of everything. From start to finish. It will get the API keys from Wordpress servers as well to authorize the wordpress install. This script will also create the NGINX file associated with the folder that needs to be published on the web. On top of all that, this script will get an SSL certificate to secure your wordpress website. Once ran, you can access the wordpress site by typing in the domain name. 
