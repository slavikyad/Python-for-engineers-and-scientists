# -*- coding: utf-8 -*-
"""
# Dask - розподілені обчислення на чистій Python
Dask 0.18.2 (http://dask.pydata.org) - це гнучка бібліотека для паралельних обчислень. Dask забезпечує динамічне планування задач, оптимізоване для інтерактивних обчислювальних навантажень, та прості шляхи масштабування задач Pandas, Scikit-Learn і Numpy. Дозволяє легко паралелізувати довільний Python-алгоритм шляхом створення "лінивих" функцій з відкладеним виконанням. Функція `dask.delayed`  обгортає довільну функцію так, що вона не виконується миттєво, а створює граф задач. Передача відкладених результатів іншим відкладеним функціям створює залежності між задачами. Обчислити результати паралельно можна за допомогою методу `compute`. Нижче наведено приклад алгоритму, який паралелізується. Для виконання прикладу на кластері див. приклад Dask.Distributed.
"""
from dask.distributed import Client
from dask import delayed
import time
def f(x): # функція, яка буде виконуватись в окремих процесах
    time.sleep(x)
    return x
if __name__ == '__main__':
    #client = Client() # клієнт (кластер на локальній машині)
    client = Client('192.168.1.33:8786') # клієнт
    res=[]
    for x in [1,2,3,4]:
        f_ = delayed(f)(x) # відкладене виконання функції f
        res.append(f_) # додати відкладений результат в список
    sum_=delayed(sum)(res) # відкладене виконання функції sum
    print sum_.compute() # обчислити f(1),f(2),f(3),f(4) паралельно, а потім обчислити їх суму
"""
    10
"""
