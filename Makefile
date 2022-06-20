build:	
	docker build --force-rm $(options) -t my_portfolio:latest .

build-prod:
	$(MAKE) build options="--target production"

compose-start:
	docker-compose up --remove-orphans $(options)

compose-stop:
	docker-compose down --remove-orphans $(options)

compose-manage-py:
	docker-compose run --r $(options) website python manage.py $(cmd)