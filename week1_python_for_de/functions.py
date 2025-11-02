# - Contoh: hitung total penjualan dari list angka.
# - Buat fungsi get_total_sales() yang menerima list dan mengembalikan jumlah total.

sales = [1000,2000,3000,4000,6000]
def get_total_sales(sales):
    return sum(sales)

total = get_total_sales(sales)
print("Total penjualan:", total)