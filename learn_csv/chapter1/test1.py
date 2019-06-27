import csv
from collections import Iterator, Generator

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
print(isinstance(exampleReader, Generator))
print(isinstance(exampleReader, Iterator))
print(exampleReader)
# for i in exampleReader:
#     print(i)
#     print(type(i))
# exampleData = list(exampleReader)
# print(exampleData)

