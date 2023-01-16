n = input()
print(f'Сумма цифр = {sum(int(i) for i in n)}')
proz = 1
for i in n:
    proz = int(i) * proz
print(f'Произведение цифр = {proz}')
