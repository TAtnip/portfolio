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

Throughout the project I visited my API frequently to create endpoints to access data necessary for both populating an unfinished resistance training program and creating my visualizations in React-chart.js. This was a frequent learning process as I encountered new methods of accessing data through my API and became more efficient in pulling what I needed.

## React Components

Component driven development to me is akin to typical Object Oriented Programming, except this is performed in perhaps a more atypical language of JavaScript. Don't Repeat Yourself heavily applied during this stage, however prior to building my frontend I failed to perform the necessary design steps to take advantage of this initially. This can be seen by my SessionBuilderForm component which is very code heavy. This form was used to track and populate metrics from workout sessions. Following this experience, I adjusted and placed a greater emphasis on the design and integration of several components to tackle my visualizations portion of the project using react-chart.js by using components to create many of my drop-downs, toggle view switch, and the visualization itself.

![Screenshot 2024-12-06 at 10 37 31 AM](https://github.com/user-attachments/assets/5f38a62c-51d1-481e-826a-2b5d0cc203b7)

## Axios Interceptor: A Refreshing Piece of Code

My project takes advantage of JWT authentication which relies on access and refresh tokens to guarantee authorized access to user data. Throughout my project I ran into several issues with this process which I solved with various techniques. Firstly, as I used Safari for my development environment, I ran into issues with refresh and access tokens failing to be updated. Unfortunately I could not create a fix for this within the time constraints, and resulted in my switch to Google Chrome which functioned as intended. Then, I continued to have issues with my Axios api failing to create a new access token with the refresh token. This would cause the user to be logged out, and need to relogin based on the expiration time I had set in my Django backend framework. I solved this by looking into the Axios documentation and coming across an Axios interceptor which would perform what my code had been intended to do, except better. Once the access token had expired, if the refresh token was still active, the interceptor handles creation of a new access token for the user to continue to seamlessly utilize the application.

![Screenshot 2024-12-06 at 10 45 00 AM](https://github.com/user-attachments/assets/f2b75317-4067-4828-af2d-56484eeefed1)

## Visualizing Performance

The 'bread and butter' of this project is the visualizations it is capable of producing based on the resistance training data. It creates these visualizations by determining performance by muscle group (aimed towards bodybuilding) and by exercise (aimed towards powerlifting). If you have some experience in the realm, you might understand that there are certain times where you push your body to absolute failure, and others where you only get close to failure. The application in its current form tracks this, and utilizes an algorithm to determine your projected maximal performance as if you had pushed the lift to absolute failure. For the muscle group, it visualizes relative increase in performance as a percentage across all lifts which include this muscle group. The user is capable of adjusting the muscle groups in each lift as preferred as this is something which is consistently debated in the field already.

### Moving Forward

I believe there continues to be a significant number of improvements to be made in this project. Firstly, we can consider utilizing AI / ML to determine optimal loading strategies, optimal programs to accomplish specific goals based on the individual (think recommender systems and clustering to determine others the individual may be similar to, as well as the individuals prior performance). There is also a big avenue for adding in nutrition and sleep data as these have significant roles in performance based on research. For example, if we understand that the night before a session we had only 4 hours of sleep relative to our average of 8, we may have different performance and thus we may need to take our performance results with a grain of salt. In terms of UI/UX there are likely an almost infinite number of improvements including a wide variety of useful notifications. My primary goal for this project was not only to create something useful for the athlete, but also to learn these frameworks and tools mentioned throughout this document. Thus, UI/UX was a slightly lower priority. Regardless, I was able to harness some useful tools, such as Adobe's AI image generator to create a calm, themed background for the project. I also gained some valuable practice in CSS, which gave me even more experience in understanding the importance of React components.

## Conclusion

Overall, this project is something that I am proud of as at every step I was able to learn something new. From managing new frameworks, creating my own API, to the insertion of valuable techniques utilized in the field to determine performance, I gained a significant insight into the software development life cycle to create a functional product. Perhaps one day I may revisit this project to improve upon it further and make available to the general public as a free tool with the database hosted on an old laptop. 
