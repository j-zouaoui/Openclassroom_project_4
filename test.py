mylist = [['ali 1  taleb', 2.0, 1250] ]
mysecondlist = [['ali 2  taleb', 1.0, 1380], ['ali 3  taleb', 2.0, 150]]

data = mylist + mysecondlist
print(data)
for item in data:
    item.remove(2)
print(data)
print(mylist)