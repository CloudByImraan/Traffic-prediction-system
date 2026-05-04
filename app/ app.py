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
st.markdown("## 🔧 Input Features")

col1, col2 = st.columns(2)

with col1:
    temp = st.number_input("Temperature (°C)", value=25.0)
    rain_1h = st.number_input("Rain (mm in last 1 hour)", value=0.0)
    clouds_all = st.slider("Cloud Coverage (%)", 0, 100, 50)

with col2:
    day = st.selectbox("Day of Week", list(days_map.keys()))
    month = st.selectbox("Month", list(months_map.keys()))
    hour = st.slider("Hour of Day (0–23)", 0, 23, 12)

weather = st.selectbox("Weather Condition", [
    "Clear","Clouds","Rain","Fog","Mist","Other"
])

is_rush_hour = 1 if (7 <= hour <= 9 or 16 <= hour <= 18) else 0

# ---------------- INPUT PROCESSING ----------------
temp_kelvin = temp + 273.15

input_dict = {
    "temp": temp_kelvin,
    "rain_1h": rain_1h,
    "snow_1h": 0,  # FIXED (not relevant)
    "clouds_all": clouds_all,
    "hour": hour,
    "day_of_week": days_map[day],
    "month": months_map[month],
    "is_rush_hour": is_rush_hour,
    "is_weekend": 1 if days_map[day] >= 5 else 0,
    "year": 2024
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
st.write("Confidence (Low vs High):", prob)

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