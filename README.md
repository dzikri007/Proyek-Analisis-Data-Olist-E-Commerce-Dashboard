# 📊 E-Commerce Data Analysis & Dashboard (Olist)

Proyek ini merupakan analisis end-to-end terhadap dataset **Olist E-Commerce** untuk menggali insight terkait performa bisnis, perilaku pelanggan, dan distribusi pasar.
Analisis dilakukan mulai dari **Data Wrangling, Exploratory Data Analysis (EDA), hingga pembuatan dashboard interaktif menggunakan Streamlit**.

---

## 📌 Business Questions

1. Bagaimana tren performa penjualan dan pendapatan selama tahun 2017–2018?
2. Produk apa yang paling mendominasi pasar (best seller) dan mana yang memiliki performa terendah?
3. Bagaimana profil demografi pelanggan berdasarkan wilayah geografis?

---

## 🚀 Features

* 📈 Interactive dashboard menggunakan Streamlit
* 📊 Visualisasi tren penjualan harian
* 📦 Analisis performa kategori produk
* 👤 RFM Analysis (Recency, Frequency, Monetary)
* 🧠 Insight otomatis & interpretasi data

---

## 🛠️ Setup Environment

### Anaconda

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Terminal / Pip

```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

## ▶️ Run Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

## 📂 Project Structure

```
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

* Penjualan menunjukkan pola fluktuatif dengan beberapa peak tertentu
* Kategori produk tertentu mendominasi revenue
* Biaya freight tinggi pada beberapa kategori berpotensi menekan profit
* Pelanggan dengan frequency dan monetary tinggi berpotensi menjadi pelanggan loyal

---

## 📜 License

Project ini digunakan untuk tujuan pembelajaran dan pengembangan portfolio.
