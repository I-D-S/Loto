import random
import logging

logging.basicConfig(filename='loto_log.log', level=logging.INFO)

while True:
    try:
        n = int(input("Введите натуральное число: "))
        assert n > 0
        logging.info('correct number input, n = {}'.format(n))
        break
    except AssertionError:
        print('Число должно быть натуральным !')
        logging.exception("num isn't natural")
    except ValueError:
        print('Неверный ввод')
        logging.exception('wrong num input')
num_list = [i for i in range(1, n + 1)]
random.shuffle(num_list)
print('Нажмите Enter чтобы увидеть число', end='')
for element in num_list:
    a = input()
    print(element, end='')
