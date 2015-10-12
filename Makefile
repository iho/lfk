##! make
all: local_init local_setup

local_init:
	sudo apt-get update --fix-missing -y
	sudo apt-get install python-pip -y
	sudo pip install virtualenv ansible

local_setup:
	ansible-playbook deploy/vagrant.yml

load_data:
	../venv/bin/python app/manage.py migrate
	echo 'delete from vagrant.wagtailcore_site where hostname = "localhost";' | mysql
	echo 'delete from vagrant.wagtailcore_page where title like "Welcome%";' | mysql
	../venv/bin/python app/manage.py loaddata dump
	cp -r app/core/fixtures/media public/

run:
	../venv/bin/python app/manage.py runserver 0.0.0.0:8000

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
	ansible-playbook deploy/beget.yml --tags="dump" --ask-vault-pass

ddb:
	echo 'DROP DATABASE vagrant;' | mysql
	echo 'CREATE DATABASE vagrant CHARACTER SET utf8;' | mysql
