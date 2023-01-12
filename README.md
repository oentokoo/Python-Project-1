# Python-Project-1
Project Pythonn from Pacmann about Python Self Service System in Mini Market 

#Latar Belakang Project

Project Python ini merupakan project pertama yang memiliki case latar belakang bahwa terdapat seseorang yang memiliki supermarket yang besar dan memiliki rencana untuk merubah alur bisnis supermarket yang dimilikinya dengan membuat sistem self service, yang mana customer dapat melakukan transaksi belanja online sendiri dengan menggunakan kode Python. Dengan menggunakan kode ini, customer dapat melakukan aktivitas seperti menambahkan, mengubah, dan menghapus item yang akan dibeli, serta melakukan pengecekan dan pembayaran transaksi yang dilakukan. Ini dapat digunakan untuk memudahkan customer dalam berbelanja tanpa harus mengantri atau berkomunikasi dengan kasir, dan juga mempermudah proses pembayaran dan pengaturan transaksi untuk pihak pengelola toko.

#Requirements Program 

Program Python tersebut memiliki Requierments sebagai berikut :

1. Membuat objek dari class Transaction yang akan digunakan sebagai ID transaksi
2. Memasukkan nama item, jumlah item, dan harga barang yang akan dibeli menggunakan method add_item
3. Mengubah nama, jumlah, dan harga item yang sudah ditambahkan ke dalam list items menggunakan method update_item_name, update_item_qty, dan update_item_price
4. Menghapus item dari list items menggunakan method delete_item atau menghapus semua item dengan method reset_transaction
5. Memeriksa kebenaran data transaksi menggunakan method check_order
6. Menghitung total harga belanja dan memberikan diskon jika total belanja melebihi batas tertentu menggunakan method total_price

#Alur Program

1. Customer membuat ID transaksi dengan membuat objek dari class Transaction
2. Customer memasukkan nama item, jumlah item, dan harga barang dengan menggunakan method add_item
3. Jika terjadi kesalahan dalam memasukkan data, customer bisa menggunakan method update_item_name, update_item_qty, atau update_item_price untuk mengubah data yang salah
4. Jika ingin membatalkan transaksi, customer bisa menggunakan method delete_item untuk menghapus item tertentu atau reset_transaction untuk menghapus semua item
5. Customer dapat mengecek data transaksi dengan method check_order yang akan mengeluarkan pesan kesalahan atau pemesanan yang benar
6. Customer dapat menghitung total harga belanja dengan method total_price yang akan memberikan diskon jika total belanja melebihi batas tertentu.
7. Customer dapat menambahkan metode pembayaran yang ingin digunakan 

#Test Case

<img width="1440" alt="Screenshot 2023-01-12 at 23 13 47" src="https://user-images.githubusercontent.com/122088142/212122983-3105ec25-c37d-4a60-b8ba-c58e07a5e1ae.png">

<img width="1440" alt="Screenshot 2023-01-12 at 23 13 58" src="https://user-images.githubusercontent.com/122088142/212123032-16ceeab9-6857-4cac-99d2-b6ffc1f25627.png">

<img width="1440" alt="Screenshot 2023-01-12 at 23 14 04" src="https://user-images.githubusercontent.com/122088142/212123093-b638d753-6e1f-40a8-9a8c-ba339bdabdac.png">
