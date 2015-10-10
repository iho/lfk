##! make
all: local_init local_setup

local_init:
	sudo apt-get update --fix-missing -y
	sudo apt-get install -y python3-minimal python3-pip python3-dev gettext libjpeg-dev libfreetype6-dev\
       zlib1g-dev memcached mysql-server mysql-client python-mysqldb libmysqlclient-dev git
	sudo pip install virtualenv pip wheel setuptools ansible -U
	virtualenv venv -p python3 --always-copy

local_setup:
	ansible-playbook deploy/vagrant.yml
	rm -rf venv
	virtualenv venv  -p python3 --always-copy
	./venv/bin/pip install -r requirements/dev.txt

load_data:
	../venv/bin/python app/manage.py migrate
	# echo 'delete from vagrant.wagtailcore_site where hostname = "localhost";' | mysql
	# echo 'delete from vagrant.wagtailcore_page where title like "Welcome%";' | mysql
	# ../venv/bin/python app/manage.py loaddata dump
	cp -r app/core/fixtures/media public/

run:
	./venv/bin/python app/manage.py runserver 0.0.0.0:8000

.PHONY: deploy
deploy:
	tar -cf /tmp/deploy.tar app requirements --exclude='app/app/settings/local.py' --exclude='app/db.sqlite3'
	ansible-playbook deploy/beget.yml --tags="deploy"
	rm -rf /tmp/deploy.tar

backup:
	ansible-playbook deploy/beget.yml --tags="backup"

rollback:
	ansible-playbook deploy/beget.yml --tags="rollback" --ask-vault-pass

dump:
	ansible-playbook deploy/beget.yml --tags="dump" 

ddb:
	echo 'DROP DATABASE vagrant;' | mysql
	echo 'CREATE DATABASE vagrant CHARACTER SET utf8;' | mysql
