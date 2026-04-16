a = int(input('Введи А <<< '))
b = int(input('Введи B <<< '))
casio = input('Введи операцию <<< ')

if casio == '+':
    print(a+b)
elif casio == '-':
    print(a-b)
elif casio == '*':
    print(a*b)
elif casio == '/':
    print(a/b)
elif casio == '%':
    print(a%b)
elif casio == '//':
    print(a//b)
    #
    # 80/10 = 8(0)
    # 76/10 = 7(6) %=6 //=7
    #
