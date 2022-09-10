import re

num = int(input())
pattern = r'^[7-9]\d{9}$'

for i in range(num):
    if bool(re.search(pattern, input())) == True:
        print('YES')
    else:
        print('NO')

#
# OR
#
# num = input()
# for num[0] in ("789"):
#     print("Yes")
# else:
#     print("No")
#

