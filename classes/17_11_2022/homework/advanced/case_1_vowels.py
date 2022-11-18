goods = [
    ['apple', 'pear', 'peach', 'chery'], 
    ['salak', 'mangustin'],
    ['mango', 'durian', 'breadfruit'],
    ['bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']
]

longest_words = [goods[0][0]]

for goods_list in goods:
    for good in goods_list:
        good_len = len(good)
        longest_len = len(longest_words[-1])

        if good_len > longest_len:
            longest_words.clear()
            longest_words.append(good)

        elif good_len == longest_len:
            longest_words.append(good)

for word in longest_words:
    vowels_count = 0

    for char in word:
        if char in ['e', 'y', 'u', 'i', 'o', 'a']:
            vowels_count += 1

    print(f"{word} - vowels: {vowels_count}")