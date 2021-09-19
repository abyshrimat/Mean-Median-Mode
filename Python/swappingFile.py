sample1.txt
sample2.txt

def swapFileData():

    fileName = input("This is a text from: ")

    file1 = data_a
    file2 = data_b

with open (file1, 'r') as a:
data_a = a.read()

with open (file1, 'w') as a:
a.write(data_b)

swapFileData()