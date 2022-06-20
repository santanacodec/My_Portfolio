tag=latest
organization=atainter
image=myportfolio

build:	
	docker build --force-rm $(options) -t my_portfolio:latest .

build-prod:
	$(MAKE) build options="--target production"

push:
	docker tag $(image):latest $(organization)/$(image):$(tag)
	docker push $(organization)/$(image):$(tag)

compose-start:
	docker-compose up --remove-orphans $(options)

compose-stop:
	docker-compose down --remove-orphans $(options)

compose-manage-py:
	docker-compose run --r $(options) website python manage.py $(cmd)

start-server:
	python manage.py runserver 0.0.0.0:80