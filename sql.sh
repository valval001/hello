#!/bin/bash

sudo apt update
sudo apt install wget -y
sudo wget https://dev.mysql.com/get/mysql-apt-config_0.8.29-1_all.deb
sudo apt install ./mysql-apt-config_*_all.deb
sudo dpkg-reconfigure mysql-apt-config
sudo apt update
sudo apt install mysql-server
sudo systemctl enable --now MySQL
sudo systemctl status mysql
mysql --version
sudo mysql_secure_installation
mysql -u root -p
