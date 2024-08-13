# Google Cloud Console Healthcare Project

## Introduction
This project dives into the use of modern data engineering and analytics intended to develop a knowledgebase of several medication's effects on medical condition stratified by various demographics. Effect was determined as length-of-stay. In this project I use tools such as Mage.ai to build an ETL pipeline on a virtual machine hosted on Google Cloud Platform. I utilize BigQuery for data warehousing and Looker Studio for data visualization while using Cloud Storage for the handling of the data throughout these processes.

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
Transformations of the data were first tested and accumulated on a notebook: [Python Transformations](https://github.com/TAtnip/portfolio/blob/51bbf7a5a942944dab176a722ff206ab7db8a101/Google%20Cloud%20Console%20Healthcare/Hospital%20Admission%20Data%20Transformation.ipynb). These transformations were then adapated to be used in a pipeline with Mage.ai to be uploaded to BigQuery. During the use of Mage.ai, I had ran into an issue which essentially was due to Git not being installed on the Google instance. After installing Git to the instance, I had a functional pipeline for my data.

![MageAI to BigQuery](https://github.com/user-attachments/assets/cb501b6e-0dfc-4979-8a63-e284c434a0df)

## BigQuery & Looker Studio
I found the use of BigQuery and Looker Studio to be very fluid and easy to use. This is in contrast to my time using Microsoft Fabric Lakehouse, SQL analytics endpoint, and PowerBI, which was clunky and at the time with a few frustrating bugs. A table was created on BigQuery to house the healthcare data.

![Screenshot 2024-08-12 at 9 11 23 PM](https://github.com/user-attachments/assets/e6121589-4c71-4412-a26a-f3231aca2029)

Finally, I was then able to incorporate this data into both a bar chart and a heat map pivot table to provide quick analysis of disparities by the various features which were included in the dataset: [Healthcare_dashboards](https://github.com/user-attachments/files/16593645/Hospital_dashboard.pdf)




