# Human Resources Website Project

## Project Overview

This project aims to create a Human Resources website using the Django framework. The website allows users to manage employee data, submit and review vacation requests, and perform various HR-related tasks.

### Collaborators

- [Abdelrhman Mostafa](https://github.com/3bde1r7man)
- [Seif Ibrahim](https://github.com/Seif-Ibrahim1)
- [Ahmed Hanfy](https://github.com/ahanfybekheet)
- [Youssef Mohamed](https://github.com/you22ef)
- [Shahd Osama](https://github.com/shahdosama10)
- [Salma Abdelaziz](https://github.com/Salmaabdelaziz271)


## Functionalities

### 1. Employee Management

- User can **add a new employee** to the system.
  - Employee data includes:
    - Id
    - Name
    - Email
    - Address
    - Phone number
    - Gender
    - Marital status
    - Number of available vacation days
    - Number of actual approved vacation days
    - Salary
    - Date of birth

- User can **update existing employee data**.

- User can **delete an existing employee data** through a delete button in the edit employee data page with a confirmation dialogue for the action before deletion occurs.

- User can **search for an employee by name** in a search for an employee screen, and employees with similar names should be rendered as a table.

### 2. Vacation Management

- User can select a specific employee after searching to submit a **vacation form** for the same employee.
  - Vacation form includes:
    - From date
    - To date
    - Reason
    - Status (initially set to "submitted")
    - Chosen employee id

- User can **review all "submitted" vacations** of different employees with the ability to approve or reject the vacation submitted.

- If user clicks on **approve button**:
  - Mark vacation as approved
  - Increment employee actual number of vacation days
  - Decrement available number of vacation days for that employee
  - Remove vacation from submitted vacations page

- If user clicks on **reject button**:
  - Mark vacation as rejected
  - Remove vacation from submitted vacations page

### 3. Navigation

- Website should have a well-designed **navigation bar** to go through all pages and a home page.


## How to Run

1. Run the development server:

```bash
python manage.py runserver
```

Access the website at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
