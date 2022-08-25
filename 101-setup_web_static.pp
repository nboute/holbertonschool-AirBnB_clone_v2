# Configure web server for deployment of web_static

exec {'/usr/bin/env apt update': }
-> exec {'/usr/bin/env apt -y install nginx': }
-> exec {'/usr/bin/env mkdir -p /data/web_static/releases/test': }
-> exec {'/usr/bin/env mkdir -p /data/web_static/shared': }
-> exec {'/usr/bin/env echo "This is a website" >> /data/web_static/releases/test/index.html': }
-> exec {'/usr/bin/env rm -rf /data/web_static/current': }
-> exec {'/usr/bin/env ln -sT /data/web_static/releases/test/ /data/web_static/current': }
-> exec {'/usr/bin/env chown -R ubuntu:ubuntu /data/': }
-> exec {'/usr/bin/env sed -i "47i location /hbnb_static {alias /data/web_static/current/;}" /etc/nginx/sites-available/default': }
-> exec {'/usr/bin/env echo "Configuration executed successfully"': }
-> exec {'/usr/bin/env service nginx restart': }
