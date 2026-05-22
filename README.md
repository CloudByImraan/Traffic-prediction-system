# 🚦 Traffic Prediction System

A Machine Learning-based traffic monitoring and prediction system that predicts traffic conditions (**HIGH or LOW**) using weather and time-related features.

The project combines Machine Learning, data preprocessing, feature engineering, and a real-time Streamlit web application to simulate intelligent traffic prediction systems.

---

##  Project Status

⚠️ **Project Currently In Progress**

This project represents an early-stage implementation of a traffic prediction and intelligent transportation monitoring system.

💡 The current version focuses on traditional Machine Learning using Logistic Regression and can be expanded with more advanced predictive models and real-time traffic integrations.

 Current implementation focuses mainly on weather-based and time-based traffic prediction using classification techniques.

---

##  Project Overview

Traffic congestion is influenced by several factors such as:

* Weather conditions
* Time of day
* Rush hours
* Weekly traffic patterns
* Seasonal changes

This project was developed to build an intelligent traffic prediction system capable of analyzing these factors and predicting whether traffic conditions are likely to be:

* HIGH Traffic
* LOW Traffic

The system combines:

* Machine Learning
* Traffic Data Analysis
* Feature Engineering
* Data Preprocessing
* Classification Algorithms
* Real-Time Prediction Interface

The application allows users to input traffic-related conditions and receive instant traffic predictions through an interactive Streamlit web interface.

---

## 🌍 Main Purpose of the Project

The major purpose of this project is to demonstrate how Machine Learning can be applied to transportation systems and smart traffic management.

This type of system can be used in:

* Smart transportation systems
* Traffic monitoring centers
* Smart city infrastructure
* Navigation and route planning systems
* Intelligent transportation systems (ITS)

The project demonstrates how AI and Machine Learning can assist in predicting traffic conditions and improving transportation planning.

---

##  Current Objectives (Current Development Focus)

This project is still evolving.
The following are the major components currently implemented in this version of the system:

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Feature engineering
* Traffic classification modeling
* Logistic Regression implementation
* Real-time traffic prediction
* Streamlit web application deployment

📌 These represent the current development focus of the project and form the foundation for future improvements.

---

##  Tech Stack

| Technology          | Description                      | Contribution to Project                                                              |
| ------------------- | -------------------------------- | ------------------------------------------------------------------------------------ |
| Python              | High-level programming language  | Used as the core programming language for implementing the Machine Learning workflow |
| Pandas              | Data analysis library            | Used for dataset loading, cleaning, and manipulation                                 |
| NumPy               | Numerical computing library      | Used for numerical operations and array handling                                     |
| Matplotlib          | Data visualization library       | Used for plotting graphs and visual analysis                                         |
| Scikit-learn        | Machine Learning library         | Used for preprocessing, model training, scaling, and evaluation                      |
| Logistic Regression | Classification algorithm         | Used for predicting traffic conditions (HIGH/LOW)                                    |
| Streamlit           | Web application framework        | Used for building the interactive prediction interface                               |
| Jupyter Notebook    | Interactive notebook environment | Used for experimentation, EDA, preprocessing, and model development                  |
| Pickle              | Serialization library            | Used for saving trained models and preprocessing objects                             |

---

## 🖥️ System Workflow

```text
                ┌─────────────────────┐
                │ Traffic Dataset     │
                └─────────┬───────────┘
                          ↓
                ┌─────────────────────┐
                │ Data Cleaning       │
                └─────────┬───────────┘
                          ↓
                ┌─────────────────────┐
                │ Exploratory Data    │
                │ Analysis (EDA)      │
                └─────────┬───────────┘
                          ↓
                ┌─────────────────────┐
                │ Feature Engineering │
                └─────────┬───────────┘
                          ↓
                ┌─────────────────────┐
                │ Data Preprocessing  │
                └─────────┬───────────┘
                          ↓
                ┌─────────────────────┐
                │ Model Training      │
                │ Logistic Regression │
                └─────────┬───────────┘
                          ↓
                ┌─────────────────────┐
                │ Model Evaluation    │
                └─────────┬───────────┘
                          ↓
                ┌─────────────────────┐
                │ Streamlit Web App   │
                └─────────┬───────────┘
                          ↓
                ┌─────────────────────┐
                │ Real-Time Traffic   │
                │ Prediction          │
                └─────────────────────┘
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

## 📁 Folder Explanation

| Folder/File              | Purpose                                            |
| ------------------------ | -------------------------------------------------- |
| app/                     | Contains the Streamlit web application             |
| app.py                   | Handles UI interaction and prediction logic        |
| data/raw/                | Stores original raw traffic dataset                |
| traffic_data.csv         | Original dataset used for training                 |
| data/processed/          | Stores cleaned and processed dataset               |
| cleaned_traffic_data.csv | Preprocessed dataset used for modeling             |
| models/                  | Stores trained ML models and preprocessing objects |
| model.pkl                | Saved Logistic Regression model                    |
| scaler.pkl               | Saved StandardScaler object                        |
| notebooks/               | Contains notebooks used during development         |
| data_cleaning.ipynb      | Handles data cleaning and preprocessing            |
| data_exploration.ipynb   | Performs exploratory data analysis                 |
| model_training.ipynb     | Handles model training and evaluation              |
| requirements.txt         | Contains required project libraries                |
| README.md                | Project documentation                              |

---

## ⚙️ Setup & Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/traffic-prediction-ml.git
```

---

## 2️⃣ Navigate Into Project Folder

```bash
cd traffic-prediction-ml
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

```bash
venv\Scripts\activate
```

---

## 📦 Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 📓 Launch Jupyter Notebook (Optional)

```bash
jupyter notebook
```

---

## ▶️ How to Run the Project

## Run Streamlit Application

```bash
streamlit run app/app.py
```

After launching:

* Open the local Streamlit URL
* Input traffic-related values
* Click prediction button
* System predicts traffic condition in real time

---

## 📊 Dataset Features

The model uses the following features for prediction:

| Feature             | Description                   |
| ------------------- | ----------------------------- |
| Temperature         | Atmospheric temperature       |
| Rain (mm)           | Rainfall measurement          |
| Cloud Coverage      | Cloud intensity level         |
| Hour of Day         | Current hour                  |
| Day of Week         | Day index                     |
| Month               | Current month                 |
| Weather Type        | Weather category              |
| Rush Hour Indicator | Indicates rush-hour condition |
| Weekend Indicator   | Indicates weekend condition   |

---

## 🧠 Machine Learning Model

## Classification Algorithm

* Logistic Regression
* Binary Classification

---

## Prediction Output

| Output | Meaning      |
| ------ | ------------ |
| 0      | LOW Traffic  |
| 1      | HIGH Traffic |

---

## ⚙️ Data Preprocessing

The following preprocessing techniques were implemented:

* Data cleaning
* Feature engineering
* Standardization using StandardScaler
* One-hot encoding for categorical variables

These preprocessing steps improve model performance and prediction consistency.

---

## 📈 Model Performance

| Metric              | Performance           |
| ------------------- | --------------------- |
| Accuracy            | ~66%                  |
| Classification Type | Binary Classification |

---

## 📊 Key Insights

The project revealed several important traffic behavior patterns:

* Traffic strongly depends on hour and day
* Rush hours significantly increase congestion
* Weather conditions moderately affect traffic flow
* Weekends often show different traffic behavior

---

## 📸 Visual Results

## Streamlit User Interface

<img width="1600" height="899" alt="traffic prediction dashboard" src="https://github.com/user-attachments/assets/4a3bcade-cec0-4714-9cd9-314e6032f94a" />


Brief Description:

* Shows interactive traffic prediction interface
* Users input traffic-related conditions
* System generates real-time predictions

---

## ✅ Features

* Real-time traffic prediction
* Machine Learning classification
* Feature engineering
* Streamlit web interface
* Data preprocessing pipeline
* Interactive user input system
* Logistic Regression implementation

---

## ⚠️ Current Limitations

Although functional, the system still has some limitations:

* Moderate prediction accuracy
* Dataset may not reflect local traffic behavior
* Limited dataset size
* Some weather conditions may not be region-relevant
* Uses only traditional Machine Learning methods

---

## 🚀 Possible Improvements

Future versions may include:

* Random Forest implementation
* XGBoost integration
* Real-time traffic API integration
* Deep Learning traffic prediction
* Live map visualization
* Cloud deployment
* Mobile application integration
* Smart city dashboard integration

---

## 🌍 Real-World Applications

Possible deployment areas include:

* Smart transportation systems
* Navigation systems
* Smart city infrastructure
* Traffic control centers
* Intelligent transportation systems
* Logistics and route optimization systems

---

## 🖥️ Project Type

## Machine Learning-Based Traffic Monitoring & Prediction System

The project combines:

* Machine Learning classification
* Data preprocessing
* Real-time prediction systems
* Interactive web deployment
* Intelligent transportation analytics

---

## 📈 Future Deployment Possibilities

| Deployment Type        | Description                      |
| ---------------------- | -------------------------------- |
| Web Application        | Browser-based traffic prediction |
| Smart City Dashboard   | Urban traffic monitoring         |
| Mobile Application     | Smartphone traffic assistance    |
| Cloud-Based System     | Centralized traffic analytics    |
| Navigation Integration | Route optimization systems       |

---

## 📚 Learning Context

This project was developed as part of a practical learning journey involving:

* Machine Learning workflows
* Classification algorithms
* Data preprocessing
* Feature engineering
* Streamlit deployment
* Real-world predictive systems

---

## 🙏 Acknowledgement

This project was developed with the support and mentorship of program facilitators who contributed guidance throughout the learning and development process.

We sincerely appreciate the mentorship, technical guidance, and learning support provided during the development of this project.

---

## 👨‍🏫 Program Facilitators

| Role                   | Name                    | LinkedIn                                                                                     |
| ---------------------- | ----------------------- | -------------------------------------------------------------------------------------------- |
| Leading Facilitator    | Abdulwahab Yisau (OWAD) | [Abdulwahab Yisau LinkedIn](https://linkedin.com/in/abdulwahab-yisau?utm_source=chatgpt.com) |
| Supporting Facilitator | Ogechi (N.) Ezedozie    | [Ogechi Ezedozie LinkedIn](https://linkedin.com/in/ogechi-ezedozie?utm_source=chatgpt.com)   |

---

## 👨‍💻 Contributors

* [Imraan Muhammad Sani (CloudByImraan) LinkedIn](https://linkedin.com/in/imraan-muhammad-sani-583625304?utm_source=chatgpt.com)
* [Akinola Hephzibah GitHub](https://github.com/hephzibah885?utm_source=chatgpt.com)

---

## 📄 License

This project is intended for educational, research, and learning purposes.
