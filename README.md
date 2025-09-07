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

## Test Expense Model

- Visit pgAdmin site: `http://localhost:5050/`
- Login using the credentials in `.env` file (`PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD`).
- Add a new server.
- In `General` tab provide a `Name`, e.g., Expenses.
- In `Connection` tab enter the host name (`postgres`), the port (`5432`), the username and password. All this information has been provided in `.env` file.
- Head to `Servers/Expenses/Databases/expense_manager` and open the Query Tool (`Alt + Shift + Q`).
- Execute the following: 
```
INSERT INTO expenses_expense (title, amount, date, description)
VALUES ('Burger', 21.37, '2025-09-07', 'Night out');
```
- Right click on `Schemas/public/Tables/expenses_expense` and select `View -> All Rows`. You should see the input provided above.
