REGISTRY='registry.jorgeadolfo.com'
IMAGE='epav-api'
PORT=5000
VERSION=`cat version`
NAME=$(IMAGE)
FULLNAME=$(REGISTRY)/$(IMAGE):$(VERSION)

make:
	@docker build -t $(FULLNAME) -f docker/Dockerfile .

rund:
	@docker run -d --rm --name $(NAME) -p $(PORT):5000 -e FLASK_ENV=development $(FULLNAME)

run:
	@docker run -it --rm --name $(NAME) -p $(PORT):5000 -e FLASK_ENV=development $(FULLNAME)

stop:
	@docker kill $(NAME)

logs:
	@docker logs -f $(NAME)

test:
	@echo $(FULLNAME)
