# Day 5 – Mini Project: Simple ETL CSV → Clean CSV
# Simulasi ETL sederhana
# - Extract: Baca sales_raw.csv.
# - Transform: Bersihkan kolom kosong & ubah tipe data.
# - Load: Simpan ke sales_clean.csv.
# - Tambahkan logging (print tahap proses).

import pandas as pd

# === E: Extract ===
print("📥 Extracting data...")

sales = pd.read_csv("/home/master/github/python-demo-project/week1_python_for_de/data/sales_raw_etl.csv")
customers = pd.read_csv("/home/master/github/python-demo-project/week1_python_for_de/data/customers_clean.csv")

print(f"Sales shape: {sales.shape}")
print(f"Customers shape: {customers.shape}\n")

# === T: Transform ===
print("🧹 Transforming data...")

# 1. Perbaiki format tanggal
# 1. Konversi tanggal dengan pembersihan fleksibel
def clean_date(x):
    try:
        # parse otomatis format campuran
        return pd.to_datetime(x, errors='coerce', dayfirst=False)
    except Exception:
        return pd.NaT

sales["order_date"] = sales["order_date"].apply(clean_date)

# 2. Pastikan semua tanggal valid
invalid_dates = sales[sales["order_date"].isna()]
if not invalid_dates.empty:
    print("⚠️ Ada tanggal yang tidak bisa dikonversi:")
    print(invalid_dates[["order_id", "order_date"]])

# 3. Isi kolom total_amount jika kosong (quantity * price)
sales["total_amount"] = sales.apply(
    lambda x: x["quantity"] * x["price"] if pd.isna(x["total_amount"]) else x["total_amount"],
    axis=1
)

# 3. Gabungkan dengan data customer
sales_enriched = pd.merge(
    sales,
    customers,
    on="customer_id",
    how="left"
)

# 4. Tambah kolom order_month untuk analisis waktu
sales_enriched["order_month"] = sales_enriched["order_date"].dt.to_period("M").astype(str)

# 5. Urutkan berdasarkan tanggal
sales_enriched = sales_enriched.sort_values(by="order_date")

# === L: Load ===
print("💾 Loading to CSV...")
sales_enriched.to_csv("/home/master/github/python-demo-project/week1_python_for_de/data/sales_enriched.csv", index=False)

print("\n✅ ETL Selesai! Hasil tersimpan di 'data/sales_enriched.csv'")
print(f"Total records: {len(sales_enriched)}")
print(sales_enriched.head())