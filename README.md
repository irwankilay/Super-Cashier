# Python Project Pacmann - Super Cashier
Super Cashier is a self-service cashier system which developed using Python programming language and connected with SQLite database.

# Background problems
Andi is the owner of a large supermarket in a city in Indonesia. Andi has plans to improve business processes by building a self-service 
cashier system at his supermarket. With this self-service system, Customers can directly enter the items purchased, the number of items 
purchased, and the price of the items purchased and other features

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
   ![Menu Utama](https://github.com/irwankilay/Super-Cashier/blob/main/flowchart.jpg)

#  Code Explanation
   From the flow chart above, there are 9 functions created.
   1. Menu_utama()
      This function is to show main menu of cashier program
   2. Menu_transaksi()
      This function is to show transaction menu 
   3. Tambah_item()
      This function is to add item in a transaction 
   4. update_item()
      This function is to update an item in a transaction
   5. hapus_item()
       This function is to delete an item in a transaction
   6. checkout()
       This function is to check out the cart
   7. lihat_keranjang()
       This function is to display the chart
   8. insert_to_table()
      This function is to insert transaction to SQLite database
   9. buat_transaksi_id()
      This function is to create transaction ID

#  Test Case Result
1.  Main Menu and create new transaction by entering 1
   ![Menu Utama](https://github.com/irwankilay/Super-Cashier/blob/main/1.jpg)
    
2. Transaction Menu and add item by entering 1
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

   Enter Transaction Menu No 5 
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/7a.jpg)

   Discount and Total pay
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/7-b.jpg)

   Pay the transaction and Data saved to SQLite
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/7-c.jpg)

   Main Transaction table in SQLite
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/7-d.jpg)

   Detail Transaction table in SQLite
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/7-e.jpg)

11. Create New Transaction and cancel

   Enter Transaction Menu No 1 and Add Manisan
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/8a.jpg)

   Enter Transaction Menu No 6 to cancel transaction
   ![Item no 2](https://github.com/irwankilay/Super-Cashier/blob/main/8b.jpg)

# Conclusion/Future Work

1. User Interface Enhancements: Currently, the program uses a text-based interface.
   Creating a graphical user interface (GUI) to improve the user experience and make
   the program more visually appealing and intuitive.
2. Error Handling and Validation: Enhance the program with robust error handling and
   input validation mechanisms. This would help prevent incorrect or invalid inputs,
   handle exceptions gracefully, and provide meaningful error messages to the user.
3. Multi-user Support: Implement a user authentication system to support multiple
   cashiers or users. This would enable individual login accounts, access control,
   and tracking of transactions performed by different users.
4. Localization and Internationalization: Make the program adaptable to different
   languages and regions.

