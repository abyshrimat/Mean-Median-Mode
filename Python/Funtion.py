def countWordsFromFile():
    fileName = input("enter the file name: ")
    file = open(fileName, 'r')
    
    numOfWords = 0

    for line in file: 
        word = line.split()
        numOfWords = numOfWords + len(words)

    print("numOfWords in the file: "+ numOfWords)

countWordsFromFile()