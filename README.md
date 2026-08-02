# 📊 E-Commerce Data Analysis & Dashboard (Olist)

This project is an **end-to-end data analysis** of the **Olist E-Commerce Dataset** to uncover valuable insights into business performance, customer behavior, and market distribution. The analysis covers the entire data analytics workflow, including **Data Wrangling, Exploratory Data Analysis (EDA), and the development of an interactive dashboard using Streamlit**.

---

## 📌 Business Questions

1. How did sales performance and revenue trends evolve throughout **2017–2018**?
2. Which product categories were the best-selling, and which had the lowest performance?
3. What are the geographic characteristics of Olist's customers?

---

## 🚀 Features

* 📈 Interactive dashboard built with **Streamlit**
* 📊 Daily sales trend visualization
* 📦 Product category performance analysis
* 👤 **RFM (Recency, Frequency, Monetary)** customer analysis
* 🧠 Automated insights and business interpretation

---

## 🛠️ Environment Setup

### Using Anaconda

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Using Pip / Terminal

```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

## 📂 Project Structure

```text
.
├── dashboard/
│   ├── dashboard.py
│   └── all_data.csv
│
├── data/
│   └── (raw dataset)
│
├── proyek_analisis_data.ipynb
├── requirements.txt
└── README.md
```

---

## 🧠 Key Insights

* Sales exhibited fluctuating trends with several noticeable peak periods.
* A small number of product categories contributed the majority of total revenue.
* High freight costs in certain categories may negatively impact overall profitability.
* Customers with high **Frequency** and **Monetary** values represent valuable loyal customer segments.

---

## 📊 Dataset

This project uses the **Olist Brazilian E-Commerce Public Dataset**, which contains information on orders, customers, products, payments, sellers, and customer reviews from Olist's marketplace.

**Dataset Source:**
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit
* Jupyter Notebook

---

## 📜 License

This project is intended for **educational purposes** and **portfolio development**.
