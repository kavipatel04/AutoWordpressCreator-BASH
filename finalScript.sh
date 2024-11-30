mysql -u [ur_user] -p[ur_passwd] -e "CREATE DATABASE $1";

cd /tmp;
curl -LO https://wordpress.org/latest.tar.gz;
tar xzvf latest.tar.gz;
sudo cp -a /tmp/wordpress/. /var/www/$1;
sudo chown -R www-data:www-data /var/www/$1;
cd /home/kavip100;
sudo python3 wpConfGen.py -b $1;
sudo python3 nginxConfGen.py  -f $1 -d $2;
sudo systemctl reload nginx;
echo 'Y' | sudo certbot --nginx -d $2 -m $3;

