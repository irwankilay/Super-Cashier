# Python Project Pacmann - Super Cashier
Super Cashier is a self-service cashier system which developed using Python programming language and connected with SQLite database.

# Background problems
Andi is the owner of a large supermarket in a city in Indonesia. Andi has plans to improve business processes by building a self-service 
cashier system at his supermarket. With this self-service system, 
- Customers can directly enter the items purchased, the number of items purchased, and the price of the items purchased and other features
- Customers who are not in the city can buy goods from this supermarket.

# Requirements
1. Customer can create a transaction ID by creating an object from transaction() function.
2. Customers can directly enter the items purchased, the number of items purchased, and the price of the items purchased.
3. If there is incorrect item name, or number of items purchased, or price of the items purchased, customer can update.
   - Update item name use update_item_name() function.
   - Update number of items purchased use update_item_qty() function.
   - Update price of the items purchased use update_item_price() function.
   
5. If customer want to cancel the purchased items, customer can do
   -  Cancel one item use delete_item() function. If one of the item purchased is cancelled, then number of items purchased,
      and the price of the items purchased will be deleted.
   - Cancel all the items by resetting the reset_transaction() function.
   
7. If customer has finished shopping online, but the customer is still unsure whether the price of the item and the name
   of the item entered are correct, It is possible for a customer to make a correction using check_order() function.
   for example, having entered the price of an item but forgot to enter the name of the item.
   When check_order() function is called, there are
   - Will show message "All transaction are correct" if there is no incorrect entry.
   - Will show message "There is incorrect data input" if there is incorrect entry.
   - Will swho all the item transactions purchased.
   
   | No | Nama Item | Jumlah Item | Harga/Item | Total Harga |
   |----|-----------|-------------|------------|-------------|
   | 1  | Mobil     | 2           | 100000     | 200000      |
   | 2  | Mie       | 1           | 5000       | 5000        |
   | 3  | Tempe     | 3           | 3000       | 9000        |

9. After checking, the customer can calculate the total shopping that has been purchased use the check_out() function.
   - If the total price per item Andi is above IDR 200000, will get a 5% discount
   - If the total price per item Andi is above IDR 300000, will get a 6% discount
   - If the total price per item Andi is above IDR 500000, will get a 7% discount
   - Total purchases are only displayed in the check_out() function, but are not stored in the database yet.

10. Every time the check_out() is executed and pay_now() is executed, transaction data is inserted into the sqlite database
    in the transaction table using the insert_to_table() function.
    The following are columns created to store data in the database :
    | Column Name      | Description                               |
    |------------------|-------------------------------------------| 
    | trans_id :       |  id transaction (auto increment)          | 
    | Item_name      : |  the name of the item purchased           | 
    | amount_item    : |  the number of items purchased            | 
    | price          : |  item price                               | 
    | total_price    : |  total price (number of items * price)    | 
    | discount       : |  discounted price                         | 
    | price_discount : |  the price of the item after the discount |

 11. Must be in Modular Code and not class based.
 12. the Main program have menu for cashier application to
     - Start new transaction,
     - Check Out
     - Reset Transaction
     - Exit the application
     When new transaction is started, the following menu will be appear.
     - Add Item purchased
     - Update item name, number of items purchased or price of the items purchased
     - Delete Item Purchased
     - Go to Main.
 14. Have Docstring comments on the function made.
 15. Have try, error in the branching for easy for error tracking.

# Flow Chart


#  Code Explanation


#  Test Case Result
1.  Main Menu
   ![Menu Utama](https://github.com/irwankilay/Super-Cashier/blob/main/1.jpg)
    
2. Transaction Menu 
   ![Menu Utama](https://github.com/irwankilay/Super-Cashier/blob/main/2.jpg)

3. Add 3 item into Transaction
   
   Item No. 1
   ![Item no 1](https://github.com/irwankilay/Super-Cashier/blob/main/3a.jpg)

   Item No. 2
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/3b.jpg)

   Item No. 3
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/3c.jpg)
   
5. Display Item Purchased
   
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/4a.jpg)

   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/4b.jpg)
   
7. Update Item and Display after updated

   Enter Transaction Menu No 2.
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/5a.jpg)

   Update item kecap 
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/5b.jpg)

   Display cart after kecap updated
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/5c.jpg)

8. Add Item and Display after deleted

   Enter Transaction Menu No 2 and add item Biscuit
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/6a.jpg)

   Enter Transaction Menu No 3 and Delete item biscuit
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/6b.jpg)

   Display cart after item biscuit deleted
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/6c.jpg) 

9. Check out

   Enter Transaction Menu No 5 and add item Biscuit
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/7a.jpg)

   Enter Transaction Menu No 3 and Delete item biscuit
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/7b.jpg)

   Display cart after item biscuit deleted
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/7c.jpg) 

# Conclusion/Future Work

1. Membuat program yang berbasis objek dengan bentuk/type Class.
2. Mengembangkan program dengan fungsi yang lebih kompleks. Misalnya, output untuk pengembalian buku yang terlambat dari batas waktu peminjaman (7 hari).
3. Perbaikan lainnya yang mungkin ditemukan setelah program digunakan oleh beberapa user.

