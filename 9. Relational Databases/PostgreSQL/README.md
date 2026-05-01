# PostgreSQL CLI exercise 

Create a database, restore the structure and contents of tables, query the tables, and dump/backup tables from the database all through the CLI

The database for this exercise was made available from this source: https://dev.mysql.com/doc/sakila/en/

The entity relationship diagram (ERD) for the sakila db:
<img width="600" height="600" alt="Screenshot 2026-04-30 at 8 17 57 PM" src="https://github.com/user-attachments/assets/a05f3faa-c649-41f8-8938-0b23e40a8bb4" />


## Initiate PostgreSQL session
```bash
> psql -U postgres
```

## create the db
```bash
> create database sakila;
```

show dbs:
```bash
> \l
```
<img width="833" height="214" alt="Screenshot 2026-05-01 at 1 26 37 PM" src="https://github.com/user-attachments/assets/917f017a-8d9c-4fd8-9bc5-49e1c0fb84b3" />

## Restore the db 
```bash
> \connect sakila;
```

```bash
> include sakila_mysql_dump.sql;
```

## Explore and query the tables
```bash
> \dt
```
<img width="413" height="348" alt="Screenshot 2026-05-01 at 1 39 31 PM" src="https://github.com/user-attachments/assets/4576c758-1a05-4cff-9413-b5ea2d361e5b" />


```bash
> \d store;
```
<img width="1199" height="284" alt="Screenshot 2026-05-01 at 1 40 57 PM" src="https://github.com/user-attachments/assets/095d5b7b-d7bf-42be-b4f0-b411d89cff18" />


```bash
>  SELECT * FROM store;
```
<img width="791" height="96" alt="Screenshot 2026-05-01 at 1 41 26 PM" src="https://github.com/user-attachments/assets/a6482823-61d0-41f9-8465-c511d38bfb10" />

## Dump/backup db and tables from the db
```bash
> pg_dump -U postgres -d sakila > sakila_db_pgsql_dump.sql 

```

```bash
> pg_dump --username=postgres --host=postgres --password --dbname=sakila --table=store --format=plain > sakila_store_pgsql_dump.sql

```

Verify the dump by viewing the contents of the dump file:
```bash
> cat sakila_db_pgsql_dump.sql

```
<img width="784" height="493" alt="Screenshot 2026-04-30 at 8 38 18 PM" src="https://github.com/user-attachments/assets/d778e14e-eefe-45e3-8db0-fec2a1e6f28a" />


