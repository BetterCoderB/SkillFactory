summ = 0.00
many_bilet = int(input('Введите количество билетов '))
for k in list(range(0, many_bilet)):
    pass
    print('Введите возраст посетителя №', k+1,end=' ')
    age = int(input())
    if (age >= 18) and (age < 25):
        summ = summ + 990
    elif age >= 25:
        summ = summ + 1390
if many_bilet >=4:
    print('сумма к оплате: ',round(summ*90/100,2),'руб.')
else:
    print('сумма к оплате: ',round(summ,2),'руб.')