# week1
EV-Price-Prediction-Using-ML
# ⚡ Electric Vehicle Price Prediction using Machine Learning

This project predicts the **resale price of Electric Vehicles (EVs)** based on features such as battery capacity, range, charging power, and more.  
It combines **Machine Learning** with **Generative AI concepts** to analyze EV datasets and forecast pricing trends.

---

## 🚀 Project Overview

The aim of this project is to:
- Understand electric vehicle data
- Clean and preprocess the dataset
- Train a regression model to predict EV prices
- Evaluate the model performance using statistical metrics
- Visualize actual vs predicted EV prices
- Save the trained model for deployment (Streamlit web app)

---

## 🧠 Technologies Used

| Tool | Purpose |
|------|----------|
| Python | Programming language |
| Pandas, NumPy | Data analysis and preprocessing |
| Scikit-Learn | Machine learning model training |
| Matplotlib | Data visualization |
| Joblib | Saving and loading ML models |
| Jupyter Notebook | Development environment |

---

## 📊 Dataset Information

**File:** `electric_vehicle_analytics.csv`  
Each record represents an electric vehicle with the following key attributes:

| Feature | Description |
|----------|--------------|
| `Year` | Model manufacturing year |
| `Battery_Capacity_kWh` | Battery size (kWh) |
| `Range_km` | Estimated driving range (km) |
| `Power_kW` | Motor power (kW) |
| `Torque_Nm` | Torque (Nm) |
| `Charging_Time_hr` | Time to fully charge |
| `Maintenance_Cost_USD` | Annual maintenance cost |
| `Resale_Value_USD` | Target variable (price) |

---

## ⚙️ Model Building Steps

1. **Data Preprocessing**
   - Handle missing values and feature selection
   - Convert categorical data into numerical form (if any)

2. **Model Training**
   - Used **Linear Regression** from Scikit-Learn
   - Split dataset into 80% training and 20% testing

3. **Evaluation Metrics**
   - **MAE (Mean Absolute Error):** 1508.06  
   - **RMSE (Root Mean Squared Error):** 1736.39  
   - **R² Score:** 0.90 → indicates high accuracy

4. **Visualization**
   - Scatter plot comparing Actual vs Predicted EV Prices shows a strong linear relationship.

---

## 💾 Saved Model

The trained model is saved using:
