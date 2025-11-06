# Week 1: EV Price Prediction Using Machine Learning # ⚡ EV Price Prediction Using Machine Learning

Based on characteristics like battery capacity, range, charging power, and more, this project forecasts the **resale price of Electric Vehicles (EVs)**.  
It analyses EV datasets and predicts pricing trends by fusing **Generative AI concepts** with **Machine Learning**.

---

## 🚀 Project Summary

Understanding electric vehicle data, cleaning and preprocessing the data, and training a regression model to forecast EV prices are the objectives of this project.
Utilise statistical metrics to assess the model's performance.
Compare projected and actual EV prices.
To deploy the trained model (Streamlit web app), save it.

---

## Technology 

| Tool | Objective | Python | Programming language || Pandas, NumPy | Data analysis and preprocessing || Scikit-Learn | Training machine learning models || Matplotlib | Data visualisation || Joblib | Saving and loading machine learning models || Jupyter Notebook | Development environment |

## Dataset Details

File: `electric_vehicle_analytics.csv`  
An electric vehicle with the following essential characteristics is represented by each record:

| Feature | Description | |----------|--------------| `Year` | Model manufacturing year || `Battery_Capacity_kWh` | Battery size (kWh) || `Range_km` | Estimated driving range (km) || `Power_kW` | Motor power (kW) || `Torque_Nm` | Torque (Nm) || `Charging_Time_hr` | Time to fully charge || `Maintenance_Cost_USD` | Annual maintenance cost || `Resale_Value_USD` | Target variable (price) |

---

## ⚙️ Model Construction Procedures

1. Preprocessing of Data
   Address missing values and feature selection. If applicable, translate categorical data into numerical form.

2. "Model Training" - Utilised Scikit-Learn's Linear Regression - Divided the dataset into 80% training and 20% testing

3. Evaluation Metrics" - Mean Absolute Error (MAE): 1508.06 - *Root Mean Squared Error (RMSE): 1736.39 - R2 Score:  0. 90 - High accuracy

A scatter plot comparing actual and predicted EV prices reveals a strong linear relationship.

---
## 🌐 Week 2 – Streamlit Web Application

In Week 2, a web interface was built using **Streamlit** to predict the resale value of electric vehicles based on user input features.  
Users can enter EV details such as year, battery capacity, range, and maintenance cost to get a predicted resale value in real time.

**Improvements made:**
- Integrated trained ML model with Streamlit frontend  
- Added clean and responsive UI design  
- Tested model predictions for accuracy and usability  
- Verified compatibility with Python 3.13 environment  

