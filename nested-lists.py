#https://www.hackerrank.com/challenges/nested-list/

score_list = []
name_list = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        name_list.append(name)
        score = float(input())
        score_list.append(score)

min_value = min(score_list)

while min_value in score_list:
    index = score_list.index(min_value)
    del score_list[index]
    del name_list[index]

second_min = min(score_list)

final_name_list = []

while second_min in score_list:
    min_index = score_list.index(second_min)
    final_name_list.append(name_list[min_index])
    del score_list[min_index]
    del name_list[min_index]

for eachName in sorted(final_name_list):
    print(eachName)
