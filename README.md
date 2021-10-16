# Kong Gateway API

Kong is an open source Gateway that provides a layer between an application and
its users. It might implement many useful features such as authentication, rate
limit and others.

This project implements a simple webpage with flask and an even simpler api
that return date and time. All of them managed using kong.

For simplicity, docker compose is being used to orchestrate all of those
containers. Nevertheless a k8 may be used just fine.

## Useful scripts

1. Before doing anything, make sure the custom images are build so it can start
with no issues.

    $ docker-compose build

2. If it is the first time the aplication is being built, a migration is needed
on the postgres database. It bootstrap kong on the database. Start by running:

    $ docker-compose run kong-migrations

3. Start kong by running the kong service, the others services such as apis and
database will start right way.

    $ docker-compose run kong

4. If modifications are done on the kong.yaml, run the syncronization service,
deck is used to do that. Be aware to have kong running before run the command
bellow.

    $ docker-compose run deck

## Authorization on the API Gateway

This project uses JWT tokens to authorize calls between user and api! Create a
valid jwt token on [JWT webisite](https://jwt.io/) using the iss (key provided
on kong.yaml) as payload and the secret (also provided) to verify signature.
For more on that please refer to JWT Kong Plugin
[DOCS](https://docs.konghq.com/hub/kong-inc/jwt/).
