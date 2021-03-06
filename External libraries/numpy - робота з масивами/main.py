# -*- coding: utf-8 -*-
"""
# numpy - робота з масивами
NumPy (http://www.numpy.org, http://scipy.org) – вільна бібліотека Python для високопродуктивних операцій з багатовимірними масивами (у тому чиcлі матрицями). NumPy є основою таких бібліотек для роботи з даними як SciPy, Matplotlib, pandas, scikit-learn та багатьох інших. Часто застосовується разом з бібліотекою SciPy, яка містить багато зручних і ефективних чисельних процедур (для інтегрування, оптимізації, інтерполяції, статистики, обробки сигналів та іншого). NumPy та SciPy можна розглядати як вільну альтернативу MATLAB. В прикладах використовується NumPy 1.13.3 та SciPy 0.19.1. В цьому прикладі показані базові операції з масивами: створення, властивості, доступ до частин масиву (зрізи), зміна форми, арифметичні операції, математичні функції, способи індексації, збереження у файлах, створення масивів з різнотипними елементами.
"""
import numpy as np
#print numpy.lookfor("create array") # шукати "create array" серед документації

# створення масивів:
np.array([1.0,2.0,3.0,4.0]) # одновимірний масив
np.array([1,2,3,4], dtype=int) # одновимірний масив цілих чисел
np.array([[1.0,2],[3,4]]) # двовимірний масив дійсних чисел
print np.array(range(6)) # одновимірний масив з прогресії
np.arange(6) # або так
print np.linspace(start=0,stop=10,num=5) # масив з рівномірно розподіленими значеннями
np.zeros((2,2)) # двовимірний нульовий масив
np.ones(2) # одновимірний масив з одиниць
np.full(2, 1) # або так
np.identity(2) # одинична матриця
np.random.random(5) # масив з випадковими значеннями
np.random.normal(loc=5, scale=1, size=5) # масив з випадковими значеннями (нормальний закон)

a=np.array([[1,2,3], [4,5,6]])
a.ndim # кількість вимірів масиву
a.shape # розмір кожного виміру
a.size # загальний розмір
a.dtype # тип даних
a.tolist() # перетворити у список

# зрізи над масивом у форматі: a[початок:кінець:крок]
print a[0,1], a[0][1], a[0], a[-1], a[:,0], a[0:2:2,0:3:2]
a[0,0]=1.2 #змінити елемент з індексами 0,0
#Увага! a[0,0]==1 бо масив цілого типу
a[0]=np.array([1,2,3]) #змінити рядок з індексом 0
a0=a[0] # це не окрема копія першого рядка масиву a
a0[0]=2 #Увага! Масив a зміниться!
a0=a[0].copy() # це окрема копія першого рядка масиву a

print a.reshape((3,2)) # повертає масив зі зміненою формою
a.shape=(3,2) # або змінити форму масиву
a.resize((3,3)) # змінити форму масиву і заповнити нові комірки нулями
a.transpose() # транспонувати (або a.T)
np.ones(2)[:, np.newaxis] # перетворити в вектор-стовпчик
np.ones(2).reshape((2,1)) # або так

np.concatenate([a, a]) # об'єднати масиви по вертикалі
np.vstack([a, a]) # або так
np.concatenate([a, a],axis=1) # об'єднати масиви по горизонталі
np.hstack([a, a]) # або так
np.split(a, [1]) # розбити масиви по вертикалі
#див. також np.vsplit, np.hsplit

# арифметичні операції над масивами
a+1 # додати 1 до кожного елемента
np.sqrt(a+1) # застосування математичних функцій
a+a # поелементне додавання
print np.array([1,2])+np.array([[1,2],[3,4]]) # додавання масивів різного розміру

np.sum(a) # сума елементів
np.sum(a, axis=0) # суми в стовпцях
np.add.reduce(a, axis=0) # або так
np.cumsum(a) # накопичувальна сума
np.mean(a) # середнє
np.std(a) # стандартне відхилення
np.min(a), np.max(a) # мінімальне, максимальне
np.argmin(a) # індекс найменшого елемента
np.sort(np.array([3,2,7,1])) # сортувати
print np.argsort(np.array([3,2,7,1])) # індекси для сортування

a=np.array([1,2,3,4])
a[[1,2]] # масив елементів з індексами 1,2
a[np.array([1,2])] # або так
a[[1,2]]=[2,3] # можна також змінювати масив `a`
a[np.array([False, True, True, False])] # або так
np.array([[1,2],[4,5]])[1,[0,1]] # комбінована індексація

b=a<4 # масив з результатами логічного виразу (dtype=bool)
b=(a > 2) & (a < 4) #або складні логічні вирази
a[b] # масив елементів з індексами b
print np.where(a<4) # масив індексів, де виконується умова
np.any(a<4) # чи будь-який елемент 
np.all(a<4) # чи усі елементи

# збереження у файлах
#a.tofile("myfile") # зберегти у файл
#a=np.fromfile("myfile", dtype=int) # прочитати з файлу
# або
#np.save("myfile.npy",a) # зберегти у файл
#a=np.load("myfile.npy") # прочитати з файлу

a = np.zeros(2, dtype=('i4,f4,a10')) # масив з різними типами
a[0]=(1, 10.0, 'A') # перший елемент
a[1]=(2, 20.0, 'B') # другий елемент
# або
a = np.zeros(2, dtype={'names':('i','x','name'),'formats':('i4','f4','a10')})
a[0]=(1, 10.0, 'A') # перший елемент
a[1]=(2, 20.0, 'B') # другий елемент
a['name'] # стовпчик 'name'
a['name']=['a','b'] # змінити значення стовпчика
print a
print a[a['x'] < 20] # ті елементи, де x<20
