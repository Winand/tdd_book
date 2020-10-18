Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.8
* virtualenv + pip
* Git

eg, on Ubuntu:

    adduser <username>
    usermod -aG sudo <username>
    # login as sudo user
    sudo apt update
    sudo apt install nginx git python3.8 python3.8-venv

## Nginx Virtual Host config

* see nginx.template.conf
* save config as /etc/nginx/sites-available/config__DOMAIN
* replace DOMAIN with, e.g., `sudo sed -i 's/DOMAIN/staging.my-domain.com/g' config__staging.my-domain.com`
* replace USER_NAME with created sudo user name
* put link into /etc/nginx/sites-enabled: `sudo ln -s /etc/nginx/sites-available/config__DOMAIN config__DOMAIN`
* disable default "welcome" config: `sudo rm /etc/nginx/sites-enabled/default`
* `sudo systemctl start nginx` or (if already started) `sudo systemctl reload nginx`

## Systemd service

* see gunicorn-systemd.template.service
* save config as /etc/systemd/system/gunicorn_DOMAIN.service
* replace DOMAIN with, e.g., staging.my-domain.com
* replace USER_NAME with created sudo user name
* load changed config: `sudo systemctl daemon-reload`
* autorun service: `sudo systemctl enable gunicorn_DOMAIN`
* start service after deployment: `sudo systemctl start gunicorn_DOMAIN`

## Folder structure:

Assume we have a user account at /home/username

    /home/username
    └── sites
        ├── DOMAIN1
        │    ├── .env
        │    ├── db.sqlite3
        │    ├── manage.py etc
        │    ├── static
        │    └── virtualenv
        └── DOMAIN2
            ├── .env
            ├── db.sqlite3
            ├── etc
