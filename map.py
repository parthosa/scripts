import webbrowser,sys,pyperclip

s1='https://www.google.com/maps/place/'

if len (sys.argv)<=1:
    s2=pyperclip.paste()
    s2m=''
    for i in s2:
        if i==' ':
            s2m+='+'
        else:
            s2m+=i
    s2=s2m

else:
    s2=''
    for i in range(1,len(sys.argv)):
        s2+=sys.argv[i]
        s2+='+'
    s2=s2[0:-1]

webbrowser.open(s1+s2)
