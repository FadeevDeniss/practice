def position(x):
    x = x[1]
    return x


f = str(open(r'war_and_peace.txt', 'r', encoding='utf-8').readlines())
for symbol in [',', '.', '!', ':', '"', 'n', '(', ')', '?']:
    f = f.replace(symbol, '')
list_of_numbers = []
for i in f.split():
    if len(i) < 5:
        continue
    if (i, f.count(i)) in list_of_numbers:
        continue
    list_of_numbers.append((i, f.count(i)))
for j in list_of_numbers:
    count = max(list_of_numbers, key=position(j))
    print(count)