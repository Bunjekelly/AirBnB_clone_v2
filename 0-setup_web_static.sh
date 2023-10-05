#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#index.html content
content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$content" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
