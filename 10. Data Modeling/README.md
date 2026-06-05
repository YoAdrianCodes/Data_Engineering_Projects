# Project Overview
This directory contains projects relating to design, modeling and implementation for data warehouses

## Fact and Dimension tables with a Star schema
I am assigned the creation of a data warehouse for the provided CSV file with billing data from a cloud service provider. For this exercise the schema will be Star with Fact and Dimension tables, supporting complex queries relating to:
* Billing by year, month, quarter
* Average billing per customer
* Billing by country, industry, and category
* Trends over time


Five rows picked at random from the CSV file:

<img width="636" height="209" alt="Screenshot 2026-06-04 at 5 56 57 PM" src="https://github.com/user-attachments/assets/f1b0bcc4-d01b-489c-b426-ba5727247924" />

There are 6 columns currently, 2 numeric, 1 date format, and 3 character. Since I know what type of queries the data warehouse will need to support I am better able to design the fact and dimension tables.The fact in this data is the bill which is generated monthly, the transaction. The dimension tables will be both customer and date information, the descriptive context. 

Initial ERD:
<img width="964" height="704" alt="Screenshot 2026-06-04 at 7 30 50 PM" src="https://github.com/user-attachments/assets/d5b68957-00c5-48c2-b116-592f420717b9" />


Create database through CLI:

<img width="485" height="44" alt="Screenshot 2026-06-04 at 7 33 39 PM" src="https://github.com/user-attachments/assets/820f93d1-9258-4fe5-bcb4-2381aa2ad825" />

Actual ERD:

<img width="823" height="707" alt="Screenshot 2026-06-04 at 5 38 55 PM" src="https://github.com/user-attachments/assets/628f1f2a-2d92-4bb6-9a9e-805dbceb351d" />
