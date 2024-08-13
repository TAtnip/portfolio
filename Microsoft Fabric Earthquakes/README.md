# Microsoft Fabric Earthquakes - Python - USGS API, Microsoft Fabric, PowerBI

## Introduction
This project uses the United States Geological Survey API to extract data, transform it using Python, and load into an SQL analytic endpoint on Microsoft fabric to perform data analysis and create data visualizations on PowerBI. The primary purpose was to create a map visualization using latitude and longitude data, however unfortunately this was not available on a Fabric free trial capacity. 

## Technology Used
1. Programming language - Python
2. USGS API - https://earthquake.usgs.gov/fdsnws/event/1/
3. Microsoft Fabric
  - Data Lakehouse
  - [Custom Python Environment](https://github.com/TAtnip/portfolio/blob/7e2f106231b67ed0889d87382c93c57845cc69e0/Microsoft%20Fabric%20Earthquakes/Python%20environment.png)
  - PowerBI

## Automated ETL Data Pipeline - [Bronze](https://github.com/TAtnip/portfolio/blob/03e81f22bea3e894f7bc5483a3ed76a6fe5d8901/Microsoft%20Fabric%20Earthquakes/Bronze%20Layer.ipynb), [Silver](https://github.com/TAtnip/portfolio/blob/4596bc49b6834a61ddbb8d9d0cae5b89930367b5/Microsoft%20Fabric%20Earthquakes/Silver%20layer.ipynb), [Gold](https://github.com/TAtnip/portfolio/blob/e564ade9a69d22fb8ad7b5a378c8010ed975d0de/Microsoft%20Fabric%20Earthquakes/Gold%20Layer.ipynb)
This project primarily involves the creation of an automated ETL data pipeline using medallion architecture to collect daily data from the USGS API. Information was queried from the API by modifying start and end dates. Automation was performed by using dynamic base parameters to extract data based on date. The pipeline then funnels this data into Lakehouse and subsequent SQL analytics endpoint to be used in a PowerBI visualization. The bronze layer extracts the raw data from the API. The silver layer performs data cleansing and transformations on the raw data which is essentially 'just-enough'. Lastly, the gold layer includes the data cleansing and transformations for specific business purposes with business logic taken into account. 

![PowerBI Automated Dataflow](https://github.com/user-attachments/assets/847fecd8-d2c9-42db-a2df-fba07445a14b)


## PowerBI Report
This was an unfortunate part of the project. As I am using a Fabric free trial capacity, there are certain features which I am unable to access. Map visualizations are one of them. This map was intended to be essentially a global heat map of earthquakes over time with tool tips detailing informations such as severity. 

![PowerBI Map Report](https://github.com/user-attachments/assets/5b363784-33a9-4cf9-83cd-3dc27d55f21c)


