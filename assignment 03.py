#Step 1: Creating a New User
#Connect to your server as the root user:

ssh root@your_server_ip

#Create a new user (replace username with your desired username):

adduser username

#Grant administrative privileges:

usermod -aG sudo username

#Set Bash as the user's login shell:

chsh -s /bin/bash username

#Step 2: Securing SSH Access
#2.1: Configure SSH for the New User
#As the root user, copy the SSH key:

rsync --archive --chown=username:username ~/.ssh /home/username

#2.2: Disable Root SSH Login
#Edit the SSH configuration file:

nano /etc/ssh/sshd_config

#Set the following line:
#config

PermitRootLogin no

#Restart the SSH service:

systemctl restart sshd

#Step 3: Installing Nginx
#Update your package list:

sudo apt update

#Install Nginx:

sudo apt install nginx

#Step 4: Configuring Nginx to Serve a Sample Website
#4.1: Creating a Sample Website

#Create a directory for your website:

sudo mkdir -p /var/www/my_website

#Assign ownership to your user:

sudo chown -R username:username /var/www/my_website

#Create a sample index.html file:

nano /var/www/my_website/index.html

#Add the following HTML:

#html

<!DOCTYPE html>
<html>
<head>
    <title>Welcome to My Website</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a sample page served by Nginx on Debian 12.</p>
</body>
</html>

#4.2: Configuring Nginx Server Block
#Back up the default Nginx configuration:

sudo mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak

#Create a new configuration file:

sudo nano /etc/nginx/sites-available/my_website

A#dd the following configuration:

nginx

server {
    listen 80;
    server_name your_domain.com www.your_domain.com;

    root /var/www/my_website;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

Enable the new site:

sudo ln -s /etc/nginx/sites-available/my_website /etc/nginx/sites-enabled/

#4.3: Restarting Nginx

#Check for syntax errors:

sudo nginx -t

#Restart Nginx:

sudo systemctl restart nginx