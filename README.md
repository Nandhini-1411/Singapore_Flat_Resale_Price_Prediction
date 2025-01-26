# Singapore Resale Flat Price Prediction

## Problem Statement
The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts the resale prices of flats in Singapore. This predictive model will be based on historical data of resale flat transactions, and it aims to assist both potential buyers and sellers in estimating the resale value of a flat.

## Motivation
The resale flat market in Singapore is highly competitive, and it can be challenging to accurately estimate the resale value of a flat. There are many factors that can affect resale prices, such as location, flat type, floor area, and lease duration. A predictive model can help overcome these challenges by providing users with an estimated resale price based on these factors.

## Scope
This project involves several key tasks:

### 1. Data Collection and Preprocessing:
- Collect a dataset of resale flat transactions from the Singapore Housing and Development Board (HDB) for the years 1990 to present.
- Clean and preprocess the data to make it suitable for machine learning.

### 2. Feature Engineering:
- Extract relevant features, including town, flat type, storey range, floor area, flat model, and lease commence date.
- Create additional features to enhance prediction accuracy.

### 3. Model Selection and Training:
- Choose a regression model (e.g., linear regression, decision trees, or random forests).
- Train the model using a portion of the dataset.

### 4. Model Evaluation:
- Evaluate the model's performance using regression metrics like:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - R² Score

### 5. Streamlit Web Application:
- Develop a user-friendly web app using Streamlit.
- Allow users to input details of a flat (e.g., town, flat type, storey range, etc.).
- Use the trained model to predict resale prices based on user inputs.

### 6. Deployment on Render:
- Deploy the Streamlit web application on the Render platform for easy access over the internet.

### 7. Testing and Validation:
- Test the deployed application to ensure it functions correctly and provides accurate predictions.

## Deliverables
The project will deliver the following:

- A well-trained machine learning model for resale price prediction.
- A user-friendly web application (built with Streamlit).
- Deployed on the Render platform (or any cloud platform).
- Documentation and instructions for using the application.
- A project report summarizing data analysis, model development, and deployment process.

## Technologies Used
- **Python** (for model development and Streamlit app)
- **Streamlit** (for web application development)
- **scikit-learn** (for machine learning model)
- **pandas** (for data manipulation)
- **numpy** (for numerical operations)
- **Render** (for deployment)
