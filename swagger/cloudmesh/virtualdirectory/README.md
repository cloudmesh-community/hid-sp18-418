# Swagger

# Overview
This service is used to list out all the currently existing databases 
in your MongoDB.
 

The service can be run from the root of the project locally with the command: 

`
sudo make all
`  

If incase the connection is refused, we need to remove the mongod.lock file and restart the service before running the make all command:
`
sudo rm /var/lib/mongodb/mongod.lock
`

`
sudo service mongod start
`

The docker container can be built with the command: 

`
sudo make docker-build
`  

The docker container can be run with the command: 

`
sudo make docker-run
`  

The docker container can be stopped with the command: 

`
sudo make docker-stop
`  

The docker can be stopped and deleted with the command: 

`
sudo make docker-delete
`  

Clean can be executed with the command: 

`
sudo make clean
`  

The results are available at http://0.0.0.0:8080/MongoDB  


## References
https://stackoverflow.com/questions/31210973/how-do-i-seed-a-mongo-database-using-docker-compose  
https://hub.docker.com/_/mongo/
https://stackoverflow.com/questions/7744147/pymongo-keeps-refusing-the-connection-at-27017?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
