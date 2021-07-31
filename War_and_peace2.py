# Here a wrote a program, that calculate top 10 most popular words in roman "War and peace",
# by the Russian author Leo Tolstoy:

with open('war_and_peace.txt', 'r+t', encoding='utf-8') as f:
    dict_of_nums = {}
    while True:
        line = f.readline()
        if not line:
            break
