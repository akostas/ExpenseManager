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

## Quickstart

1. Build and start the image:

```
docker-compose up --build
```

2. Visit `http://localhost:8000/` to confirm that Django welcome page loads successfully.
3. Visit `http://localhost:5050/` to confirm that pgAdmin login page loads successfully.
3. Verify PostgreSQL is running:
    - Open a shell inside the expense_manager_postgres container
      ```bash
      docker exec -it expense_manager_postgres bash
      ```
      or use the Docker Desktop.

    - Connect to the database:
      ```bash
      psql -U admin -d expense_manager
      ```

    - Once inside `psql`, list databases:
      ```sql
      \l
      ```

      or the tables:
      ```sql
      \dt
      ```

## Test Expense Model using pgAdmin

- Visit pgAdmin site: `http://localhost:5050/`
- Login using the credentials in `.env` file (`PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD`).
- Add a new server.
- In `General` tab provide a `Name`, e.g., Expenses.
- In `Connection` tab enter the host name (`postgres`), the port (`5432`), the username and password. All this
  information has been provided in `.env` file.
- Head to `Servers/Expenses/Databases/expense_manager` and open the Query Tool (`Alt + Shift + Q`).
- Execute the following:

```
INSERT INTO expenses_expense (title, amount, date, description)
VALUES ('Burger', 21.37, '2025-09-07', 'Night out');
```

- Right click on `Schemas/public/Tables/expenses_expense` and select `View -> All Rows`. You should see the input
  provided above.

## Test API Endpoints

### POST /expenses/

#### Valid input

Send a POST API call to test the creation of an expense:

```
curl -i -X POST http://localhost:8000/api/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Dinner", "amount": 45.20, "date": "2025-09-07", "description": "Sushi"}'
```

It should return `201` status code, along with the provided json.

#### Bad Request `400`

Send a POST API call with missing items in the input, e.g., title:

```
curl -i -X POST http://localhost:8000/api/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"amount": 45.20, "date": "2025-09-07"}'
```

It should return a `400 Bad Request` with the following error message: `{"title":["This field is required."]}`

### GET /expenses/

Send a GET API call to retrieve all the Expense records:

```
curl -i -X GET http://localhost:8000/api/expenses/
```

It should return a `200 OK` with a list of JSON files, of all the Expense records.

### GET /expenses/<id> - retrieve a specific Expense

Send a GET API call to retrieve a specific Expense record, based on its ID.

```
curl -i -X GET http://localhost:8000/api/expenses/2/
```

It should return a `200 OK` with the specific Expense (in case it already exists).
If an Expense record with the specific ID doesn't exist then it should return `404 Not Found` with the following
message: `{"detail":"No Expense matches the given query."}`.
