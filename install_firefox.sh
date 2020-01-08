wget -q https://download-installer.cdn.mozilla.net/pub/firefox/releases/66.0.3/linux-x86_64/en-US/firefox-66.0.3.tar.bz2
tar -xvf firefox-66.0.3.tar.bz2 -C /
ln -s /firefox/firefox /usr/bin
/usr/bin/firefox --version
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xvzf geckodriver*
cp ./geckodriver /usr/local/bin/geckodriver