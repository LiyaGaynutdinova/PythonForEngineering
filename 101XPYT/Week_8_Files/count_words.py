import string

def count_words(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            # Remove punctuation and convert to lowercase
            line = line.translate(str.maketrans('', '', string.punctuation))
            line = line.lower()

            # Split the line into words
            words = line.split()

            # Count the occurrences of each word
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

    return word_count

def print_word_count(word_count):
    print("Word Count:")
    print("---------------")
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Test the solution
file_path = "sample.txt"
word_count = count_words(file_path)
print_word_count(word_count)