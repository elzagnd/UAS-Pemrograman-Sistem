import sqlite3

try:
    # Koneksi ke database
    conn = sqlite3.connect('mahasiswa.db')
    c = conn.cursor()

    # Membuat tabel
    c.execute('''CREATE TABLE IF NOT EXISTS mahasiswa (
                    nim TEXT PRIMARY KEY,
                    nama TEXT,
                    email TEXT
                )''')

    # Data mahasiswa
    mahasiswa = [
        ('001', 'elza', 'elza@example.com'),
        ('002', 'nanda', 'nanda@example.com'),
        ('003', 'Charlie', 'charlie@example.com')
    ]

    # Mengisi tabel
    c.executemany('INSERT INTO mahasiswa (nim, nama, email) VALUES (?, ?, ?)', mahasiswa)

    # Commit perubahan
    conn.commit()

    print("Data telah berhasil dimasukkan ke dalam tabel 'mahasiswa'.")

except sqlite3.IntegrityError as e:
    print("Error: Terjadi duplikasi nilai pada primary key 'nim'.")
    print(e)
except Exception as e:
    print("Error: Terjadi kesalahan saat mengakses database.")
    print(e)
finally:
    # Tutup koneksi
    if conn:
        conn.close()
