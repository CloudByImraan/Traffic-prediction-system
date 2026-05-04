import streamlit as st
import pandas as pd
import pickle

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("../models/model.pkl", "rb"))
scaler = pickle.load(open("../models/scaler.pkl", "rb"))
df = pd.read_csv("../data/processed/cleaned_traffic_data.csv")

# ---------------- PAGE SETUP ----------------
st.title("🚦 Traffic Prediction System")
st.markdown("Predict whether traffic will be **High or Low** using time + weather patterns.")

# ---------------- INPUT SECTION ----------------
st.markdown("## 🔧 Enter Traffic Conditions")

col1, col2 = st.columns(2)

days_map = {
    "Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,
    "Friday":4,"Saturday":5,"Sunday":6
}

months_map = {
    "January":1,"February":2,"March":3,"April":4,
    "May":5,"June":6,"July":7,"August":8,
    "September":9,"October":10,"November":11,"December":12
}

weather_options = ["Clear", "Clouds", "Rain", "Drizzle", "Mist", "Haze", "Fog", "Thunderstorm", "Snow", "Other"]

with col1:
    day = st.selectbox("Day of Week", list(days_map.keys()))
    month = st.selectbox("Month", list(months_map.keys()))
    hour = st.slider("Hour of Day", 0, 23, 8)
    clouds = st.slider("Cloud Coverage (%)", 0, 100)

with col2:
    rain = st.number_input("Rain (mm)", min_value=0.0)
    rush_hour = st.selectbox("Rush Hour?", ["No", "Yes"])
    weather = st.selectbox("Weather Condition", weather_options)

# ---------------- INPUT PROCESSING ----------------
input_dict = {
    "hour": hour,
    "day_of_week": days_map[day],
    "month": months_map[month],
    "is_weekend": 1 if days_map[day] >= 5 else 0,
    "is_rush_hour": 1 if rush_hour == "Yes" else 0,
    "clouds_all": clouds,
    "rain_1h": rain
}

# ---------------- WEATHER ENCODING ----------------
weather_cols = [col for col in scaler.feature_names_in_ if "weather_main_" in col]

for col in weather_cols:
    input_dict[col] = 1 if col == f"weather_main_{weather}" else 0

# ---------------- ALIGN FEATURES ----------------
feature_columns = list(scaler.feature_names_in_)
input_df = pd.DataFrame([input_dict])
input_df = input_df.reindex(columns=feature_columns, fill_value=0)

# ---------------- PREDICTION ----------------
if st.button("Predict Traffic"):
    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)

    st.markdown("## 🚨 Result")

    if prediction == 1:
        st.error("HIGH TRAFFIC 🚗🚗🚗")
    else:
        st.success("LOW TRAFFIC 🚗")

    st.write("Prediction Probability:", probability)

# ---------------- DASHBOARD ----------------
st.markdown("---")
st.markdown("## 📊 Traffic Insights")

# Traffic by Day
st.markdown("### Traffic by Day")
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

df["day_name"] = df["day_of_week"].map(dict(enumerate(days)))
df["day_name"] = pd.Categorical(df["day_name"], categories=days, ordered=True)

st.bar_chart(df.groupby("day_name")["traffic_level"].mean())

# Traffic by Hour
st.markdown("### Traffic by Hour")
st.line_chart(df.groupby("hour")["traffic_level"].mean())

# Weather Impact
st.markdown("### Traffic by Weather")

weather_cols_df = [col for col in df.columns if col.startswith("weather_main_")]

df["weather_main"] = df[weather_cols_df].idxmax(axis=1).str.replace("weather_main_", "")
st.bar_chart(df.groupby("weather_main")["traffic_level"].mean())

# Rain Impact
st.markdown("### Traffic vs Rain")
st.line_chart(df[["rain_1h","traffic_level"]].dropna().set_index("rain_1h"))

# Footer
st.markdown("---")
st.caption("🚦 Traffic Prediction System | Built with Logistic Regression")