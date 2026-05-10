# 🚦 Traffic Prediction System [(CLASSIFICATION) logistic regression]

A machine learning-based web application that predicts traffic conditions (**HIGH or LOW**) using weather and time-related features. The system is deployed using Streamlit for real-time interaction.

---

## 📌 Overview

Traffic congestion is influenced by multiple factors such as weather, time of day, and weekly patterns.

This project builds a classification model to analyze these factors and predict traffic levels, helping users make better planning decisions.

---

## 🚀 Features

* 📊 Predict traffic conditions (High / Low)
* 🤖 Machine Learning model (Logistic Regression)
* 🌐 Interactive web interface (Streamlit)
* ⚡ Real-time predictions based on user input
* 📈 Data preprocessing and feature engineering

---

## 🧠 Machine Learning Model

* Algorithm: Logistic Regression
* Task: Binary Classification
* Output:

  * `0` → Low Traffic
  * `1` → High Traffic

### Preprocessing:

* StandardScaler (Normalization)
* One-hot encoding (Weather categories)

---

## 📊 Dataset Features

* Temperature
* Rain (mm)
* Cloud Coverage
* Hour of Day
* Day of Week
* Month
* Weather Type
* Rush Hour Indicator
* Weekend Indicator

---

## 🖥️ UI Layout (Simplified View)

```text
+--------------------------------------+
|   Traffic Prediction System          |
+--------------------------------------+

[ Temperature        ______ ]
[ Rain (mm)          ______ ]
[ Cloud Coverage     ______ ]
[ Hour               ______ ]
[ Day of Week        ______ ]
[ Month              ______ ]
[ Weather Type       ______ ]

[ Rush Hour (Yes/No) ]
[ Weekend (Yes/No)   ]

        [ Predict Traffic ]

----------------------------------------
| Result: 🚦 HIGH TRAFFIC              |
----------------------------------------
```

---

## 📂 Project Structure

```bash
traffic-prediction-ml/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── traffic_data.csv
│   └── processed/
│       └── cleaned_traffic_data.csv
│
├── models/
│   ├── model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── data_exploration.ipynb
│   └── model_training.ipynb
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

```bash
# Clone repository
git clone https://github.com/your-username/traffic-prediction-ml.git

# Navigate into project folder
cd traffic-prediction-ml

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app/app.py
```

---

## 📈 Model Performance

* Accuracy: ~66%
* Classification Type: Binary

---

## 📊 Key Insights

* Traffic strongly depends on time (hour & day)
* Rush hours significantly increase congestion
* Weather has moderate influence on traffic

---

## ⚠️ Limitations

* Moderate accuracy (baseline model)
* Dataset may not reflect local traffic patterns
* Some features (e.g., snow) may not be region-relevant

---

## 🎓 What You Will Learn

* Machine learning classification workflow
* Feature engineering techniques
* Model deployment using Streamlit
* Data preprocessing and scaling
* Building real-world prediction systems

---

## 🚧 Project Status

✅ Completed (ML + Deployment Project) [beginner level]

---

## 🔮 Future Improvements

* Use advanced models (Random Forest, XGBoost)
* Integrate real-time traffic APIs
* Improve feature engineering
* Deploy as a full-scale web application

---

## 👨‍💻 Author

Imraan Muhammad Sani

---

## 📌 Final Note

This project demonstrates how machine learning can be applied to real-world problems like traffic prediction and serves as a foundation for intelligent transportation systems.

💡 This project demonstrates my current approach and can be further enhanced with more advanced features and optimizations.
📌 Built as part of my early learning phase in machine learning and application development.
---
