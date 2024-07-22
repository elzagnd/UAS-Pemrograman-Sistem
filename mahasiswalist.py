class Mahasiswa:
    def __init__(self, nim, nama, email):
        self.nim = nim
        self.nama = nama
        self.email = email

    def __str__(self):
        return f'NIM: {self.nim}, Nama: {self.nama}, Email: {self.email}'

class MahasiswaList:
    def __init__(self):
        self.list_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.list_mahasiswa.append(mahasiswa)

    def tampilkan_mahasiswa(self):
        for mahasiswa in self.list_mahasiswa:
            print(mahasiswa)

# Membuat objek MahasiswaList
mahasiswa_list = MahasiswaList()

# Menambahkan data mahasiswa
mahasiswa1 = Mahasiswa('001', 'Elza', 'elzae@example.com')
mahasiswa2 = Mahasiswa('002', 'Nanda', 'nanda@example.com')
mahasiswa_list.tambah_mahasiswa(mahasiswa1)
mahasiswa_list.tambah_mahasiswa(mahasiswa2)

# Menampilkan data mahasiswa
mahasiswa_list.tampilkan_mahasiswa()
