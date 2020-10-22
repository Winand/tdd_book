# Setup environment in Alpine
# pip packages are also installed with root permissions
# otherwise they will be installed in ~/.local which is not in PATH
apk add libstdc++  # required by VS Code
apk add python3  # pip3 is also installed
ln -s /usr/bin/python3 /usr/bin/python
pip3 install --upgrade pip
pip install -r ../requirements.txt  # pip install django gunicorn
pip install selenium
apk add gcc python3-dev musl-dev libffi-dev make openssl-dev #
pip install fabric3
pip install pylint
apk add git
