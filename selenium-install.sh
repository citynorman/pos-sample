#http://mike.ucoz.com/publ/programming/ubuntu/selenium_ubuntu_amazon_ec2_headless/8-1-0-4
#http://blog.protegra.com/2013/01/09/web-ui-testing-with-selenium-pt-3/

cd /usr/bin
#Install headless java
sudo aptitude install -y openjdk-6-jre-headless

#Fonts
sudo aptitude install -y xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic

#Headless X11 magic is here
sudo aptitude install -y xvfb

#We still demand X11 core
sudo aptitude install -y xserver-xorg-core

#Firefox installation
sudo aptitude install -y firefox

#memcached
sudo aptitude install -y memcached
sed -i -e 's/"l 127.0.0.1"/"l 0.0.0.0"/g' /etc/memcached.conf
sudo service memcached restart

#swap
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile   none    swap    sw    0   0' >> /etc/fstab

#Download Selenium server
wget http://selenium.googlecode.com/files/selenium-server-standalone-2.31.0.jar -P 

#run
Xvfb :0 -screen 0 1024x768x24 2>&1 >/dev/null &
export DISPLAY=:0
nohup xvfb-run java -jar selenium-server-standalone-2.31.0.jar > selenium.log &

Xvfb :99 -screen 0 1024x768x24 -ac 2&gt;&amp;1 &gt;/dev/null &
export DISPLAY=:99
java -jar /home/ubuntu/selenium-server-standalone-2.25.0.jar -port 8080 -maxSession 50
