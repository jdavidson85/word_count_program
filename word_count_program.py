with open('tale_of_two_cities.txt', 'r') as file:
    word_count = {}

    for line in file:
        words = line.strip().split()

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    print("Unique words in the file:")
    for word, count in word_count.items():
        if count == 1:
            print(word)
