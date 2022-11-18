goods = [
    ['apple', 'pear', 'peach', 'chery'], 
    ['salak', 'mangustin'],
    ['mango', 'durian', 'breadfruit'],
    ['bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']
]

longest_words = [goods[0][0]]
longest_indexes = [[0, 0]]

for index, goods_list in enumerate(goods):
    for inner_index, good in enumerate(goods_list):
        good_len = len(good)
        longest_len = len(longest_words[-1])

        if good_len > longest_len:
            longest_words.clear()
            longest_indexes.clear()

            longest_words.append(good)
            longest_indexes.append([index, inner_index])

        elif good_len == longest_len:
            longest_words.append(good)
            longest_indexes.append([index, inner_index])
            
for index, word in enumerate(longest_words):
    print(f"{word} - (index: {longest_indexes[index][0]}, inner index: {longest_indexes[index][1]})")