"""
    Option 1
"""

text = input("Enter text: ")
text_words_list = text.split(" ")
print(text_words_list)

text_words_count = len(text_words_list)
text_chars_count = len(text)
text_non_whitespace_chars = len("".join(text_words_list))

text_vowels_count = 0

text_vowels_count += text.count("a")
text_vowels_count += text.count("e")
text_vowels_count += text.count("i")
text_vowels_count += text.count("o")
text_vowels_count += text.count("u")
text_vowels_count += text.count("y")

print(f"Words count: {text_words_count}")
print(f"Chars count: {text_chars_count}")
print(f"Non-whitespace chars: {text_non_whitespace_chars}")
print(f"Vowels count: {text_vowels_count}")

"""
    Option 2
"""
string = input("Enter text: ")
string_words_count = 0
string_chars_count = 0
string_non_whitespace_chars = 0
string_vowels_count = 0

for char in string:
    string_chars_count += 1
    
    if char == ' ':
        string_words_count += 1
    else:
        string_non_whitespace_chars += 1

        if char in ['a', 'e', 'i', 'o', 'u', 'y']:
            string_vowels_count += 1

print(f"""
        Words: {string_words_count}
        Chars: {string_chars_count}
        Non-whitespace chars: {string_non_whitespace_chars}
        Vowels: {string_vowels_count}
    """)
