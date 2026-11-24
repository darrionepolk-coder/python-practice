def main():
    # Read the words from the text file.
    infile = open("words.txt", "r")

    words = infile.read().lower().split()
    infile.close()

    # Remove common punctuation from the beginning and end of each word.
    cleaned_words = []
    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")
        if word != "":
            cleaned_words.append(word)

    # Count each word with a dictionary.
    word_counts = {}
    for word in cleaned_words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # A set contains each word only once.
    unique_words = set(cleaned_words)

    print("Word Count Results")
    print("------------------")
    for word in unique_words:
        print(word + ":", word_counts[word])

    print("\nTotal words:", len(cleaned_words))
    print("Unique words:", len(unique_words))


if __name__ == "__main__":
    main()
