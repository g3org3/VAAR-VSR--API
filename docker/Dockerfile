FROM registry.jorgeadolfo.com/epav:1.0.1

RUN apt-get update && apt-get install -y unzip

RUN mkdir /server-api
WORKDIR /server-api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY docker/entrypoint.sh .
RUN chmod +x entrypoint.sh
COPY lib .

RUN mkdir output
RUN mkdir files
COPY files files

ENTRYPOINT ["/server-api/entrypoint.sh"]
