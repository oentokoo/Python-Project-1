class Transaction:
    def __init__(self): #Fungsi ini akan dijalankan saat objek dari class Transaction dibuat. Pada fungsi ini, atribut items didefinisikan sebagai list kosong. Atribut ini akan digunakan untuk menyimpan item-item yang dibeli oleh customer.
        self.items = []

    def add_item(self, item_name, item_qty, item_price): # Fungsi ini digunakan untuk menambahkan item baru ke dalam list items. Parameter yang diperlukan adalah nama item, jumlah item, dan harga per item.
        self.items.append({'name': item_name, 'qty': item_qty, 'price': item_price})

    def update_item_name(self, item_name, new_name): #Fungsi ini digunakan untuk mengubah nama item yang sudah ada dalam list items. Parameter yang diperlukan adalah nama item yang ingin diubah dan nama baru yang akan digunakan.
        for item in self.items:
            if item['name'] == item_name:
                item['name'] = new_name

    def update_item_qty(self, item_name, new_qty): #Fungsi ini digunakan untuk mengubah jumlah item yang sudah ada dalam list items. Parameter yang diperlukan adalah nama item yang ingin diubah dan jumlah baru yang akan digunakan.
        for item in self.items:
            if item['name'] == item_name:
                item['qty'] = new_qty

    def update_item_price(self, item_name, new_price): #Fungsi ini digunakan untuk mengubah harga item yang sudah ada dalam list items. Parameter yang diperlukan adalah nama item yang ingin diubah dan harga baru yang akan digunakan.
        for item in self.items:
            if item['name'] == item_name:
                item['price'] = new_price

    def delete_item(self, item_name): #ungsi ini digunakan untuk menghapus item dari list items. Parameter yang diperlukan adalah nama item yang ingin dihapus.
        for item in self.items:
            if item['name'] == item_name:
                self.items.remove(item)

    def reset_transaction(self): #Fungsi ini digunakan untuk menghapus semua item dari list items.
        self.items = []

    def check_order(self): #Fungsi ini digunakan untuk memeriksa apakah semua item dalam list items memiliki nama, jumlah, dan harga yang valid. Jika terdapat kesalahan input, fungsi akan mengeluarkan pesan kesalahan dan tidak akan menampilkan daftar pemesanan. Jika tidak ada kesalahan, fungsi akan mengeluarkan pesan "Pemesanan sudah benar" dan menampilkan daftar pemesanan.
        for item in self.items:
            if item['name'] == '' or item['qty'] == 0 or item['price'] == 0:
                print('Terdapat kesalahan input data')
                return
        print('Pemesanan sudah benar')
        for item in self.items:
            print(f'{item["qty"]} {item["name"]} @ Rp{item["price"]}')

    def total_price(self): #digunakan untuk menghitung total harga belanja dari semua item yang ada dalam list items. Pertama, variable total_price diinisialisasi dengan 0. Kemudian, loop dijalankan untuk mengecek setiap item dalam list items. Pada setiap iterasi, jumlah item dikali dengan harga item dan ditambahkan ke total_price.
        total_price = 0
        for item in self.items:
            total_price += item['qty'] * item['price']

        if total_price > 200000:
            total_price *= 0.95
        if total_price > 300000:
            total_price *= 0.92
        if total_price > 500000:
            total_price *= 0.9

        print(f'Total harga: Rp{total_price}')
        #Setelah semua item diterima, fungsi akan mengecek apakah total harga melebihi batas diskon tertentu. Jika ya, maka diskon akan diterapkan pada total harga. Dalam kode yang diberikan, jika total harga melebihi Rp 200.000, akan diberikan diskon 5%. Jika melebihi Rp 300.000, akan diberikan diskon 8%. Jika melebihi Rp 500.000, akan diberikan diskon 10%. Setelah diskon diterapkan, fungsi akan mengeluarkan total harga belanja dengan format Rupiah.

    def choose_payment_method(self, method):  #Fungsi ini digunakan untuk memilih metode pembayaran yang dikehendaki oleh konsumen
        self.payment_method = method
        
    def get_payment_method(self): #Fitur ini digunakan untuk mengetahui metode pembayaran apa yang digunakan oleh konsumen untuk 
        return self.payment_method

