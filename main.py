# Data buku
books = [
    {"isbn":"9786237121144", "judul":"cara jadi heker", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"rikihama", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"cara jadi perintis", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"cara jadi pewaris", "jumlah":4, "terpinjam":0}
]

# Data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""}
]

def tampilkan_data():
    print("\n--- Data Buku ---")
    for b in books:
        print(f"ISBN: {b['isbn']}, Judul: {b['judul']}, Pengarang: {b['pengarang']}, Jumlah: {b['jumlah']}, Terpinjam: {b['terpinjam']}")

def tambah_data():
    isbn = input("ISBN: ")
    judul = input("Judul: ")
    pengarang = input("Pengarang: ")
    jumlah = int(input("Jumlah: "))
    books.append({"isbn":isbn, "judul":judul, "pengarang":pengarang, "jumlah":jumlah, "terpinjam":0})
    print("Buku berhasil ditambahkan.")

def edit_data():
    isbn = input("Masukkan ISBN buku yang ingin diedit: ")
    for b in books:
        if b["isbn"] == isbn:
            b["judul"] = input(f"Judul baru ({b['judul']}): ") or b["judul"]
            b["pengarang"] = input(f"Pengarang baru ({b['pengarang']}): ") or b["pengarang"]
            b["jumlah"] = int(input(f"Jumlah baru ({b['jumlah']}): ") or b["jumlah"])
            print("Data buku berhasil diperbarui.")
            return
    print("Buku tidak ditemukan.")

def hapus_data():
    isbn = input("Masukkan ISBN buku yang ingin dihapus: ")
    for b in books:
        if b["isbn"] == isbn:
            books.remove(b)
            print("Buku berhasil dihapus.")
            return
    print("Buku tidak ditemukan.")

def tampilkan_peminjaman():
    print("\n--- Semua Data Peminjaman ---")
    for r in records:
        print(f"ISBN: {r['isbn']}, Status: {r['status']}, Tgl Pinjam: {r['tanggal_pinjam']}, Tgl Kembali: {r['tanggal_kembali']}")

def tampilkan_belum():
    print("\n--- Pinjaman Belum Kembali ---")
    for r in records:
        if r["status"] == "Belum":
            print(f"ISBN: {r['isbn']}, Tgl Pinjam: {r['tanggal_pinjam']}")

def peminjaman():
    isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
    for b in books:
        if b["isbn"] == isbn:
            if b["jumlah"] - b["terpinjam"] > 0:
                b["terpinjam"] += 1
                tanggal = input("Tanggal pinjam (YYYY-MM-DD): ")
                records.append({"isbn":isbn, "status":"Belum", "tanggal_pinjam":tanggal, "tanggal_kembali":""})
                print("Pinjaman berhasil dicatat.")
            else:
                print("Buku sedang tidak tersedia.")
            return
    print("ISBN tidak ditemukan.")

def pengembalian():
    isbn = input("Masukkan ISBN buku yang dikembalikan: ")
    for r in records:
        if r["isbn"] == isbn and r["status"] == "Belum":
            r["status"] = "Selesai"
            r["tanggal_kembali"] = input("Tanggal kembali (YYYY-MM-DD): ")
            for b in books:
                if b["isbn"] == isbn:
                    b["terpinjam"] -= 1
            print("Pengembalian berhasil dicatat.")
            return
    print("Data pinjaman belum ditemukan.")

# Menu utama
while True:
    print("\n---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Pinjaman")
    print("[6] Tampilkan Pinjaman Belum Kembali")
    print("[7] Pinjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau X): ").upper()
    if menu == "1":
        tampilkan_data()
    elif menu == "2":
        tambah_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        hapus_data()
    elif menu == "5":
        tampilkan_pinjaman()
    elif menu == "6":
        tampilkan_belum()
    elif menu == "7":
        peminjaman()
    elif menu == "8":
        pengembalian()
    elif menu == "X":
        print("👋 Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")
        
