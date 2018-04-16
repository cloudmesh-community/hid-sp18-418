FROM python:2.7

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y mongodb-clients psmisc
EXPOSE 8080

WORKDIR /opt/default_controller/
COPY ./server/ /opt/default_controller/
RUN pip install -r requirements.txt
COPY ./bootstrap.sh bootstrap.sh
RUN chmod +x /opt/default_controller/bootstrap.sh