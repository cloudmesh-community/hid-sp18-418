FROM mongo:latest
EXPOSE 27017
FROM ubuntu:16.04

RUN apt-get update -q && apt-get install -qy \
    build-essential \
    python-dev \
    python-pip \
    wget \
    curl \
    git-core \
    default-jre \
    software-properties-common -y

#RUN apt-get update -q && apt-get install -qy default-jre 


RUN pip install --upgrade pip
RUN pip install connexion
RUN pip install pymongo
RUN pip install six
#RUN pip install json
RUN git clone https://github.com/cloudmesh-community/hid-sp18-418.git

WORKDIR /hid-sp18-418/swagger-docker

RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
EXPOSE 8080

RUN make service

CMD ["make", "start"]
