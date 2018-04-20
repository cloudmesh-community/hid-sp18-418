# Swagger

# Service Description

This service is used to list out all the currently existing databases in your MongoDB database. The service sucessfully
runs within the docker container as well.
 
# Instructions for Execution :

* Clone the repository with the command

    `
    git clone https://github.com/cloudmesh-community/hid-sp18-418.git
    `  

* Navigate to the project directory

    `
    cd /hid-sp18-418/swagger/cloudmesh/virtualdirectory
    `

#### MongoDB

##### Only if there is a mongod.lock file present, run the next command else ignore it:
* If incase MongoDB was not shutdown appropriately previously the mongod.lock file created when the service starts does not get dropped. 
Therefore, there is a need to drop that lock file manually to repair the database and start it again.

    `
    sudo rm /var/lib/mongodb/mongod.lock
    `
    
##### Start the MongoDB Service
* The MongoDB service instance is started with the command :
    `
    sudo service mongod start
    `
    
#### Makefile
* The swagger service can then be run locally with the command: 

    `
    sudo make all
    `  

##### Check the results using your browser
* The results are then available at http://0.0.0.0:8080/MongoDB  

# Sample Output

* These are the DB names of my all my DBs in my MongoDB database currently

    "[\"admin\", \"config\", \"local\", \"new_database\"]"

# Docker Commands

* The docker container can be built with the command: 

    `
    sudo make docker-build
    `  

* The docker container can be run with the command: 

    `
    sudo make docker-run
    `  

* The docker container can be stopped with the command: 

    `
    sudo make docker-stop
    `  

* The docker can be stopped and deleted with the command: 

    `
    sudo make docker-delete
    `  

* Clean can be executed with the command: 

    `
    sudo make clean
    `  

## Docker Container

* To run the container we can use the Docker Pull command

    `
    sudo make docker-pull
    ` 

## References
* https://stackoverflow.com/questions/31210973/how-do-i-seed-a-mongo-database-using-docker-compose  
* https://hub.docker.com/_/mongo/
* https://stackoverflow.com/questions/7744147/pymongo-keeps-refusing-the-connection-at-27017utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
