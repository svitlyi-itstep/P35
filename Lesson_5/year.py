year = int(input('Year:'))

if not year % 400:
    print('Високосний')
elif not year % 100:
    print('Не високосний')
elif not year % 4:
    print('Високосний')
