make:
	docker build -t registry.jorgeadolfo.com/epav-api:1.1.0 -f docker/Dockerfile .

rund:
	docker run -d --rm --name server-api -p 5000:5000 -e FLASK_ENV=development registry.jorgeadolfo.com/epav-api

run:
	docker run -it --rm --name server-api -p 5000:5000 -e FLASK_ENV=development registry.jorgeadolfo.com/epav-api

stop:
	docker kill server-api