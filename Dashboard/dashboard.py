import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# =========================
# CONFIG
# =========================
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "all_data.csv")

st.set_page_config(
    page_title="Olist E-Commerce Dashboard",
    layout="wide",
    page_icon="📈",
)

sns.set_theme(style="whitegrid", palette="deep")

CHART_COLOR = "#1f77b4"
TEXT_COLOR = "#2f4f6f"
BORDER_COLOR = "#dbe5f1"


# =========================
# HELPER FUNCTIONS
# =========================
def create_daily_orders_df(df):
    return (
        df.set_index("order_purchase_timestamp")
        .resample("D")
        .agg(order_count=("order_id", "nunique"),
             revenue=("price", "sum"))
        .reset_index()
    )


def create_revenue_by_category(df):
    return (
        df.groupby("product_category_name")["price"]
        .sum()
        .sort_values(ascending=False)
        .head(6)
        .reset_index()
    )


def create_rfm_df(df, analysis_date):
    rfm = df.groupby("customer_id", as_index=False).agg(
        last_purchase=("order_purchase_timestamp", "max"),
        frequency=("order_id", "nunique"),
        monetary=("price", "sum"),
    )
    rfm["recency"] = (analysis_date - rfm["last_purchase"]).dt.days
    return rfm.sort_values(by=["recency", "frequency", "monetary"])


# =========================
# LOAD DATA
# =========================
df = pd.read_csv(DATA_PATH)

df["order_purchase_timestamp"] = pd.to_datetime(
    df["order_purchase_timestamp"], errors="coerce"
)

df = df.dropna(subset=["order_purchase_timestamp"]).copy()

df["order_date"] = df["order_purchase_timestamp"].dt.date
df["order_month"] = df["order_purchase_timestamp"].dt.to_period("M").astype(str)

min_date = df["order_date"].min()
max_date = df["order_date"].max()


# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.markdown("## Filter Analisis")

    start_date, end_date = st.date_input(
        "Rentang Waktu",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date],
    )

    st.markdown("---")
    st.markdown("### Tips")
    st.markdown(
        "- Geser tanggal untuk melihat tren\n"
        "- Fokus kategori revenue tinggi\n"
        "- Perhatikan biaya freight"
    )


# =========================
# FILTER DATA
# =========================
main_df = df[
    (df["order_date"] >= start_date) &
    (df["order_date"] <= end_date)
].copy()

if main_df.empty:
    st.error("Tidak ada data pada rentang ini.")
    st.stop()


# =========================
# HEADER
# =========================
st.markdown(
    f"""
    <div style='padding: 24px 0; border-bottom: 2px solid {BORDER_COLOR};'>
        <h1 style='margin: 0; color:{CHART_COLOR};'>
            Olist E-Commerce Dashboard
        </h1>
        <p style='color:{TEXT_COLOR};'>
            Dashboard analisis penjualan yang ringkas dan informatif
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================
# DATA PREP
# =========================
daily_orders_df = create_daily_orders_df(main_df)
revenue_by_cat = create_revenue_by_category(main_df)
rfm_df = create_rfm_df(main_df, pd.to_datetime(end_date))


# =========================
# KPI
# =========================
total_revenue = main_df["price"].sum()
total_orders = main_df["order_id"].nunique()
avg_price = main_df["price"].mean()
unique_categories = main_df["product_category_name"].nunique()
top_category = revenue_by_cat.iloc[0, 0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"Rp {total_revenue:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Avg Price", f"Rp {avg_price:,.0f}")
col4.metric("Kategori", f"{unique_categories}")

st.divider()


# =========================
# DAILY ORDERS
# =========================
st.subheader("📊 Daily Orders")

fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(
    daily_orders_df["order_purchase_timestamp"],
    daily_orders_df["order_count"],
    marker="o",
    color=CHART_COLOR,
)
ax.set_title("Jumlah Pesanan Harian")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
st.pyplot(fig)

st.markdown("### 📌 Penjelasan")
st.markdown("Menampilkan jumlah pesanan per hari untuk melihat tren penjualan.")

avg_orders = daily_orders_df["order_count"].mean()
max_orders = daily_orders_df["order_count"].max()
peak_date = daily_orders_df.loc[
    daily_orders_df["order_count"].idxmax(),
    "order_purchase_timestamp"
]

st.markdown("### 💡 Intisari Insight")
st.markdown(
    f"""
- Rata-rata pesanan: **{avg_orders:.0f} / hari**
- Puncak: **{peak_date.date()}**
- Tertinggi: **{max_orders} orders**
"""
)

st.divider()


# =========================
# PRODUCT PERFORMANCE
# =========================
st.subheader("📦 Product Performance")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(
        x="price",
        y="product_category_name",
        data=revenue_by_cat,
        color=CHART_COLOR,
        ax=ax,
    )
    ax.set_title("Revenue per Kategori")
    st.pyplot(fig)

with col2:
    freight_df = (
        main_df.groupby("product_category_name")["freight_value"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(
        x="freight_value",
        y="product_category_name",
        data=freight_df,
        color=CHART_COLOR,
        ax=ax,
    )
    ax.set_title("Freight per Kategori")
    st.pyplot(fig)

st.markdown("### 📌 Penjelasan")
st.markdown("Membandingkan revenue dan biaya pengiriman per kategori.")

top_rev = revenue_by_cat.iloc[0]
top_freight = freight_df.iloc[0]

st.markdown("### 💡 Intisari Insight")
st.markdown(
    f"""
- Revenue tertinggi: **{top_rev['product_category_name']}**
- Nilai: **Rp {top_rev['price']:,.0f}**
- Freight tertinggi: **{top_freight['product_category_name']}**
"""
)

st.divider()


# =========================
# RFM ANALYSIS (FIXED)
# =========================
st.subheader("👤 RFM Analysis")

col1, col2, col3 = st.columns(3)
col1.metric("Recency", f"{rfm_df['recency'].mean():.1f} hari")
col2.metric("Frequency", f"{rfm_df['frequency'].mean():.2f}")
col3.metric("Monetary", f"Rp {rfm_df['monetary'].mean():,.0f}")

st.divider()

# Recency
st.markdown("### 📉 Recency")

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(
    x="recency",
    y="customer_id",
    data=rfm_df.sort_values("recency").head(5),
    color=CHART_COLOR,
    ax=ax,
)
st.pyplot(fig)

# Frequency
st.markdown("### 🔁 Frequency")

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(
    x="frequency",
    y="customer_id",
    data=rfm_df.sort_values("frequency", ascending=False).head(5),
    color=CHART_COLOR,
    ax=ax,
)
st.pyplot(fig)

# Monetary
st.markdown("### 💰 Monetary")

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(
    x="monetary",
    y="customer_id",
    data=rfm_df.sort_values("monetary", ascending=False).head(5),
    color=CHART_COLOR,
    ax=ax,
)
st.pyplot(fig)

st.markdown("### 💡 Intisari Insight")
best_customer = rfm_df.sort_values(
    ["frequency", "monetary"], ascending=False
).iloc[0]

st.markdown(
    f"""
- Pelanggan terbaik: **{best_customer['customer_id']}**
- Fokus retensi pelanggan aktif
"""
)

st.divider()


# =========================
# FINAL INSIGHT
# =========================
st.subheader("🧠 Kesimpulan Akhir")

st.markdown(
    f"""
- Kategori utama: **{top_category}**
- Total revenue: **Rp {total_revenue:,.0f}**
- Terdapat fluktuasi penjualan harian
- Freight tinggi perlu evaluasi

👉 Rekomendasi:
- Fokus kategori profit tinggi
- Optimasi logistik
- Retensi pelanggan loyal
"""
)

st.caption("Copyright (c) Owi 2026")