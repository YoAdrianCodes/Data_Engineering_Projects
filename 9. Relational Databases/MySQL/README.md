# MySQL CLI exercise 

Create a database, restore the structure and contents of tables, query the tables, and dump/backup tables from the database all through the CLI

The database for this exercise was made available from this source: https://dev.mysql.com/doc/sakila/en/

The entity relationship diagram (ERD) for the sakila db:
<img width="600" height="600" alt="Screenshot 2026-04-30 at 8 17 57 PM" src="https://github.com/user-attachments/assets/a05f3faa-c649-41f8-8938-0b23e40a8bb4" />


## Initiate mySQL session
```bash
> mysql -u root -p
```

## create the db
```bash
> create database sakila;
```

```bash
> SHOW DATABASES;
```
<img width="258" height="189" alt="Screenshot 2026-04-30 at 8 26 02 PM" src="https://github.com/user-attachments/assets/ff4c1df3-7a90-4866-9a56-d29c63ea0c88" />

## Restore the db 
```bash
> use sakila;
```

```bash
> source sakila_mysql_dump.sql;
```

## Explore and query the tables
```bash
> SHOW FULL TABLES WHERE table_type = 'BASE TABLE';
```
<img width="345" height="366" alt="Screenshot 2026-04-30 at 8 30 23 PM" src="https://github.com/user-attachments/assets/832a93a2-3af1-4c46-988f-dfd9d60870ab" />


```bash
> DESCRIBE staff;
```
<img width="1074" height="296" alt="Screenshot 2026-04-30 at 8 31 36 PM" src="https://github.com/user-attachments/assets/6fc9c5be-7c11-4907-b201-0fafafecf7f1" />


```bash
>  SELECT * FROM staff;
```
<img width="1788" height="131" alt="Screenshot 2026-04-30 at 8 32 36 PM" src="https://github.com/user-attachments/assets/731dd622-e923-4300-bdc7-c14c76e70571" />

## Dump/backup db and tables from the db
```bash
> mysqldump --host=mysql --port=localhost --user=root --password sakila > sakila_db_mysql_dump.sql

```

```bash
> mysqldump --host=mysql --port=localhost --user=root --password sakila staff > sakila_staff_mysql_dump.sql

```

Verify the dump by viewing the contents of the dump file:
```bash
> cat sakila_db_mysql_dump.sql

```
<img width="784" height="493" alt="Screenshot 2026-04-30 at 8 38 18 PM" src="https://github.com/user-attachments/assets/d778e14e-eefe-45e3-8db0-fec2a1e6f28a" />


