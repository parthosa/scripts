# create two folders papers and keys in your cwd
import random
import os
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for n in range(1,36):
    arg1=''
    arg2=''
    qn=1
    zoo=list(capitals.keys())
    random.shuffle(zoo)

    for i in zoo:
        arg1+=str(qn)+'\n'
        arg2+=str(qn)+' '
        qn+=1
        arg1+=i +'  ki capital?? \n'

        meow=[]

        while True:
            if len(meow)==3:
                break

            var=(list(capitals.values()))[random.randint(0,49)]
            if var!=capitals[i]:
                meow.append(var)

        meow.append(capitals[i])
        random.shuffle(meow)

        for m in range(len(meow)):
        	if m==0:
        		arg1+='a '+meow[m]+'\n'
        		if meow[m]==capitals[i]:
        			arg2+='a\n'
        	if m==1:
        		arg1+='b '+meow[m]+'\n'
        		if meow[m]==capitals[i]:
        			arg2+='b\n'
        	if m==2:
        		arg1+='c '+meow[m]+'\n'
        		if meow[m]==capitals[i]:
        			arg2+='c\n'
        	if m==3:
        		arg1+='d '+meow[m]+'\n'
        		if meow[m]==capitals[i]:
        			arg2+='d\n'







    os.chdir('./papers')
    s=str(n)
    f1=open("paper"+s,"w")
    f1.write(arg1) # write the questions
    f1.close()

    os.chdir('../keys')
    f2=open("key"+s,"w")
    f2.write(arg2)
    f2.close()
    os.chdir('../')
