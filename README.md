# Challenge Data Analytics - Alkemy

Link to the challenge --> [Challenge Readme](challenge.md)

### Prerequisites

Create a virtual environment
> python -m venv myvenv

Install all dependencies
> pip install -r requirements.txt

### Data Research

### Setup Database

` docker run -d --name data_challenge -p 5432:5432 -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=postgres -e POSTGRES_DB=DataAlkemyChallenge postgres `

### Access database

`docker exec -it data_challenge psql -U postgres -d DataAlkemyChallenge`



