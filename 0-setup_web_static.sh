#!/usr/bin/env bash
# Install nginx and do the following

# Install Nginx if not already installed
if ! which nginx > /dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file to test Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create a symbolic link from /data/web_static/current to /data/web_static/releases/test
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership of /data/ directory to ubuntu user and group recursively
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

# Configure Nginx to serve content of /data/web_static/current to hbnb_static
sudo sed -i '/listen 80 default_server;/a\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart
