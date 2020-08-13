# Setup environment in Alpine
apk add libstdc++
apk add python3
ln -s /usr/bin/python3 /usr/bin/python
pip3 install --upgrade pip
pip install django
pip install selenium
pip install pylint
apk add git
