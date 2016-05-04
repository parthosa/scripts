import webbrowser,sys

a='https://www.google.co.in/?ion=1&espv=2#q='
b='+'.join(sys.argv[1:])
url=a+b+'+weather'
webbrowser.open(url)
