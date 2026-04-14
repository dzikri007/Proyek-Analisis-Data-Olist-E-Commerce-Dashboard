# Olist E-Commerce Data Analysis Dashboard ✨

## Deskripsi
Proyek ini merupakan analisis data dari dataset E-Commerce Olist untuk memenuhi kualifikasi submission pada kursus "Belajar Analisis Data dengan Python" di Dicoding. Fokus utama analisis ini adalah melihat performa penjualan di tahun 2017, tren metode pembayaran, serta persebaran geografis pelanggan.

## Struktur Proyek
- `dashboard/`: Berisi file dashboard utama (`dashboard.py`) dan dataset yang telah dibersihkan (`all_data.csv`).
- `data/`: Direktori yang berisi dataset mentah dalam format CSV.
- `notebook.ipynb`: File Jupyter Notebook yang berisi proses Data Wrangling, EDA, hingga Visualisasi.
- `requirements.txt`: Daftar library yang dibutuhkan untuk menjalankan proyek.
- `README.md`: Dokumentasi proyek.

## Pertanyaan Bisnis
1. Apa saja kategori produk dengan pendapatan (revenue) tertinggi di tahun 2017?
2. Apa metode pembayaran yang paling sering digunakan oleh pelanggan selama 2017-2018?
3. Negara bagian mana yang memiliki jumlah pelanggan unik terbanyak di tahun 2017?

## Cara Menjalankan Dashboard

### 1. Persiapan Environment
Pastikan Anda memiliki Python versi 3.9 atau lebih baru. Disarankan untuk menggunakan virtual environment:
```bash
# Untuk Windows
python -m venv venv
.\venv\Scripts\activate

# Untuk Mac/Linux
python3 -m venv venv
source venv/bin/activate

Live Dashboard URL
Proyek ini telah dideploy secara publik dan dapat diakses melalui:
👉 https://owi-olist-e-commerce-dashboard.streamlit.app/
