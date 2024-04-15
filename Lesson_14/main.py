file_path = 'products.txt'

def get_products():
    with open(file_path, mode='r', encoding='utf8') as file:
        return file.read().split('\n')

def save_products(products_list):
    with open(file_path, mode='w', encoding='utf8') as file:
        file.write('\n'.join(products_list))

while True:
    print('1. Переглянути')
    print('2. Додати')
    print('3. Видалити')
    print('0. Вихід')

    action = input('Оберіть дію:')
    if action == '1':
        print('Список продуктів:')
        for product in get_products():
            print(f' - {product}')
        input('Натисніть Enter, щоб продовжити')
    elif action == '2':
        new_product = input('Введіть назву продукту, який хочете додати:')
        products = get_products()
        products.append(new_product)
        save_products(products)
    elif action == '3':
        print('Список продуктів:')
        for index, product in enumerate(get_products()):
            print(f'{index}. {product}')
        product_index = int(input('Введіть індекс продукту, який треба видалити:'))
        products = get_products()
        products.pop(product_index)
        save_products(products)
    elif action == '0':
        break


'''
    Зробити програму, яка дозволяє додавати, переглядати
    та видаляти записи у файлі. 
    
    В програмі має бути користувацьке меню. Наприклад:
    1. Переглянути записи
    2. Додадати запис
    3. Видалити запис
    0. Вихід
'''



