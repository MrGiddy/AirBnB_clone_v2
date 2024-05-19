#!/usr/bin/env bash
# Sets up web servers for deployment of web_static

# Install Nginx if it not already installed
sudo apt update && sudo apt install -y nginx

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/

# Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file /data/web_static/releases/test/index.html
# Add simple content, to test Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current to the /data/web_static/releases/test/ folder
# If the symlink already exists, it should be deleted and recreated every time the script is ran
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
# This should be recursive; everything inside should be created/owned by this user/group.
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of 
# /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static).
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    add_header X-Served-By \$hostname;
    add_header Content-Type text/html;

    location / {
        return 200 'Holberton School\n';
    }

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /var/www/html;
        internal;
    }
}
" > /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart
