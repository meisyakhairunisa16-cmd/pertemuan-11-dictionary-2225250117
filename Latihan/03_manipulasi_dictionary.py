# Manipulasi Dictionary

data = {
    "nama": "meisya",
    "nilai": 85
}

# Menambah data
data["kelas"] = "A"

# Mengubah data
data["nilai"] = 90

print("Setelah ditambah dan diubah:")
print(data)

# Menghapus data
data.pop("kelas")

print("\nSetelah kelas dihapus:")
print(data)