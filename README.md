
## Course Work 6

---
This application is created based on the Django and React frameworks. And provides base functionality of ad site
such as create, update and delete ad, get a list of all ads or a detail info. You also can add comments under
each advertisement. This application provides authentication and authorization functions, so you can only update
or delete ads created by yourself.

An actions available in the application:

 - CRUD operations for ads and comments
 - CRUD operations for users with different roles (user and admin)
 - authentication and authorization functionality
 - different API routes with documentation

The project also have some backend test. To start it you have to add .env file and add DB=localhost environment 
variable.

---
The project's structure: 
 - frontend_react - frontend part of the application
 - market_postgres - docker-compose file for application created all necessary containers
 - skymarket - backend part of the application based on the Django framework with common structure 
 - requirements.txt - file with the project's dependencies 
 - README.md - this file with app info
 - .gitignore - file with folders and files to exclude from the repository
 ---
 The project was created in 17 March 2023 by Aleksey Mavrin