# Kitschy. Co Backend

## PostgreSQL

1. First [install PostgreSQL](https://www.postgresql.org/download/) into your system.
    - There are a lot of intricacies in the install process so be careful.
2. Enter `psql` in your terminal to enter the **PostgreSQL CLI**.
    - Make sure you have a user named `postgres` with the password `postgres`, as this is what is defined in `backend/settings.py`
3. Create the `kitschy_co_db` database locally.
```sql
-- As `postgres` user
CREATE DATABASE kitschy_co_db;
```
4. You can now safely exit the CLI.
```sql
\q
```

## Django

> Make sure you have executed the initial instructions on the repository `README.md`

1. Migrate the database.
```bash
# for windows
python manage.py makemigrations
python manage.py migrate

# for unix (alternative)
./manage.py makemigrations
./manage.py migrate
```
