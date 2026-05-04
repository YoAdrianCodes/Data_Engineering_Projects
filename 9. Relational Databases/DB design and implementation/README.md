# DB design and implementation with pgAdmin

Identify the entities and attributes for the HR department of a company and create an ERD. Use that ERD to create the tables and relationships for the db, then upload data to those tables all through pgAdmin.

Simplified three step approach for the DB design:
1. Understand the requirements
2. Conceptual and logical design
3. Physical design

## Understand the Requirements
Initial entities for a HR department of a global company are the following:
* global regions
* locations
* counties
* departments
* employees
* jobs
* job_history

Potential attributes for each entity:
global regions:
* region_id
* region_name

countries:
* country_id
* country_name
* region_id (multiple different countries have one region)

Locations:
* location_id
* street_address
* postal_code
* city
* state
* country_id (multiple different locations have one country)

Departments
* department_id
* department_name
* manager_id
* location_id

Employees:
* employee_id
* first name
* last name
* email
* hire date
* job id
* salary
* manager id
* department id

jobs:
* job id
* job title

job_history:
* employee id
* start date
* end date
* job id
* department id


## Conceptual and Logical design (ERD)
Created an ERD with data types and relationships included:
<img width="974" height="921" alt="Screenshot 2026-05-03 at 7 28 25 PM" src="https://github.com/user-attachments/assets/66bb583c-512c-41b1-853c-4067228ce939" />


## Physical Design
Generate and execute the SQL command in pgAdmin to create the schema of the HR database from the ERD page. The upload the .tar file to restore the data in the database.


