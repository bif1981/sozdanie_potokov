# Домашнее задание по теме "Создание потоков".
# Цель задания:
#
# Освоить механизмы создания потоков в Python.
# Практически применить знания, создав и запустив несколько потоков.
#
# Задание:
# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.
#
# Примечание:
# Используйте методы: start() для старта потока, join() для заморозки дальнейшей интерпретации, пока процессы не завершаться.
# Для установки интервала в 1 секунду используйте функцию sleep() из модуля time, предварительно импортировав его.
#
#
# Входные данные:
# Нет
# Выходные данные:
# 1
# a
# 2
# b
# 3
# c
# ......
# 10
# j

# Создать и запустить поток
import random
import time
from collections import defaultdict
from threading import Thread

def chisla(n):
    catch = defaultdict(int)
    for i in range(1, 11):
        print(f'{i}', flush=True)  # flush - небуферизованный вывод
        time.sleep(1)


def bukvy(element):
    catch = defaultdict(int)
    for number in range(ord("a"), ord("j") + 1):
        print(chr(number), flush=True)
        time.sleep(1)

#chisla_catch = defaultdict(int)
thread1 = Thread(target=chisla, args = (10,)) #catch=chisla_catch)

#bukvy_catch = defaultdict(int)
thread2 = Thread(target=bukvy, args = (10,)) #catch=bukvy_catch)

thread1.start()
thread2.start()
thread1.join()
thread2.join()



# Пример из лекции
# FISH = (None, 'плотва', 'окунь', 'лещ')
#
#
# # Определим функцию, эмулирующую рыбалку
#
# def fishing(name, worms, catch):  # Имя рыбака, черви
#     #catch = defaultdict(int)  # catch - это его улов
#     for worm in range(worms):
#         print(f'{name}: Червяк № {worm + 1} - Забросил, ждем...', flush=True)  # flush - небуферизованный вывод
#         _ = 3 ** (random.randint(50, 70) * 10000)
#         fish = random.choice(FISH)
#         if fish is None:
#             print(f'{name}: Тьфу, сожрали червяка...', flush=True)
#         else:
#             print(f'{name}: Ага, у меня {fish}', flush=True)
#             catch[fish] += 1
#
#
#
# # fishing('Вася', worms=10)
#
# # А теперь создадим второго рыбака, пошедшего на рыбалку ОДНОВРЕМЕННО с первым
# vasya_catch = defaultdict(int)
# thread = Thread(target=fishing, kwargs=dict(name='Вася', worms=10, catch=vasya_catch))
# thread.start()
#
# kolya_catch = defaultdict(int)
# fishing(name='Коля', worms=10, catch=kolya_catch)
#
# thread.join()
#
# for name, catch in (('Вася', vasya_catch), ('Коля', kolya_catch)):
#     print(f'Итого: рыбак {name} поймал:', flush=True)
#     for fish, count in catch.items():
#         print(f'   {fish} - {count}', flush=True)
