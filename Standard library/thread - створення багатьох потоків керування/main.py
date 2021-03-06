# -*- coding: utf-8 -*-
"""
# thread - створення багатьох потоків керування
Потоком виконання називають частину процесу, яка може виконуватись паралельно з іншими потоками цього процесу і використовувати спільні з ними ресурси. Синхронізація потоків і процесів - це механізм, який перешкоджає одночасному їх зверненню до спільно використовуваних ресурсів. Модуль `thread` забезпечує низькорівневі (на відміну від `threading`) примітиви для роботи з багатьма потоками. В прикладі створюються 4 потоки, які виконують функцію `f`. Звернення потоків до спільного списку `A` синхронізовано за допомогою простого об'єкта блокування `allocate_lock`. Нижче показані результати роботи програми з цим об'єктом і без нього. Зауважте, що в CPython існує глобальне блокування інтерпретатора Global Interpreter Lock (GIL), яке являє собою механізм синхронізації потоків, що не дозволяє в один момент часу виконуватись більше ніж одному потоку. Тому застосовуйте модуль `multiprocessing`, якщо програмі потрібно задіяти для обчислень кілька процесорів. А багатопотоковість краще застосовувати у випадку багатьох одночасних задач введення-виведення.
"""
import thread,time

def f(i): # функція виконується в окремому потоці
    mutex.acquire() # блокувати (лише один потік може виконуватись в один і той самий момент часу)
    A.append(i)
    time.sleep(1)
    A.append(i)
    mutex.release() # розблокувати
    T[i]=1 # повідомити головному потоку, що потік завершився
A=[] # глобальний список
T=[0,0,0,0] # глобальний список (якщо потік `i` завершився, то T[i]=1)
mutex = thread.allocate_lock() # створити блокуючий об'єкт
for i in range(4): # створити 4 потоки
    thread.start_new(f, (i, )) # стартувати потік 'i'
while 0 in T: # поки усі потоки не приєднаються
    pass # тут головний потік може робити щось своє
print A
