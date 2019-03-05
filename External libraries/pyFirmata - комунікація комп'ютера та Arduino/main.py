# -*- coding: utf-8 -*-
"""
# pyFirmata - комунікація комп'ютера та Arduino
Arduino (www.arduino.cc)- відкрита і зручна у використанні платформа, яка основана на одноплатному мікроконтроллері Atmel AVR і використовується аматорами для побудови простих систем автоматики і робототехніки. Firmata (http://firmata.org) це загальний протокол для зв'язку мікроконтроллерів з головним комп'ютером. Firmata дозволяє експериментувати з Arduino без необхідності його перепрограмовування кожного разу. В прикладі використано плату Arduino UNO для вимірювання значень температури за допомогою терморезистора і виведення їх на графік у реальному часі.

Передусім установіть драйвер USB-SERIAL для Arduino. В цьому прикладі це CH340 (http://www.wch.cn/download/CH341SER_ZIP.html). Розпакуйте на комп'ютер середовище Arduino IDE. У файлі /avr/boards.txt перевірте швидкість передачі даних uno.upload.speed=57600. Під'єднайте датчик температури (терморезистор) до контактів GND, ANALOG IN 0, 5V (рис.). Під'єднайте світлодіод до контактів GND і DIGITAL 13. Під'єднайте Arduino до USB-порту комп'ютера. В гілці "порти" диспетчера пристроїв знайдіть USB-SERIAL CH340 (COM9), де COM9 - назва послідовного порту. У вас номер може бути інший. З Arduino IDE завантажте в пам'ять мікроконтроллера приклад Firmata/StandardFirmata. Установіть на комп'ютері pyFirmata (https://github.com/tino/pyFirmata) і запустіть наступний приклад.

![](fig1.png)

Рисунок - Під'єднання датчика температури
"""
import matplotlib.pyplot as plt
import time
from pyfirmata import Arduino, util
board = Arduino('COM9') # з'єднати Arduino з портом COM9
it = util.Iterator(board); it.start() # для використання аналогових портів
board.analog[0].enable_reporting()
X=[] # список зі значеннями температури
plt.ion() # інтерактивна побудова графіка
while len(X)<30: # поки довжина списку мала
    time.sleep(1) # затримка 1 с
    x=board.analog[0].read() # читати значення з аналогового входу 0
    print x
    X.append(x) # додати в список
    plt.plot(X,'ko-'); plt.draw() # рисувати графік (plt.clf() - очистити)
    if x>0.35: # якщо температура висока
        board.digital[13].write(1) # включити світлодіод
    else:
        board.digital[13].write(0) # виключити світлодіод
board.exit() # вийти
"""

![](fig2.png)

Рисунок - Графік температури
"""
