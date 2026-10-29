# Praktik Pertemuan 11
# Sistem Data Mahasiswa

def cari_mahasiswa(data, nim):
    return data.get(nim)

def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0
    for info in data.values():
        total += info["nilai"]

    return total / len(data)

# Data awal
data_mahasiswa = {
    "A001": {"nama": "meisya", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

print("=== Pencarian Mahasiswa ===")

nim = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil:
    print(f"{nim}: {hasil}")
else:
    print("Data tidak ditemukan")

print("\n=== Pencarian NIM Tidak Ada ===")

nim = "A999"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil:
    print(f"{nim}: {hasil}")
else:
    print("Data tidak ditemukan")

# Tambah mahasiswa
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

# Ubah nilai
data_mahasiswa["A002"]["nilai"] = 82

print("\n=== Rekap Semua Mahasiswa ===")

for nim, info in data_mahasiswa.items():
    print(f"{nim}: {info}")

print("\nRata-rata nilai:", round(rata_rata_nilai(data_mahasiswa), 2))