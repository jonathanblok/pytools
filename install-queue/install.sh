#!/bin/sh
echo "=== Escalating Privelige ==="
sudo su
echo "=== Updating Apt Cache ==="
apt-get update
echo "=== Installing Java8 JDK ==="
apt-get install openjdk-8-jdk-headless -y
echo "=== Installing Maven ==="
apt-get install maven -y 
echo "=== Installing Tomcat7 ==="
apt-get install tomcat7 -y
echo "=== Shutting Down ==="
poweroff


