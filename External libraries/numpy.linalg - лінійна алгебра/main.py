# -*- coding: utf-8 -*-
"""
# numpy.linalg - лінійна алгебра
Модуль містить базові інструменти лінійної алгебри: для декомпозиції матриць, розрахунку власних значень, визначника, норми матриці, розв'язування систем лінійних рівнянь та інвертування матриць. В прикладі також показано відмінність типів matrix і ndarray. Модуль `scipy.linalg` містить функції `numpy.linalg` та деякі додаткові функції, але може бути швидшим.
"""
import numpy as np
A = np.matrix([[3, 1], [1, 2]]) # матриця
print A*A # множення матриць

print np.linalg.det(A) # визначник матриці (якщо не 0, то існує обернена матриця до A)

W,V=np.linalg.eig(A) # власні значення і власні вектори
print W[0],V[:,0] # перше власне значення і відповідний власний вектор
print A*V[:,0] - W[0]*V[:,0] # перевірка A*V[:,i]=W[i]*V[:,i]

# розв'язування систем лінійних рівнянь AX=B (A,B - матриці)
A = np.matrix([[3, 1], [1, 2]]) # матриця
B = np.matrix([[9], [8]]) # матриця
X = np.linalg.solve(A, B) # розв'язати систему 
# X = A**(-1)*B # або шляхом інвертування матриці A
# A*X-B # перевірка (нульова матриця)
print X

# розв'язування систем лінійних рівнянь AX=B (A,B - масиви)
A = np.array([[3, 1], [1, 2]]) # масив
B = np.array([9, 8]) # масив
X = np.linalg.solve(A, B) # розв'язати систему
# X = np.linalg.inv(A).dot(B) # або шляхом інвертування матриці A
# np.dot(A, X) - B # перевірка (нульовий масив)
