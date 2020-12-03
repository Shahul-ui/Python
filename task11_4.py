numbers_list= [15, 8, 6, 3, 16, 11, 2, 25, 24, 21]
odd_list = []
def logic(i):
    if i % 2 == 0:
        return False
    else:
        return True
filter_list = filter(logic,numbers_list)
for number in filter_list:
    odd_list.append(number)
print(odd_list)
