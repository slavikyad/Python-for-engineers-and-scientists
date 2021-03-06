# -*- coding: utf-8 -*-
"""
# scipy.integrate - інтегрування
Модуль `scipy.integrate` містить функції для інтегрування, у тому числі для інтегрування звичайних диференціальних рівнянь. В прикладі дано функцію $y=x^2$. Розраховується визначений інтеграл

$$\int_{-3}^{3}ydx$$.
"""
import numpy as np
from scipy.integrate import quad
f = lambda x,a: x**a # функція
print quad(f, -3, 3, args=(2,)) # результат інтегрування і оцінка абсолютної похибки результату
x=np.array([-3,-2,-1,0,1,2,3])
print np.trapz(f(x,2),x) # інтегрувати задану масивом функцію методом трапецій
