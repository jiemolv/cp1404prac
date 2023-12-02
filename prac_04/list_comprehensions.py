

# TODO 1: Create a list of even numbers from 1 to 20 using list comprehension
even_numbers = [x for x in range(2, 21, 2)]
print(even_numbers)

# TODO 2: Create a list of squares of even numbers from 1 to 20 using list comprehension
squares_of_evens = [x**2 for x in range(2, 21, 2)]
print(squares_of_evens)

# TODO 3: Create a list of words with length 5 or less from a given sentence
sentence = "The quick brown fox jumps over the lazy dog"
short_words = [word for word in sentence.split() if len(word) <= 5]
print(short_words)
