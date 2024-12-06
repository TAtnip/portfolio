# Project Performance: A Django, React Web Application

## Introduction

Fitness Applications are typically a structured notes application. This project aims to build upon the average fitness tracking application in order to provide users with the ability to easily create their own data visualizations to understand their athletic performance. I performed this with the latest research in mind and tailored the application in it's current form to athletes participating in resistance training with goals of bodybuilding or powerlifting. 

![Screenshot 2024-12-06 at 10 18 36 AM](https://github.com/user-attachments/assets/1d440bb1-77a7-4bb3-9914-86a62749d981)

## Technology Used
1. Programming Languages - Python, JavaScript
2. Frameworks - Django, React
3. Database - PostgreSQL
4. Authentication - JWT
5. Key Data Visualization Package - React-chart.js

## Project Setup

This project relies on a Django backend API served by a PostgreSQL database to handle fitness data management. The backend also implements JWT authentication to handle secure data authentication and authorization for the user. The React frontend brings the power of component-driven UI with quick response times to improve the user experience throughout the application. 

Admittedly, I ran into several issues when first tackling this project. I had not used either framework before and thus there was a learning curve which involved determining how to best create my own RESTful API, how to harness components within React, and how to utilize Axios to obtain access and refresh tokens to provide both a seamless and secure experience for the user.

## RESTful API

The creation of my API was a segmental one. First, I determined an optimal database structure. During this time, I also learned about the Django User model which was very helpful in the integration of JWT authentication to hash and store passwords. Initially, my passwords were not hashed. After some research, it turned out that in my Serializer I needed to capitalize on the set_password() method to assure that this occurred on the creation of a user through my React frontend. 
![Screenshot 2024-12-06 at 10 01 40 AM](https://github.com/user-attachments/assets/7650f569-f5a1-491e-a056-832e39765f5d)

Throughout the project as well I visited my API frequently to create endpoints to access data necessary for both populating an unfinished resistance training program and creating my visualizations in React-chart.js. 



To be continued!
