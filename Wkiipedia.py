import wikipedia
word=str(input())
page=wikipedia.summary(word)
print(page)