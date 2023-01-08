per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('money = '))
deposit = list(map(lambda num: num * money /100, list(per_cent.values())))
print(deposit,"\nМаксимальная сумма, которую вы можете заработать —",sorted(deposit)[-1])
