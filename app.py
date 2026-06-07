import streamlit as st

st.set_page_config(
    page_title="Crypto AI Scanner",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Crypto AI Scanner")

st.write("مرحباً بك في النسخة الأولى من التطبيق")

coin = st.text_input(
    "أدخل رمز العملة",
    value="BTC"
)

if st.button("تحليل"):

    st.success(f"تم تحليل {coin}")

    st.metric(
        label="درجة الفرصة",
        value="75/100"
    )

    st.metric(
        label="احتمالية النجاح",
        value="78%"
    )
