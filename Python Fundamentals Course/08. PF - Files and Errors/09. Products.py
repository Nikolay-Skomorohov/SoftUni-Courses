class Product:
    def __init__(self, name: str, type_: str, price: float, quantity: int):
        self.name = name
        self.type_ = type_
        self.price = price
        self.quantity = quantity


products_list = []

while True:
    input_command = input().split()

    if input_command[0] == 'analyze':
        pass

    elif input_command[0] == 'sales':
        pass

    elif input_command[0] == 'stock':
        if not products_list == []:
            with open('D:\\Testy\\products.txt', 'w') as output_file:
                for pr in products_list:
                    output_file.write(f'{pr.name} {pr.type} {pr.price} {pr.quantity}')
        else:
            print('No products stocked')

    elif input_command[0] == 'exit':
        pass

    else:
        if all(product for product in products_list
               if product.name != input_command[0] and product.type != input_command[1]):
            Product(*input_command)
        else:
            change = next(product for product in products_list
                          if (product.name == input_command[0]) and (product.type_ == input_command[1]))
            change.price = input_command[2]
            change.quantity = input_command[3]

        for product in products_list:
            if product.name == input_command[0] and product.type_ == input_command[1]:
                product.price = input_command[2]
                product.quantity = input_command[3]
