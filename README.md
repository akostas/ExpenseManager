# ExpenseManager
This is an expense manager created with Django

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)

## Environmnetal Variables

This project uses a `.evn` file for configuration.
An example file is provided as `.env_dist`.

1. Copy the template:

```
cp .env_dist .env
```

2. Update values as needed (e.g., database name, user or password).

## First Commit: Dockerization

This repo demonstrates a reproducible Docker setup with:

- Django
- Postgres
- pgAdmin
- Docker Compose
- Environment variables

Later commits will add the Django project and features.

### Test commit

Execute the following commands and make sure that no error is generated:
```
docker build -t expense-manager .
docker run -p 8000:8000 expense-manager
```
