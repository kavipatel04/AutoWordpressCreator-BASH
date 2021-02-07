import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", type=str, help="filepath in terms of /var/www")
parser.add_argument("-d", "--domain", type=str, help="domain name ex. something.com")
args = parser.parse_args()
filepath = str(args.filepath)
domainName = str(args.domain)
file1 = open("/etc/nginx/sites-enabled/" + domainName + ".conf", "a+")
file1.write("server {\r\n    listen 80;\r\n    listen [::]:80;\r\n\r\n    root /var/www/" +filepath +  ";\r\n    index index.php index.html index.htm index.nginx-debian.html;\r\n\r\n    server_name " + domainName +  ";\r\n\r\n    location / {\r\n        try_files $uri $uri/ /index.php$is_args$args;\r\n    }\r\n\r\n    location ~ \\.php$ {\r\n        include snippets/fastcgi-php.conf;\r\n        fastcgi_pass unix:/run/php/php7.4-fpm.sock;\r\n    }\r\n\r\n    location ~ /\\.ht {\r\n        deny all;\r\n    }\r\n}")
file1.close()

