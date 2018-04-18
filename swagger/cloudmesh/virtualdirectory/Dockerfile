FROM ubuntu:latest
COPY . /app
WORKDIR /app/

EXPOSE 8080

RUN pwd

RUN ls

RUN apt-get update -y

RUN apt-get install -y python-pip python-dev build-essential

RUN apt-get install -y vim

RUN apt-get update -y

RUN apt-get -f install

RUN apt-get install -y default-jdk

RUN pip install psutil
RUN pip install --upgrade pip
RUN apt-get install wget

RUN apt-get install sudo

RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

RUN echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

RUN sudo apt-get update

RUN sudo apt-get install -y mongodb-org

RUN pip install connexion

RUN pip install pymongo

RUN sudo mongod --dbpath /app/data/db --fork --logpath /app/mongodb.log

RUN sudo mongo --host 127.0.0.1:27017 > out.txt &

EXPOSE 27017

RUN make service

WORKDIR /app/flaskConnexion

ENTRYPOINT ["python","-m","swagger_server"]
