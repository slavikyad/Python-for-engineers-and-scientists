# -*- coding: utf-8 -*-
"""
# Файли
Файл - це інформаційний об'єкт, який містить послідовність байтів і розміщений у файловій системі на носію інформації. Усі файли є бінарними, але якщо для файлу застосовується кодування символів (ASCII, UTF-8, CP1251 або інше), то його називають текстовим. Наприклад файл з кодом Python програми (.py) є текстовим. В бінарних файлах кодування символів не застосовується. Для роботи з файлом його відкривають функцією `open`, яка створює файловий об'єкт, що має методи запису, читання і закриття файлу.
"""
f1=open("file1.txt", "w") # відкрити текстовий файл для запису
f1.write("Line1\n") # записати рядок ('\n' - символ кінця рядка)
f1.close() # закрити файл

f2=open("file1.txt", "a") # відкрити текстовий файл для добавлення
f2.writelines(("Line2\n","Line3\n")) # записати послідовність рядків
f2.close() # закрити файл

f3=open("file1.txt", "r+") # відкрити текстовий файл для читання і запису
print f3.read() # читати весь файл
f3.seek(0) # установити позицію на початок файлу
print f3.readline(),f3.tell() # читати рядок, вивести поточну позицію
print f3.readlines() # читати список рядків до кінця
f3.seek(0) # установити позицію на початок файлу
for line in f3: # для кожного рядку у файлі
    pass # виконати пусту команду
f3.close() # закрити файл

f4=open("file1.txt", "rb") # відкрити бінарний файл для читання
# спробуйте також відкрити цей файл як текстовий "r"
f4.seek(7) # установити позицію після байта 7
while True: # читає файл побайтово
    b=f4.read(1) # читати байт
    if not b: break # перервати цикл, якщо байтів немає
    print ord(b), # числове подання Юнікод-символу
#зверніть увагу на два байти (13 10), які в текстових файлах Windows використовуються для позначення кінця рядка
f4.close() # закрити файл
