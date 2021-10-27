word = input()

count_dict = {}
for ch in word.upper():
    count_dict[ch] = count_dict.get(ch, 0) + 1

count_list = sorted(list(count_dict.items()), key=lambda x:x[1], reverse=True)

if len(count_list)>=2 and count_list[0][1] == count_list[1][1]:
    print('?')
else:
    print(count_list[0][0])