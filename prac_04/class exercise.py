texts="?name=Bob&age=99&day=Wed"
texts =texts[1:].split("&")
print(texts)
words = []
for i in range(len(texts)):
    tuple_words = (tuple(texts[i].split("=")))
    print(tuple_words)
    words.append(tuple(tuple_words))

print(words)