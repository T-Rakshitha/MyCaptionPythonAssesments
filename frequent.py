def most_frequent(string):
    d = dict()
    for letter in string:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1

    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    for key, value in sorted_dict.items():
        print(key, "=", value)


string = "Mississippi"
most_frequent(string)