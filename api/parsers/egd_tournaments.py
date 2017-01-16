file = open('all.hst')
# count = 0
tournament_list = set()
for line in file:
    if len(line.split()) == 11 and line.split()[3] == 'UA':
        # print(line.split())
        tournament_list.add(line.split()[6])
        # count += 1
    # if count > 5:
    #     file.close()
    #     break
print([line for line in tournament_list])