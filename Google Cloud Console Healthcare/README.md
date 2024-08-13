# Google Cloud Console Healthcare Project

## Introduction
This project dives into the use of modern data engineering and analytics intended to develop a knowledgebase of several medication's effects on medical condition stratified by various demographics. 
Effect was determined as length-of-stay. In this project I use tools such as Mage.ai to build an ETL pipeline on a virtual machine hosted on 
Google Cloud Platform. I utilize BigQuery for data warehousing and Looker Studio for data visualization while using Cloud Storage for the handling of the data throughout these processes.

## Architecture
![Architecturediagram](https://github.com/user-attachments/assets/8bd4b1b9-7651-40b3-ab7c-a503b29d06c8)

## Technology Used
1. Programming language - Python
2. Scripting language - SQL
3. Google Cloud Platform
  - Compute Instance
  - Cloud Storage
  - BigQuery
  - Looker Studio
4. Mage.AI data pipeline tool - **https://www.mage.ai/

## Dataset
The dataset used in this project was obtained on Kaggle, a data science community platform. The data consists of random data with features such as:
  - Medication
  - Medical Condition
  - Length-of-Stay
  - Age
  - Gender
  - Blood Type
  - Doctor
  - Hospital
  - Admission/discharge dates


## Data model
<img width="580" alt="Model" src="https://github.com/user-attachments/assets/c15d4118-fe24-408e-9c48-ef816a578d9e">

## Pipeline
Transformations of the data were first tested and accumulated on a notebook: [Python Notebook](Google Cloud Console Healthcare/Hospital Admission Data Transformations.ipynb)




