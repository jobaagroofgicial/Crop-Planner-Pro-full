import streamlit as st
import pandas as pd
from io import BytesIO
import data

st.set_page_config(page_title="Crop Planner Pro - Full", layout="wide")

st.title("🌾 Crop Planner Pro — Full")
st.write("Complete crop database • 10-step spray schedule • Pest management • Rotation adviser • Profit calculator")

Sidebar controls

st.sidebar.header("Settings & Tools")
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
    df_sched = pd.DataFrame(sched)
    st.dataframe(df_sched)
else:
    st.write("স্প্রে সিডিউল নেই।")

st.subheader("🔎 Pest / Disease Notes")
pests = info.get('pest_notes', [])
if pests:
    for p in pests:
        st.write(f"- {p}")

st.subheader("🔄 ক্রপ রোটেশন (৩-বা ৪ বছরের পরিকল্পনা)")
rotation = info.get('rotation', [])
if rotation:
    df_rot = pd.DataFrame(rotation)
    st.dataframe(df_rot)
else:
    st.write("রোটেশন ডেটা নেই।")

with col2:
st.header("💰 লাভ ক্যালকুলেটর (বিঘা ভিত্তিক)")
default_cost = info.get('cost', 0)
default_yield = int(info.get('yield_per_bigha', 1000))
default_price = info.get('sell_rate', 0)

cost = st.number_input("মোট খরচ (বিঘা প্রতি)", value=default_cost, step=100.0, format="%.2f")
yield_amount = st.number_input("আপনার অনুমানকৃত উৎপাদন (কেজি)", value=default_yield, step=10)
sell_price = st.number_input("বিক্রির মূল্য (টাকা/কেজি)", value=default_price, step=1.0, format="%.2f")

total_income = yield_amount * sell_price
profit = total_income - cost

st.metric("মোট আয় (টাকা)", f"{total_income:,.0f}")
st.metric("মোট লাভ/ক্ষতি (টাকা)", f"{profit:,.0f}")

if profit > 0:
    st.success("লাভ হচ্ছে ✅")
else:
    st.error("ক্ষতি হতে পারে ⚠️")

st.markdown("---")
st.header("Export / Save")
# Prepare report dataframe
report = {
    "ফসল": selected_crop,
    "বীজের পরিমাণ": info.get('seed_rate',''),
    "প্রত্যাশিত উৎপাদন": info.get('expected_yield',''),
    "মোট খরচ": cost,
    "উৎপাদন (কেজি)": yield_amount,
    "বিক্রয় মূল্য (টাকা/কেজি)": sell_price,
    "মোট আয়": total_income,
    "লাভ/ক্ষতি": profit
}
report_df = pd.DataFrame([report])

csv = report_df.to_csv(index=False).encode('utf-8')
st.download_button("CSV ডাউনলোড", data=csv, file_name=f"{selected_crop}_report.csv", mime="text/csv")

# Excel download
def to_excel_bytes(df):
    out = BytesIO()
    with pd.ExcelWriter(out, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Report")
        writer.save()
    return out.getvalue()

excel_bytes = to_excel_bytes(report_df)
st.download_button("Excel ডাউনলোড", data=excel_bytes, file_name=f"{selected_crop}_report.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

st.markdown("---")
st.caption("Crop Planner Pro — Full. ডেটাবেস বড় করে তুমি যেকোনো ফসল এখানে যোগ করতে পারবে।")
