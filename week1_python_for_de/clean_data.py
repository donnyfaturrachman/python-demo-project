# Day 4 – Data Cleaning dengan Pandas
# Operasi DataFrame
# - Gunakan pandas untuk manipulasi data.
# - Coba fungsi: fillna(), drop_duplicates(), astype().
# - Bersihkan kolom yang null atau salah tipe data.
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("/home/master/github/python-demo-project/week1_python_for_de/data/customers_raws.csv")

print("=== Sebelum Cleaning ===")
print(df.info())
print(df.head(), "\n")

# Hilangkan spasi berlebih
df['customer_name'] = df['customer_name'].astype(str).str.strip()

# Email lowercase
df['email'] = df['email'].astype(str).str.lower()

# Format kota
df['city'] = df['city'].astype(str).str.strip().str.title()

# Format tanggal
df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')

# 🔹 Ubah kolom age ke numerik
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Hitung median age
median_age = df['age'].median(skipna=True)

# Isi missing value dengan median
df['age'] = df['age'].fillna(median_age)

# Hapus duplikat berdasarkan email
df = df.drop_duplicates(subset=['email'], keep='first')

# Hapus email yang tidak valid
df = df[df['email'].str.contains('@', na=False)]

print(df.info())
print(df.head())

df.to_csv("/home/master/github/python-demo-project/week1_python_for_de/data/customers_clean.csv", index=False)
print("\n✅ Data bersih tersimpan ke 'data/customers_clean.csv'")
