fob=open('C:\PythonAssigment1\DictionaryFile.txt','r')
listme=fob.readlines()

dayOfTheWeek = input('please enter day name you want to: ')

d = {}
for line in listme:
    (key, val) = line.split()
    d[key] = val
    if (key == dayOfTheWeek):
        print(dayOfTheWeek + " in dutch is " + d[key])
fob.close()