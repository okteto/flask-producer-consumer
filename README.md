# Producer consumer: Flask-MongoDB-Rabbitmq-NGINX

This project shows how to create a consumer producer application with a simple compose and deploy into okteto using a docker-compose file.

## Architecture

This application has the following components:
 - Producer: Generates random text and send it to a rabbitmq queue.
 - Consumer: Get the text from the queue, transform it to uppercase and save it on a MongoDB.
 - API: Gets data from the DB and show it to the user
