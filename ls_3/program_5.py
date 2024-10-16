# Принимаем два слова от пользователя
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

if len(word1) != len(word2):
    print("Слова не являются анаграммами")
else:

    char_count1 = {}
    char_count2 = {}

    for char in word1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    for char in word2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    if char_count1 == char_count2:
        print("Слова являются анаграммами")
    else:
        print("Слова не являются анаграммами")