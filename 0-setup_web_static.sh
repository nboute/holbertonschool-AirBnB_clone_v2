#!/usr/bin/env bash
#Configure web server for deployment of web_static

apt update
apt -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "This is a website" >> /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -sT /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
echo "Configuration executed successfully"
service nginx restart
