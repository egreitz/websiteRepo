import time
from pathlib import Path

#file paths
p = Path(r'C:\Users\Eva\Desktop\website\test\example.txt')

bp = Path(r'C:/backups/backup.txt')

#main program loop
while True :

    date = time.ctime()
    print(date)
    print()
    print('book')
    book = input('>')
    book = f'book: {book}'
    print()
    print('music')
    music = input('>')
    music = f'music: {music}'

    #update file
    file_ = open(p, 'a')
    file_.write(f'\n{date}\n{book}\n{music}')
    file_.close()

    #update backup
    backup = open(bp, 'a')
    backup.write(f'\n{date}\n{book}\n{music}')
    backup.close()

    input('>')




