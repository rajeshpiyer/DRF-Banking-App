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

*User Registeration
 
 ![Screenshot from 2023-03-25 15-46-22](https://user-images.githubusercontent.com/96044398/227735637-3a599214-f194-474c-b97f-3aae2d39b25e.png)
  
*Email

 ![Screenshot from 2023-03-25 15-04-09](https://user-images.githubusercontent.com/96044398/228198915-8646148d-2b8f-46c2-9d59-c2f460cc853b.png)


*Login 
JWT Token

![Screenshot from 2023-03-23 12-25-38](https://user-images.githubusercontent.com/96044398/227235956-2d3de5bf-830d-433b-9417-74730b63ef24.png)

 
*Create Blog 

![Screenshot from 2023-03-23 13-04-04](https://user-images.githubusercontent.com/96044398/227236510-b3bd7327-62ef-4380-b706-e7580f9a7ccc.png)


*List blog

![Screenshot from 2023-03-23 14-25-36](https://user-![updateblog](https://user-images.githubusercontent.com/96044398/227735425-1f06266a-72de-459f-8b65-5c89fc9fa3c1.png)


*Update Blog

![updateblog](https://user-images.githubusercontent.com/96044398/227736801-51399fb7-c480-485d-98d7-c95a031205ed.png)


*Add comments

![Screenshot from 2023-03-24 00-18-34](https://user-images.githubusercontent.com/96044398/227736038-5f022d5c-7609-4d32-bfb3-f9be3e0369a5.png)

*List comment using blogid

![Screenshot from 2023-03-25 23-45-19](https://user-images.githubusercontent.com/96044398/227735361-671525b6-c248-4c00-8edb-d1dbe3c0f288.png)

*Update comment

![Screenshot from 2023-03-25 23-50-07](https://user-images.githubusercontent.com/96044398/227735474-62988de8-142f-4fd6-b7c2-450ff4618d3a.png)


*Admin list blog

![Screenshot from 2023-03-26 00-28-00](https://user-images.githubusercontent.com/96044398/228199790-78d0cff5-e89e-41eb-8d5c-69f97b01f438.png)


*Admin delete blog

![Screenshot from 2023-03-26 00-26-58](https://user-images.githubusercontent.com/96044398/227736251-ec3172fa-a5ee-441a-a2c2-cbafe9720ced.png)

![Screenshot from 2023-03-26 00-28-00](https://user-images.githubusercontent.com/96044398/227736258-0ce59c75-9c8c-462c-940e-e64a0537a622.png)


*Admin list comment

![Screenshot from 2023-03-24 02-12-45](https://user-images.githubusercontent.com/96044398/227735825-6a9b0a63-a41a-4752-9061-d8869ed99f24.png)

*Admin delete comment

![Screenshot from 2023-03-26 00-30-24](https://user-images.githubusercontent.com/96044398/227736345-dc69989f-f571-47ae-8f48-545866fcce8b.png)


*Token refresh

![Screenshot from 2023-03-25 23-53-23](https://user-images.githubusercontent.com/96044398/227735522-71afb5ef-807b-4c4a-857c-62a992a281a7.png)

*Token blacklist

![Screenshot from 2023-03-03 12-14-50](https://user-images.githubusercontent.com/96044398/222651928-4f8658ef-18c2-4c4c-a966-d0846a4bb7bb.png)




<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap
UserSection

- [x] User Authentication:a.Users will be able to create an account, log in, and log out.

- [x] Newly registered users should receive an email upon registration.

- [x] Blog Posts:a.Users can perform CRUD operations in their own blog posts.

- [x] Users can view the list & details of all blog posts, including blogs posted byother users.

- [x] Users should be able to upload image attachments with the blog.

- [x] A blog post should have a title, content, created time & updated time. The restof the fields should be added as per requirement.

- [x] Users can add comments to any posts.

- [x] A user should be able to see all the comments that are posted under a blogpost.

- [x] Only the author of the comment will be allowed to edit or delete thecomments.

- [x] The created time & updated time of the comment should be saved.

 AdminSection
 
- [x] AdminSection1.Authentication:Admins will be able to log in and log out.

- [x] A new admin user can only be registered by another authenticated adminuser. 

- [x] Blog Posts:Admins can view the list & details of all blog posts.

- [x] Admins should be able to delete blog posts.

- [x] Comments:Admins can view the list of all comments under a post.

- [x] Admins should be able to delete comments.




<p align="right">(<a href="#readme-top">back to top</a>)</p>
