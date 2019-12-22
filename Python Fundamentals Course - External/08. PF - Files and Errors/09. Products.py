class Product:
    def __init__(self, name: str, type_: str, price: float, quantity: int):
        self.name = name
        self.type_ = type_
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.type_}, Product: {self.name}\nPrice: ${self.price:.2f}, Amount Left: {self.quantity}"


def check_for_db():
    stocked_list = []
    try:
        with open('D:\\Testy\\products.txt', 'r') as stock_file:
            stock_info = stock_file.readlines()
            for stocked_product in stock_info:
                info = stocked_product.split()
                new_product = Product(name=info[0], type_=info[1], price=float(info[2]), quantity=int(info[3]))
                stocked_list.append(new_product)

            return stocked_list
    except FileNotFoundError:
        return stocked_list


def analyze():
    list_to_analyze = check_for_db()
    if not list_to_analyze:
        print("No products stocked")
        return
    list_to_analyze.sort(key=lambda x: x.type_)
    for item in list_to_analyze:
        print(item)


def sales(products_list: list):
    product_categories = {'Domestics': 0, 'Electronics': 0, 'Food': 0}
    for key in product_categories.keys():
        for prod_obj in products_list:
            if prod_obj.type_ == key:
                product_categories[key] += float(prod_obj.price) * int(prod_obj.quantity)

    for category, value in sorted(product_categories.items(), key=lambda kv: kv[1], reverse=True):
        if value > 0:
            print(f"{category}: ${value:.2f}")


def stock(products_list: list):
    if not products_list == []:
        with open('D:\\Testy\\products.txt', 'w') as output_file:
            for pr in products_list:
                output_file.write(f'{pr.name} {pr.type_} {float(pr.price):.2f} {int(pr.quantity)}\n')
    else:
        print('No products stocked')


def create_product(input_data: list):
    add_new = Product(name=input_data[0],
                      type_=input_data[1],
                      price=float(input_data[2]),
                      quantity=int(input_data[3]))
    return add_new


def change_product(input_data: list, product: object):
    product.price = float(input_data[2])
    product.quantity = int((input_data[3]))


def check_product(input_data: list, products_list: list):
    if products_list:
        for product in products_list:
            if product.name == input_data[0] and product.type_ == input_data[1]:
                change_product(input_data, product)
                return products_list
        products_list.append(create_product(input_data))
        return products_list
    else:
        products_list.append(create_product(input_data))
        return products_list


def main():
    products_list = []
    stocked_list = check_for_db()
    products_list.extend(stocked_list)
    while True:
        input_command = input().split()
        if input_command[0] == 'analyze':
            analyze()
        elif input_command[0] == 'sales':
            sales(products_list)
        elif input_command[0] == 'stock':
            stock(products_list)
        elif input_command[0] == 'exit':
            exit()
        else:
            products_list = check_product(input_command, products_list)


if __name__ == "__main__":
    main()
