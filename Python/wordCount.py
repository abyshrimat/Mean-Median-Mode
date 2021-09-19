intro = input("enter about yourself: ")
characterCount = 0
wordCount = 1
for i in intro: 
    characterCount = characterCount + 1
    if(i==' '):
        wordCount = wordCount + 1
print("number of words: ")
print(wordCount)
print("number of characters in intro")
print(characterCount)
