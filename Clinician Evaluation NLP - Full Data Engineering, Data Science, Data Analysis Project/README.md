# Clinician Evaluation NLP - Full Data Engineering, Data Science, Data Analysis Project - Python, Spark SQL - Microsoft Fabric, Synapse Data Engineering & Data Science, Azure, MLFlow, PowerBI, Spark

## Introduction
The purpose of this project was to inform clinicians, physicians, and case managers to reduce length-of-stay and identify those patients who will require further rehabilitation after the acute care visit.

This project was initially performed solely in a python notebook. I utilize and explore NLP packages such as re, gensim, and NLTK as well as gpt-4o from OpenAI on thier efficacy to analyze clinician evaluations for data. I work with Azure to obtain a free trial capacity in Microsoft Fabric by creating a second user with a free azure account, upload all evaluations to a container on azure, then utilize Microsoft fabric for data engineering including ETL and an automated data pipeline, MLFlow for the creation of four separate Machine Learning models, then PowerBI for analysis of the evaluation data.

## Architecture
![Architecture Diagram](https://github.com/user-attachments/assets/40888887-cda9-4d14-8352-58d57701f0c0)

## Technology Used
1. Programming language - Python
2. Scripting language - Spark SQL
3. Azure
  - Blob storage container
  - Creation of a new user
5. Microsoft Fabric
  - Data Lakehouse - Microsoft Lakehouse
  - MLFlow to manage and compare two classification and two regression models
  - PowerBI to create data visualizations

## Evaluations and HIPAA - [Evaluation Generator](https://github.com/TAtnip/portfolio/blob/ee25b6c206b6816446bff5977388cd733e0fe260/Clinician%20Evaluation%20NLP%20-%20Full%20Data%20Engineering%2C%20Data%20Science%2C%20Data%20Analysis%20Project/02%20Evaluation%20Generator.ipynb)
This project focuses on physical therapy evaluations in the acute care setting. Clinician evaluations are protected by HIPAA law due to the PHI which it contains. Therefore, for this project I created 10 pseudo-evaluations containing with different styles of writing that I have seen as a clinician. These evaluations were uploaded to a container in Microsoft Azure Blob Storage. In order to expand my sample size, I also created a dataset with 1000 evaluations randomly with data influenced by logic. 
![AzureBlobStorage](https://github.com/user-attachments/assets/6dd3a41d-38ec-4208-a9fd-5dd99e3d5eb0)

## Natural Language Processing Exploration - [NLP Notebook](https://github.com/TAtnip/portfolio/blob/ba4251338c2f8b1aae24861b32aeb512b72c17ee/Clinician%20Evaluation%20NLP%20-%20Full%20Data%20Engineering%2C%20Data%20Science%2C%20Data%20Analysis%20Project/01%20NLP%20GPT%20Exploration.ipynb)
This project is partially a documentation of my exploration of various natural language processing techniques to extract data from the evaluations. I utilized re and NLTK to pull information from short input fields such as ordering provider or fusion. I then explored the use of gensim and word mover's distance to analyze the efficacy of using this to pull information from paragraphs of prior level of function and mobility assessments. This proved to likely be inaccurate. After this, I attempted the OpenAI API with gpt-4o to analyze these paragraphs. While this took some tuning of the GPT, I found it to be accurate and effective. It was able to analyze an evaluaton at less than one cent per evaluation, which for this project is well worth it.

## Machine Learning Models - [Machine Learning Notebook](https://github.com/TAtnip/portfolio/blob/cf4e79340e89b42e479034e07954f4f603229b82/Clinician%20Evaluation%20NLP%20-%20Full%20Data%20Engineering%2C%20Data%20Science%2C%20Data%20Analysis%20Project/03%20ML%20Models.ipynb)
Within this project, I create models which are useful for predicting length-of-stay and the need for a rehabilitation stay after discharge. For the continuous variable, length-of-stay, I utilize a RANSAC regression model and a random forest regression model. For the categorical variable, need for rehabilitation, I utilize a logistic regression model and a random forest classification model. I tune these appropriately to determine the best model. 

## Solving the Fabric Free Trial Capacity
![Microsoft Fabric](https://github.com/user-attachments/assets/ced3769c-0372-4f63-9065-18efefcf4d17)

As it stands, I was unable to receive a fabric free trial capacity using my student email. This is due to settings associated with my tenant, the university I am attending. I was able to solve this by creating a free Azure trial account with which I was able to create a member user with it's own Microsoft Account. This account was then able to sign up for a free fabric trial capacity, which I used for the duration of this project.

![Azure Users](https://github.com/user-attachments/assets/aa882053-5ad9-4294-bd6f-2ffc9a65c656)

## Data Pipeline - [Bronze](https://github.com/TAtnip/portfolio/blob/337f4191c7d27a35b1f7dc13f82d488c41f07e0b/Clinician%20Evaluation%20NLP%20-%20Full%20Data%20Engineering%2C%20Data%20Science%2C%20Data%20Analysis%20Project/Microsoft%20Fabric%20Implementation/01%20Bronze%20Layer%20NLP.ipynb), [Silver](), [Gold]()
In Microsoft Fabric, I create a 3 layered pipeline. I refactored my previous notebooks containing the code to be ran outside of the cloud, to now be run in Microsoft Fabric. Spark integration with Microsoft Fabric notebooks was a game-changer, improving my ability to modify DataFrames as needed. The bronze layer extracts the raw data from the evaluations. The silver layer cleans the data and is where the natural language processing occurs. The gold layer applies some business logic for later use. This pipeline is automated to run weekly. I ran into various problems throughout this requiring me to create a custom python environment in Microsoft Fabric. During this time, I also notably ran into several bugs in Fabric leading to some inefficiencies such as the dreaded autoscroll bug. I found it was easier to modify my notebooks outside of fabric, then upload and run in Fabric for confirmation of functional code.
![Data Pipeline Successful Run](https://github.com/user-attachments/assets/ef22aaf0-e613-4b6f-b74f-5cb2475b11af)

## MLFlow
Within MLFlow, I was able to refactor my machine learning models and create a clear method of comparison of models. For some models I found it easier to log metrics and models manually. 

![Logistic Regression MLFlow](https://github.com/user-attachments/assets/90f9754c-f63a-4726-99a3-0dcfab0fec0b)

## PowerBI
In order to complete a few of my analyses in PowerBI, I took advantage of Spark SQL. Currently, it appears there is a lack of documentation on SQL queries in the lakehouse for Microsoft Fabric, as some functionality at this time no longer works. I also found there to be a small learning curve to performing powerBI analysis on Microsoft Fabric rather than desktop or the online platform. There were also a few bugs in PowerBI on this platform, one of which changes all of my colors on the diagram and adjusted all font sizes and even select font types in one swoop. 

## Conclusions
![PowerBI Dashboard page 1](https://github.com/user-attachments/assets/3cdb1286-beba-4691-9258-c3fdaace9cc6)

This project provides several conclusions which empower stakeholders. Firstly, based on the analysis, we can see that individuals who ambulate further during the evaluation (and likely during the first day post-operation) are more likely to discharge sooner and to their home environment. We also are able to derive inferences on pain. The charts created are able to suggest that patients in severe pain during the evaluation have a greater likelihood to discharge to a rehabilitation facility and tend to have longer length-of-stay. These inferences give physical therapists the information required to suggest further ambulations for patients during the evaluation as well as physicians and nursing staff the information to suggest greater pain medication or pain reducing modalities on the day of the evaluation. 

Based on the results of the machine learning models, our best model to predict length-of-stay was our Random Forest Regressor model with the parameters of {'max_depth': 3, 'max_features': None, 'min_samples_leaf': 8, 'min_samples_split': 30, 'n_estimators': 250}. For this model, we received an R^2 of 0.70. This tells us that our current data accounts for about **70%** of the variation in length-of-stay based on this model. Case managers, nurse managers, and hospital throughput facilitators can utilize this model to predict hospital capacity, staffing needs, and potential date of discharge. 

Our best model **based on accuracy** to predict need for rehabilitation is the Random Forest Classifier model with the parameters of {'max_depth': 6, 'minInstancesperNode': 8}. Based on the accuracy score of 0.86, we are able to predict the outcome of need for rehabilitation based on the evaluation alone with this data roughly **86%** of the time. Precision was 92.75% for this model, while recall was 79.01%. Precision for the logistic regression model was 81.51% and recall was 86.61%. Based on precision and recall, it may be **more beneficial to utilize the logistic regression model** for need_rehab. This is because it likely is more beneficial to identify patients who are more likely to need rehab as there are a number of hospital processes that benefit from beginning earlier such as referrals for authorization and reduced plan of care to reduce length-of-stay for that patient in the acute care setting and improve frequency of those patients that are not expected to discharge to rehab to reduce length-of-stay for those patients as well.

Finally, it is important that while the inferences of this project was mostly was created based on random evaluation data, it would not be very difficult to implement and adjust this towards real data. It would likely be as simple as refactoring some code to handle actual evaluations as well as funneling evaluations into Azure blob storage. 

Thank you for taking the time to look over this project. Throughout this project, I've learned a significant amount on Microsoft Fabric as well gained plenty of experience on the data cycle as a whole. If you have any questions, feel free to contact me.
