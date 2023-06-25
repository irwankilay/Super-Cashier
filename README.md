# Python Project Pacmann - Super Cashier
Super Cashier is a self-service cashier system which developed using Python programming language and connected with SQLite database.

# Background problems
Andi is the owner of a large supermarket in a city in Indonesia. Andi has plans to improve business processes by building a self-service 
cashier system at his supermarket. With this self-service system, 
- Customers can directly enter the items purchased, the number of items purchased, and the price of the items purchased and other features
- Customers who are not in the city can buy goods from this supermarket.

# Feature Requirements
1. Customer can create a transaction ID by creating an object from function transaction().
2. Customers can directly enter the items purchased, the number of items purchased, and the price of the items purchased
3. If there is incorrect item name, or number of items purchased, or price of the items purchased, customer can update.
4. dasdas

# Cara Menggunakan Program
1. Download semua file/module Python ke dalam satu direktori lokal.
2. Definisikan variabel-variabel di module init_variable.py dan simpan.
3. Buka terminal dan sesuaikan lokasi direktori lokal.
4. Jalankan module python start.py di terminal.
5. Jalankan module python main.py di terminal.
6. Anda cukup menjalankan module python start.py satu kali, dan dapat menjalankan module python main.py saja setelahnya.

# Hasil Test Case
1. Pendaftaran Anggota Baru

    - Penambahan Data Anggota Baru

    ![1 Pendaftaran Anggota Baru](https://user-images.githubusercontent.com/109220639/180597034-aa853286-f291-4ca3-9633-ca7678568647.jpg)

    - Menampilkan Daftar Anggota Setelah Pendaftaran

    ![4 Tampilkan Daftar Anggota](https://user-images.githubusercontent.com/109220639/180597039-0df64db9-625c-44b8-8da7-661a3f932c59.jpg)

2. Pendaftaran Buku

    - Penambahan Data Buku Baru
    
    ![2 Pendaftaran Buku Baru](https://user-images.githubusercontent.com/109220639/180597228-5fc20b1d-7ebf-4e59-87bd-0c4b66c94434.jpeg)
    
    - Menampilkan Daftar Buku 
    
    ![5 Tampilkan Daftar Buku](https://user-images.githubusercontent.com/109220639/180597232-f9d7f8bb-e7b8-46d4-b91c-fad65f0f1854.jpeg)
    
3. Peminjaman Buku

    - Melakukan Peminjaman
    
    ![3 Peminjaman Buku](https://user-images.githubusercontent.com/109220639/180597274-acfcaa86-c65c-4117-b098-6297c6168ee4.jpeg)

    - Menampilkan Daftar Peminjaman
    
    ![6 Tampilkan Daftar Peminjaman](https://user-images.githubusercontent.com/109220639/180597280-6e9efba5-21bf-478a-a628-1074b42eb456.jpeg)

    - Menampilkan Daftar Buku Setelah Peminjaman (stok berkurang 1)
    
    ![Daftar Buku Setelah Peminjaman](https://user-images.githubusercontent.com/109220639/180597288-40e27e4d-d0f4-444e-87fc-2ce4ffff80c9.jpeg)

4. Pengembalian Buku

    - Melakukan Pengembalian 
    
    ![7 Pengembalian Buku](https://user-images.githubusercontent.com/109220639/180597304-0e910549-f768-4b80-a928-9fde3301a662.jpeg)

    - Menampilkan Daftar Peminjaman (data peminjaman terhapus)
    
    ![Daftar Peminjaman Setelah Pengembalian](https://user-images.githubusercontent.com/109220639/180597312-4c24b1e7-5e36-475e-9c15-4d5a992eed73.jpeg)

    - Menampilkan Daftar Buku Setelah Pengembalian (stok terupdate)
    
    ![Daftar Buku Setelah Pengembalian](https://user-images.githubusercontent.com/109220639/180597320-f2c31016-1e1f-4f3c-b352-81b746a481c9.jpeg)

5. Meampilkan Hasil Pencarian Judul Buku

![Pencarian Judul Buku](https://user-images.githubusercontent.com/109220639/180597323-2f7313e6-e67f-4772-9f4c-2a18248625b6.jpeg)

# Saran Perbaikan
1. Membuat program yang berbasis objek dengan bentuk/type Class.
2. Mengembangkan program dengan fungsi yang lebih kompleks. Misalnya, output untuk pengembalian buku yang terlambat dari batas waktu peminjaman (7 hari).
3. Perbaikan lainnya yang mungkin ditemukan setelah program digunakan oleh beberapa user.

