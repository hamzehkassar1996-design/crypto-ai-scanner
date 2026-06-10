import streamlit as st
import pandas as pd
import ccxt

st.set_page_config(
    page_title="Crypto AI Scanner",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Crypto AI Scanner")
st.subheader("CoinEx Market Scanner")

exchange = ccxt.coinex({
    "enableRateLimit": True
})

symbol = st.text_input(
    "أدخل الزوج",
    value="BTC/USDT"
)

timeframe = st.selectbox(
    "الفريم",
    ["1h", "4h", "1d"],
    index=1
)

if st.button("تحميل البيانات"):

    try:

        candles = exchange.fetch_ohlcv(
            symbol,
            timeframe=timeframe,
            limit=100
        )

        df = pd.DataFrame(
            candles,
            columns=[
                "time",
                "open",
                "high",
                "low",
                "close",
                "volume"
            ]
        )

        st.success("تم تحميل البيانات بنجاح")

        st.dataframe(df.tail(20))

        last_price = df["close"].iloc[-1]

        st.metric(
            "آخر سعر",
            round(last_price, 6)
        )

    except Exception as e:

        st.error(str(e))
