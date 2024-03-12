inf = open ('Elka.txt', 'r')
f = inf.readlines()
# список из всех строк файла
print (f)
print (len(f), ' - число строк в файле')
for i in f:
    print (i.count(' ')+1, 'число слов в строке')
    print (len(i), 'число символов в строке')
inf.close
