# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
print('Пункт A.')
random_songs = []
random_songs.append(my_favorite_songs[0][1])
random_songs.append(my_favorite_songs[3][1])
random_songs.append(my_favorite_songs[-1][1])
#print(random_songs)
time_songs_sec = 0
for i in random_songs:
    minutes_in_sec = int(i) * 60
    seconds = round((i - int(i)) * 100)
    time_songs_sec += minutes_in_sec + seconds
all_time_minutes = int(time_songs_sec // 60) + int(time_songs_sec % 60) / 100
print(f'Три песни звучат {round(all_time_minutes,2)} минут')



# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

print('Пункт B.')
random_songs = []
random_songs.append(my_favorite_songs_dict['Waste a Moment'])
random_songs.append(my_favorite_songs_dict['A Sorta Fairytale'])
random_songs.append(my_favorite_songs_dict['Nowhere to Run'])
#print(random_songs)
time_songs_sec = 0
for i in random_songs:
    minutes_in_sec = int(i) * 60
    seconds = round((i - int(i)) * 100)
    time_songs_sec += minutes_in_sec + seconds
all_time_minutes = int(time_songs_sec // 60) + int(time_songs_sec % 60) / 100
print(f'Три песни звучат {round(all_time_minutes,2)} минут')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
#import random

print('Пункт C.')
import random
random_songs = random.choices(my_favorite_songs, k=3)
#print(random_songs)
time_songs_sec = 0
for i in random_songs:
    minutes_in_sec = int(i[1]) * 60
    seconds = round((i[1] - int(i[1])) * 100)
    time_songs_sec += minutes_in_sec + seconds
all_time_minutes = int(time_songs_sec // 60) + int(time_songs_sec % 60) /100
print(f'Три песни звучат {round(all_time_minutes,2)} минут')


random_songs = random.choices(list(my_favorite_songs_dict.values()), k=3)
#print(random_songs)
time_songs_sec = 0
for i in random_songs:
    minutes_in_sec = int(i) * 60
    seconds = round((i - int(i)) * 100)
    time_songs_sec += minutes_in_sec + seconds
all_time_minutes = int(time_songs_sec // 60) + int(time_songs_sec % 60) /100
print(f'Три песни звучат {round(all_time_minutes,2)} минут')

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

print('Пункт D.')
import datetime
random_songs = random.choices(list(my_favorite_songs_dict.values()), k=3)
#print(random_songs)
time_songs_sec = 0
for i in random_songs:
    time_songs_sec += (int(i) * 60) + round((i - int(i)) * 100)
time_songs = datetime.timedelta(seconds=time_songs_sec)
print(f'Три песни звучат {time_songs} минут')