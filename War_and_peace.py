f = str(open(r'war_and_peace.txt', 'r', encoding='utf-8').readlines())
for symbol in [',', '.', '!', ':', '"']:
    f = f.replace(symbol, '')
f = f.split()
for i in f:
    if len(i) < 5:
        continue



