# 🚦 Traffic Prediction System using Machine Learning

## 📌 Project Overview

This project is a Machine Learning-based Traffic Prediction System that predicts whether traffic conditions will be **HIGH or LOW** based on weather and time-related features. The system uses a Logistic Regression model and is deployed using Streamlit for real-time predictions.

Traffic congestion is influenced by multiple factors such as weather conditions, time of day, and weekly patterns. This project aims to capture these patterns and provide a simple prediction system for better decision-making.

---

## 🎯 Objectives

- Build a classification model to predict traffic levels
- Use weather and time-based features for prediction
- Deploy a real-time interactive web app using Streamlit
- Provide insights into traffic behavior patterns

---

## 🧠 Machine Learning Model

- Algorithm: Logistic Regression
- Task: Binary Classification (High / Low Traffic)
- Preprocessing: StandardScaler normalization
- Encoding: One-hot encoding for weather conditions

---

## 📊 Dataset Features

- Temperature
- Rain (mm)
- Cloud Coverage
- Hour of Day
- Day of Week
- Month
- Weather Type
- Rush Hour Indicator
- Weekend Indicator

---

## 🏗️ Project Structure
traffic-prediction-ml/
│
├── app/
│ └── app.py
│
├── data/
│ ├── raw/
│ │ └── traffic_data.csv
│ └── processed/
│ └── cleaned_traffic_data.csv
│
├── models/
│ ├── model.pkl
│ └── scaler.pkl
│
├── notebooks/
│ ├── data_cleaning.ipynb
│ ├── data_exploration.ipynb
│ └── model_training.ipynb
│
├── requirements.txt
└── README.md

---

## 📈 Model Performance

- Accuracy: ~66%
- Output: Binary Classification
  - 0 → Low Traffic
  - 1 → High Traffic

---

## 🚀 How to Run the Project (VS Code)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/traffic-prediction-ml.git
2. Install dependencies
pip install -r requirements.txt
3. Run the Streamlit app
streamlit run app/app.py

📈 Key Insights
Traffic is highly influenced by time (hour & day)
Rush hours significantly increase congestion
Weather has a moderate impact on traffic patterns


⚠️ Limitations
Model accuracy is moderate (baseline level)
Dataset may not reflect local (Nigeria) traffic patterns fully
Some features (e.g., snow) are less relevant in certain regions


🔮 Future Improvements
Use more advanced models (Random Forest, XGBoost)
Incorporate real-time traffic data
Improve feature engineering
Deploy as a full web application

👨‍💻 Author
Imraan Muhammad Sani



📌 Conclusion
This project demonstrates how machine learning can be applied to real-world problems like traffic prediction. It serves as a strong foundation for building more advanced intelligent transportation systems.