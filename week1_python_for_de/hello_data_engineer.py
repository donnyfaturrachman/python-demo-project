print('Donny Faturrachman')
from datetime import datetime, date
# waktu sekarang lengkap
now = datetime.now()
print("Tanggal dan waktu sekarang:", now.strftime("%Y-%m-%d %H:%M:%S"))

# hanya tanggal hari ini
today = date.today()
print("Tanggal hari ini:", today.isoformat())