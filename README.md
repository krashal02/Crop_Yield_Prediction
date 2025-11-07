# 🌾 Crop Yield Prediction Web Application

This project is a **Flask-based Machine Learning Web Application** that predicts **crop yield (hg/ha)** based on environmental and agricultural factors such as rainfall, temperature, pesticide usage, year, and region.  
It helps farmers, researchers, and policymakers understand and estimate potential yield based on given input conditions.

---

## 🧠 Project Overview

The system uses a **Decision Tree Regression Model** trained on crop yield data to predict the expected yield per hectare.  
Users can input the following features via a web form:

| Feature | Description |
|----------|-------------|
| **Year** | Year between 1990–2014 |
| **Average Rainfall (mm)** | Annual average rainfall in millimeters |
| **Pesticides (tonnes)** | Quantity of pesticides used |
| **Average Temperature (°C)** | Mean annual temperature |
| **Area** | Country or region name |
| **Item** | Crop name (e.g., Rice, Wheat, Maize) |

The app processes these inputs through a **trained preprocessor** and **Decision Tree Regressor model** to generate a prediction.

---

## ⚙️ Tech Stack

- **Frontend:** HTML, TailwindCSS  
- **Backend:** Flask (Python)  
- **Machine Learning:** Scikit-learn  
- **Libraries:** Numpy, Pandas, Pickle  


