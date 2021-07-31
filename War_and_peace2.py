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
