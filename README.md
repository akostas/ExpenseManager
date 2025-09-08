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

## Create users

1. Enter `expense_manager_django` container:

```
docker exec -ti expense_manager_django sh
```

2. Use the provided script to create a user:

```
python scripts/create_user.py --username testuser --email test@test.com --password testpass
```

Expected output: `User 'testuser' created successfully.`

**NOTE**: A user is required to perform the following API calls.

## Test API Endpoints

### POST /expenses/

#### Valid input

Send a POST API call to test the creation of an expense:

```
curl -i -X POST -u testuser:testpass http://localhost:8000/api/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Dinner", "amount": 45.20, "date": "2025-09-07", "description": "Sushi"}'
```

It should return `201` status code, along with the provided json.

#### Bad Request `400`

Send a POST API call with missing items in the input, e.g., title:

```
curl -i -X POST -u testuser:testpass http://localhost:8000/api/expenses/ \
  -H "Content-Type: application/json" \
  -d '{"amount": 45.20, "date": "2025-09-07"}'
```

It should return a `400 Bad Request` with the following error message: `{"title":["This field is required."]}`

### GET /expenses/

Send a GET API call to retrieve all the Expense records:

```
curl -i -X GET -u testuser:testpass http://localhost:8000/api/expenses/
```

It should return a `200 OK` with a list of JSON files, of all the Expense records.

### GET /expenses/<id> - retrieve a specific Expense

Send a GET API call to retrieve a specific Expense record, based on its ID.

```
curl -i -X GET -u testuser:testpass http://localhost:8000/api/expenses/2/
```

It should return a `200 OK` with the specific Expense (in case it already exists).
If an Expense record with the specific ID doesn't exist then it should return `404 Not Found` with the following
message: `{"detail":"No Expense matches the given query."}`.

### PUT /expenses/<id> - update a specific Expense (full update)

Send a PUT API call to modify an Expense record, by providing all the required arguments.

```
curl -i -X PUT -u testuser:testpass http://localhost:8000/api/expenses/3/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated Book","amount":20.00,"date":"2025-09-07","description":"Updated"}'
```

It should return a `200 OK` with the updated Expense.

### PATCH /expenses/<id> - update a specific Expense (partial update)

Send a PATCH API call to modify an Expense record, by providing some of the arguments.

```
curl -i -X PATCH -u testuser:testpass http://localhost:8000/api/expenses/3/ \
  -H "Content-Type: application/json" \
  -d '{"amount":25.00}'
```

It should return a `200 OK` with the updated Expense.

### DELETE /expenses/<id> - delete a specific Expense

Send a DELETE API call to delete an Expense record.

```
curl -i -X DELETE -u testuser:testpass http://localhost:8000/api/expenses/3/
```

It should return a `204 No Content`.

## Filtering, Searching, Ordering, Pagination

### Filtering

#### Filter by exact title (case-sensitive)

```
curl -i -u testuser:testpass http://localhost:8000/api/expenses/?title=<exact word>
```

#### Filter by exact date

```
curl -i -u testuser:testpass http://localhost:8000/api/expenses/?date=2025-09-07
```

#### Filter by exact amount

```
curl -i -u testuser:testpass http://localhost:8000/api/expenses/?amount=23.17
```

### Searching (case in-sensitive)

It is possible to search with partial input in the title or description fields:

```
curl -i -u testuser:testpass http://localhost:8000/api/expenses/?search=dinner
```

### Ordering

The results may be returned ordered among the following fields: id, date, amount. By default, they are returned in
ascending order based on their id.

#### Example 1: Ascending order based on date

```
curl -i -u testuser:testpass http://localhost:8000/api/expenses/?ordering=date
```

#### Example 2: Descending order based on the amount

```
curl -i -u testuser:testpass http://localhost:8000/api/expenses/?ordering=-amount
```

**NOTE**: All of the above may be combined, for example:

```
curl -i -u testuser:testpass http://localhost:8000/api/expenses/?search=dinner&ordering=-amount
```

### Pagination

Pagination has been implemented, so that only 10 items are returned per page. If the GET call is sent like this (
default):

```
curl -i -u testuser:testpass http://localhost:8000/api/expenses/
```

then only the first 10 items will be returned, and the response will inform for the total amount that exist. In order to
view the next pages, a GET call similar to the following shall be made:

```
curl -i -u testuser:testpass http://localhost:8000/api/expenses/?page=2
```
