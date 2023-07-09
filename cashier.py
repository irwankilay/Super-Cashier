import os
import tty
import sqlite3

keranjang = []  # Keranjang belanja

trans_count = 0

def buat_transaction_id(prefix):
    """
    Menghasilkan ID secara otomatis
    """
    try:
    
        global trans_count
        trans_count += 1
        trans_id = f"{prefix}{trans_count:04d}"
        return trans_id

    except Exception as e:
        print("error terjadi ketika buat transaksi ID:", e)

def mulai_transaksi():
    """
    Logic to start a new transaction
    """
    try:
        print("New transaction started.")
        menu_transaksi()

    except Exception as e:
        print("error terjadi ketika mulai transaksi:", e)

def batalkan_transaksi():
    '''
    membatalkan transaksi
    '''
    try:
        print("transaction is dibatalkan.")
        menu_transaksi()

    except Exception as e:
        print("error terjadi ketika membatalkan transaksi:", e)

def menu_utama():
    '''
    Menu Utama dari program kasir
    '''
    try:
        while True:
            os.system('clear')
            print("=== Program Kasir ===")
            print("1. Transaksi baru")
            print("0. Keluar")
       
            pilihan = input("Masukan pilihan : ")
            if pilihan == "0":
                break 
            elif pilihan == "1":
                mulai_transaksi()
                break
            else:
                print("Pilihan anda tidak valid")
    
    except Exception as e:
        print("error terjadi ketika di menu utama:", e)

def menu_transaksi():
        '''
        Menu-menu transaksi
        '''
        os.system('clear')
        print("----- Transaction Menu -----")
        print("1. Add Item purchased")
        print("2. Update item name, number of items purchased, or price of the items purchased")
        print("3. Delete Item Purchased")
        print("4. Lihat Keranjang")
        print("5. Check Out")
        print("6. Batalkan Transaksi. Go to Main")

        pilihan = input("Enter your pilihan: ")
        if pilihan == "1":
            tambah_item()
        elif pilihan == "2":
            update_item()
            pilihan=input("Press Enter to continue...")
            if pilihan == "":
                menu_transaksi()
        elif pilihan == "3":
            hapus_item()
            pilihan=input("Press Enter to continue...")
            if pilihan == "":
                menu_transaksi()
        elif pilihan == "4":
            lihat_keranjang()
            pilihan=input("Press Enter to continue...")
            if pilihan == "":
                menu_transaksi()
        elif pilihan == "5":
            checkout()
        elif pilihan == "6":
            keranjang.clear()
            pilihan=input("Transaksi telah di-batalkan.\nPress Enter to continue...")
            if pilihan == "":
                menu_utama()
        else:
            print("Invalid choice. Please try again.")

def tambah_item():
    '''
    fungsi untuk menambah item transaksi
    '''
    nama_item = input("Masukkan nama item: ")
    jumlah_item = int(input("Masukkan jumlah item: "))
    harga_barang = int(input("Masukkan harga barang: "))
    item = (nama_item, jumlah_item, harga_barang)
    keranjang.append(item)
    pilihan=input("Press Enter to continue...")
    if pilihan == "":
        menu_transaksi()

def update_item():
    '''
    fungsi untuk megupdate item transaksi
    '''
    lihat_keranjang()
    nama_item = input("Masukkan nama item: ")
    jumlah_item = int(input("Masukkan jumlah item: "))
    harga_barang = int(input("Masukkan harga barang: "))
    for i, item in enumerate(keranjang):
        if item[0] == nama_item:
            updated_item = list(item)
            updated_item[1] = jumlah_item
            updated_item[2] = harga_barang
            keranjang[i] = tuple(updated_item)
    lihat_keranjang()

def hapus_item():
    '''
    fungsi untuk menghapus item
    '''
    lihat_keranjang()
    for item in keranjang:
        nama_item = input("Masukkan nama item: ")
        if item[0] == nama_item:
            keranjang.remove(item)
            break
    lihat_keranjang()

def checkout():
    '''
    fungsi untuk checkout dan pembayaran
    '''
    total_price = sum(item[1] * item[2] for item in keranjang)
    discount = 0.0

    if total_price > 500000:
        discount = 0.07
    elif total_price > 300000:
        discount = 0.06
    elif total_price > 200000:
        discount = 0.05

    discount_amount = total_price * discount
    total_purchase = total_price - discount_amount

    lihat_keranjang()
    print(f"Total Diskon: IDR {discount_amount:.0f}")
    print(f"Total yang harus dibayar : IDR {total_purchase:.0f}")

    pilihan=input("Press Enter to continue untuk membayar...")
    if pilihan == "":
        trans_id=buat_transaction_id("TR")
        insert_to_table(trans_id,discount, total_purchase)
        # Insert transaction data into the database
        pilihan=input("Pembayaran sudah diterima. Kembali ke menu utama.")
        if pilihan == "":
            menu_utama()
    else:
        menu_transaksi()

def lihat_keranjang():
    '''
    fungsi untuk lihat keranjang
    '''
    os.system('clear')
    print("== Keranjang ==")
    if len(keranjang) == 0:
        print("Keranjang kosong.")
    else:
        header = ["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
        max_lengths = [len(header[i]) for i in range(len(header))]

        for item in keranjang:
            for i in range(len(item)):
                if len(str(item[i])) > max_lengths[i]:
                    max_lengths[i] = len(str(item[i]))

        line = "+"
        for length in max_lengths:
            line += "-" * (length + 2) + "+"
        print(line)

        for i, header_item in enumerate(header):
            if i in [2, 3, 4]:  # Align "Jumlah Item", "Harga/Item", and "Total Harga" headers to the right
                print(f"| {header_item:>{max_lengths[i]}} ", end="")
            else:
                print(f"| {header_item:<{max_lengths[i]}} ", end="")
        print("|")

        print(line)

        for i, item in enumerate(keranjang, start=1):
            row = f"| {i:<{max_lengths[0]}} | {item[0]:<{max_lengths[1]}} | {item[1]:>{max_lengths[2]}} | {item[2]:>{max_lengths[3]}} | {item[1] * item[2]:>{max_lengths[4]}} |"
            print(row)

        print(line)
        

def insert_to_table(trans_id,discount, price_discount):
    """
    Inserts the transaction data into the 'transaction' table in the SQLite database.
    """
 
    try:
        conn = sqlite3.connect("your_database.db")
        cursor = conn.cursor()

        query = '''CREATE TABLE IF NOT EXISTS main_trans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trans_id TEXT,
            discount REAL,
            price_discount INTEGER
        )'''
        cursor.execute(query)

        query = '''CREATE TABLE IF NOT EXISTS details_trans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trans_id TEXT,
            Item_name TEXT,
            amount_item INTEGER,
            price INTEGER,
            total_price INTEGER
        )'''
        cursor.execute(query)

        query = "INSERT INTO main_trans (trans_id, discount, price_discount) VALUES (?,?, ?)"
        cursor.execute(query, (trans_id,discount, price_discount))

        for item in keranjang:
            item_name = item[0]
            amount_item = item[1]
            price = item[2]
            total_price = amount_item * price
            query = "INSERT INTO details_trans (trans_id,item_name, amount_item, price, total_price) VALUES (?,?, ?, ?, ?)"
            cursor.execute(query, (trans_id,item_name, amount_item, price, total_price))

        conn.commit()
        cursor.close()
        conn.close()
        keranjang.clear()
        print("Transaction data inserted successfully.")
    except Exception as e:
        print("An error occurred while inserting transaction data:", e)
