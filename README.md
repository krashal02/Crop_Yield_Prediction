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

---

## 🚀 Project Structure

```
.
├── app.py                    # Flask backend
├── templates/
│   └── index.html            # Frontend interface
├── dtr.pkl                   # Trained Decision Tree model
├── preprocessor.pkl          # Fitted preprocessor for encoding/scaling
├── yield.ipynb               # Model training notebook
├── yield_df.csv              # Dataset used for training
└── README.md                 # Project documentation
```

---

## 💻 How to Run Locally

1. **Clone this repository:**
   ```bash
   git clone https://github.com/krashal02/Crop_Yield_Prediction.git
   cd Crop_Yield_Prediction
   ```

2. **Install dependencies:**
   ```bash
   pip install flask numpy pandas scikit-learn
   ```

3. **Ensure model files exist:**
   - `dtr.pkl` → Trained Decision Tree model  
   - `preprocessor.pkl` → Data transformation pipeline

4. **Run the Flask app:**
   ```bash
   python app.py
   ```

5. **Open the application:**
   Visit → [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌱 Example Output

After submitting the form:
> 🌾 Predicted Crop Yield: **4567.2 hg/ha**

---

## 🧩 Model Training Summary

- **Model:** DecisionTreeRegressor  
- **Input Features:** Year, Average Rainfall, Pesticides, Average Temperature, Area, Item  
- **Output:** Predicted crop yield (hg/ha)  
- **Data Preprocessing:**  One-Hot Encoding, and Scaling  
- **Evaluation Metrics:** Mean Absolute Error (MAE), R² Score  

---



## 👨‍💻 Author

**Krashal Yaduvanshi**  
💡 Full Stack Developer & Machine Learning Enthusiast  
📍 Jaipur, India  
