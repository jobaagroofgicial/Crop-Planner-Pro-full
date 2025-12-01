import streamlit as st
import pandas as pd
from io import BytesIO
import data

st.set_page_config(page_title="Crop Planner Pro - Full", layout="wide")

st.title("🌾 Crop Planner Pro — Full")
st.write("Complete crop database • 10-step spray schedule • Pest management • Rotation adviser • Profit calculator")

Sidebar controls

search = st.sidebar.text_input("সার্চ ফসল (নাম লিখে এন্টার করো):").strip()
selected_crop = None

crop_list = sorted(list(data.crop_data.keys()))

if search:
matches = [c for c in crop_list if search.lower() in c.lower()]
else:
matches = crop_list

selected_crop = st.sidebar.selectbox("ফসল নির্বাচন করো:", matches)

Main display

info = data.crop_data[selected_crop]

col1, col2 = st.columns([2,1])

with col1:
st.header(f"📌 {selected_crop} — পূর্ণ গাইড")
st.subheader("🔹 বীজ ও উৎপাদন তথ্য")
st.write(f"বীজের পরিমাণ: {info.get('seed_rate','-')}")
st.write(f"প্রত্যাশিত উৎপাদন (বিঘা প্রতি): {info.get('expected_yield','-')}")
st.write(f"ডিফল্ট বিক্রয় মূল্য (টাকা/কেজি): {info.get('sell_rate','-')}")

st.subheader("🌱 সার প্রয়োগ বিবরণ")
fert = info.get('fertilizer', {})
if fert:
    for k, v in fert.items():
        st.write(f"- **{k}:** {v}")

st.subheader("🐛 10-স্টেপ স্প্রে সিডিউল (দিন ও পদক্ষেপ)")
sched = info.get('spray_schedule', [])
if sched:
    df_sched = pd.Data
