class Transaction:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, item_qty, item_price):
        self.items.append({'name': item_name, 'qty': item_qty, 'price': item_price})

    def update_item_name(self, item_name, new_name):
        for item in self.items:
            if item['name'] == item_name:
                item['name'] = new_name

    def update_item_qty(self, item_name, new_qty):
        for item in self.items:
            if item['name'] == item_name:
                item['qty'] = new_qty

    def update_item_price(self, item_name, new_price):
        for item in self.items:
            if item['name'] == item_name:
                item['price'] = new_price

    def delete_item(self, item_name):
        for item in self.items:
            if item['name'] == item_name:
                self.items.remove(item)

    def reset_transaction(self):
        self.items = []

    def check_order(self):
        for item in self.items:
            if item['name'] == '' or item['qty'] == 0 or item['price'] == 0:
                print('Terdapat kesalahan input data')
                return
        print('Pemesanan sudah benar')
        for item in self.items:
            print(f'{item["qty"]} {item["name"]} @ Rp{item["price"]}')

    def total_price(self):
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


