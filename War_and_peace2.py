# Here a wrote a program, that calculate top 10 most popular words in roman "War and peace",
# by the Russian author Leo Tolstoy:

with open('war_and_peace.txt', 'r+t', encoding='utf-8') as f:
    dict_of_nums = {}
    while True:
        line = f.readline()
        if not line:
            break
        for symbol in ['!', '?', '.', ',', '"', ':', ')', '(']:
            line = line.replace(symbol, '')
        for i in line.split():
            if len(i) <= 5:  # Condition that allows us to pass words, which length are lower or equal 5 symbols
                continue
            elif i in dict_of_nums:
                dict_of_nums[i] += 1
            else:
                dict_of_nums[i] = 1
        for j in range(1, 11, 1):
            x = max(dict_of_nums, key=lambda k: dict_of_nums[k])
            print(j, 'место:', 'слово', x, dict_of_nums.get(x), 'раз встречается в тексте')
            dict_of_nums.pop(x)


# 1 место:  слово строка 3438 раз встречается в тексте
# 2 место:  слово Вместо 2874 раз встречается в тексте
# 3 место:  слово сказал 2216 раз встречается в тексте
# 4 место:  слово только 1586 раз встречается в тексте
# 5 место:  слово князь 1082 раз встречается в тексте
# 6 место:  слово Андрей 952 раз встречается в тексте
# 7 место:  слово Наташа 880 раз встречается в тексте
# 8 место:  слово когда 868 раз встречается в тексте
# 9 место:  слово теперь 862 раз встречается в тексте
# 10 место:  слово этого 826 раз встречается в тексте