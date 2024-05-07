# DRF_BANKING_APP


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      </li>
	      <ul>
		       <li><a href="#built-with">Built With</a></li>
	     </ul>
	    <li>
	      <a href="#getting-started">Getting Started</a></li>
	      <ul>
	        <li><a href="#installation">Installation</a></li>
	        <li><a href="#prerequisites">Prerequisites</a></li>
</ul>
<li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
 
    
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

DRF_BANKING_APP  is a python project created using DjangoRestframework.
An Online banking Application with  Admin, Staff and Customers. The authorisation is done using the jwt bearer tokenisation .Various features like email ,user profile are included in this project

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

[Django]: https://docs.djangoproject.com/en/4.1/
[Django Restframework]: https://www.django-rest-framework.org/
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/rajeshpiyer/DRF-Banking-App.git
   ```
2. CD to project
   ```sh
   cd DRF-Banking-App
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



Follow the given steps to run the project in your localhost. 

### Prerequisites
* Install Python
  ```
  $ sudo apt install python3
  ```
* Create an environment
  ```
  $ python3 -m venv venv
  ```
  
* Activate environment
  ```
  $ source env/bin/activate
  ```

* Install dependencies
  ```
  $ (venv)  python -m pip install -r requirements.txt
  ```

* Make migrations
  ```
  $ (venv)  python3 manage.py makemigrations
  ```

* Migrate models
  ```
  $ (venv)  python3 manage.py migrate
  ```

* Run the project
  ```
  $ (venv)  python3 manage.py runserver
  ```




<!-- USAGE EXAMPLES -->
## Usage

Screenshots of the project using Postman

*User Login
 
 ![Screenshot from 2023-03-25 15-46-22](https://github.com/rajeshpiyer/DRF-Banking-App/blob/main/Screenshots/Login.png)
  
*List Accounts

 ![Screenshot from 2023-03-25 15-04-09](https://github.com/rajeshpiyer/DRF-Banking-App/blob/main/Screenshots/List%20Accounts.png)


*Deposit

![Screenshot from 2023-03-23 12-25-38](https://github.com/rajeshpiyer/DRF-Banking-App/blob/main/Screenshots/Deposit.png)

 
*Apply Loan

![Screenshot from 2023-03-23 13-04-04](https://github.com/rajeshpiyer/DRF-Banking-App/blob/main/Screenshots/Apply%20Loan.png)


*Email Alerts

![Screenshot from 2023-03-23 14-25-36](https://github.com/rajeshpiyer/DRF-Banking-App/blob/main/Screenshots/Mail%20-%20Account%20Created.png)

![updateblog](https://github.com/rajeshpiyer/DRF-Banking-App/blob/main/Screenshots/Budget%20Mail.png)


![Screenshot from 2023-03-24 00-18-34](https://github.com/rajeshpiyer/DRF-Banking-App/blob/main/Screenshots/Apply%20Loan%20-%20Mail.png)

*Account Statement

![Screenshot from 2023-03-25 23-45-19](https://github.com/rajeshpiyer/DRF-Banking-App/blob/main/Screenshots/Account%20STatement.png)




<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap
Customer Section

- [x] Registration & Login.

- [x] Create account & Set Budget.

- [x] Deposit, Withdraw and Transfer.

- [x] List Accounts and View Account Statements.

- [x] Apply for Loan and View Status.

- [x] Repay Loan.

- [x] Get Budget Alerts via Email and Use Expense categorization tools.

 Staff Section
 
- [x] Register & Login.

- [x] View Accounts & Loans. 

- [x] Approve Loans.

