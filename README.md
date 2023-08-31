# Fast_api_deploy

how to setup postgres in docker 

RUN -->
1.  sudo docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword postgres

2. docker exec -it my-postgres bash

3. psql -U postgres

RUN docker

sudo docker compose up