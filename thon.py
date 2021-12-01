valor = count = resu =  0
while True:
    print('-' * 35)
    valor = int(input('Quer ver tabuada de qual valor? (0 para encerrar) '))
    print('-' * 35)
    if valor == 0:
        break
    count += 1
    for count in range(1, 11):
        resu = valor * count
        print(f'{valor} x {count} = {resu}')
print('PROGRAMA TABUADA ENCERRADO. \033[0;32mVolte sempre!\033[m')
print('-' * 35)