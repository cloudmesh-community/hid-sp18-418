SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAML=swagger.yaml
EXECDIR=mongodb/
OUTPUT=mongodb/
REQDIR=mongodb/server/flaskConnexion
RESTSERV=RESTServer

all: service start

service:
	mkdir $(EXECDIR)
	chmod 777 $(EXECDIR)
	wget https://www.dropbox.com/s/0730xoz8rboes7b/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate \
	-i $(YAML) \
	-l python-flask \
	-o $(OUTPUT) \
	-D supportPython2=true 

	sudo pip install virtualenv

	sudo virtualenv $(RESTSERV)

	sudo chmod 777 $(RESTSERV)

	sudo pip install requests==1.1.0 

	cp -r *.py $(EXECDIR)/swagger_server/controllers

	cd $(EXECDIR) && sudo pip install -r requirements.txt

start:
	cd $(EXECDIR) && python -m swagger_server
	cd ..

clean:
	sudo rm -rf $(OUTPUT)
	sudo rm *.jar
	sudo rm -rf $(RESTSERV)

docker-build:
	sudo docker build -t surya/swagger-mongo:latest .

docker-run:
	sudo docker run -d -p 8080:8080 surya/swagger-mongo

docker-stop:
	sudo docker stop $$(sudo docker ps -alq)

docker-pull:
	sudo docker pull surya/swagger-mongo

docker-delete:
	sudo docker rmi -f surya/swagger-mongo

docker-deleteall: docker-stop docker-delete

