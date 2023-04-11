docker run -d --name data_challenge -p 5432:5432 -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=postgres -e POSTGRES_DB=DataAlkemyChallenge postgres

docker exec -it data_challenge psql -U postgres -d DataAlkemyChallenge