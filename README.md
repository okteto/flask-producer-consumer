# Producer consumer: Flask-MongoDB-Rabbitmq-NGINX

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/okteto/flask-producer-consumer)

This project shows how to create a consumer producer application with a simple compose and deploy into okteto using a docker-compose file.

## Prerrequisites
Create an Okteto secret with key `RABBITMQ_PASS` and `rabbitmq` as value

## Architecture

This application has the following components:
 - Producer: Generates random text and send it to a rabbitmq queue.
 - Consumer: Get the text from the queue, transform it to uppercase and save it on a MongoDB.
 - API: Gets data from the DB and show it to the user
