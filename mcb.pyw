import pyperclip
import sys
import shelve
shelffile=shelve.open('data')
if sys.argv[1]=='list':
    for i in list(shelffile.keys()):
        print(i)

if sys.argv[1]=='save':
    shelffile[sys.argv[2]]=pyperclip.paste()

if sys.argv[1] in list(shelffile.keys()):
    pyperclip.copy(shelffile[sys.argv[1]])

shelffile.close()
