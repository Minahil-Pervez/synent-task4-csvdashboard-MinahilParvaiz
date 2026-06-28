# 📊 CSV to Dashboard

## Overview
CSV to Dashboard is an interactive data visualization application developed using Streamlit. The application allows users to upload any CSV dataset and explore it through dynamic charts, summary statistics, filtering options, and basic data cleaning features.
This project was completed as **Task 4 (Basic Level)** of the Synent Data Science Internship.

# Objective
The objective of this project is to transform raw CSV datasets into an interactive dashboard that enables users to understand and analyze their data without writing additional code.

## Problem Statement
Organizations often store information in CSV files. Analyzing these files manually can be difficult, especially when the dataset is large or contains missing values and duplicate records.
This project provides an interactive dashboard that simplifies data exploration and visualization through an easy to use interface.

## Dataset
This application works with any CSV dataset.
Example datasets:
* Student Performance Dataset
* Sales Dataset
* Iris Dataset
* Titanic Dataset
* Any structured CSV file

Dataset Source:
Kaggle

## Tools and Technologies
* Python
* Streamlit
* Pandas
* Plotly Express

## Methodology

### Step 1: Upload Dataset
The user uploads a CSV file through the Streamlit interface.
### Step 2: Data Preview
The application displays the first few rows of the dataset to help users verify that the correct file has been uploaded.
### Step 3: Dataset Information
The dashboard displays:
* Number of rows
* Number of columns
* Column names
### Step 4: Missing Value Analysis
Missing values are calculated for every column to help users identify incomplete data.
### Step 5: Summary Statistics
Statistical measures such as count, mean, median, minimum, maximum, and standard deviation are generated automatically.
### Step 6: Data Cleaning
Users can:
* Remove duplicate records
* Remove rows containing missing values
### Step 7: Data Filtering
Categorical columns are displayed in the sidebar, allowing users to filter the dataset dynamically.
### Step 8: Data Visualization
The dashboard generates interactive visualizations including:
* Histogram
* Box Plot
* Scatter Plot
* Bar Chart
* Pie Chart
* Correlation Matrix
### Step 9: Key Insights
Important statistical values such as maximum, minimum, average, median, and standard deviation are displayed.

## Features
* Upload any CSV file
* Interactive dashboard
* Data preview
* Dataset statistics
* Missing value analysis
* Duplicate removal
* Missing value removal
* Dynamic filtering
* Interactive visualizations
* Download filtered dataset

## Results
The dashboard successfully converts raw CSV data into meaningful visualizations and statistical summaries.
Users can quickly identify patterns, trends, missing values, and outliers while exploring their datasets interactively.

## Project Structure
```
synent-task4-csvdashboard-zubairali

│── app.py
│── dataset.csv
│── requirements.txt
│── README.md
│── screenshots
│     ├── home.png
│     ├── histogram.png
│     ├── scatterplot.png
│     └── piechart.png
```
## How to Run

1. Clone this repository.
2. Install dependencies.
```
pip install -r requirements.txt
```
3. Run the application.
```
streamlit run app.py
```
4. Upload any CSV dataset.
5. Explore the dashboard.

## Future Improvements

* Dark mode
* More chart types
* Export charts as images
* Advanced filtering
* Machine learning integration

## Author

Minahil Parvaiz
Artificial Intelligence Student
Synent Data Science Internship
