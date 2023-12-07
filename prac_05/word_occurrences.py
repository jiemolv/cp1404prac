def count_words(text):
    """Count the occurrences of words in a string"""
    word_counts = {}

    # Split text into words
    words = text.split()

    # Count the occurrences of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def main():
    # Ask user for input text
    text = input("Text: ")

    # Count word occurrences
    word_counts = count_words(text)

    # Find the length of the longest word for formatting
    max_word_length = max(len(word) for word in word_counts)

    # Print the word counts in sorted order
    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_length}} : {count}")


if __name__ == "__main__":
    main()
