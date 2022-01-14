import string
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    openn=0
    close=0
    wrong=0
    for i in s:
        if i=="(":
            openn+=1
        elif i==")":
            close+=1
        if close>openn:
            wrong+=close-openn
            openn=0
            close=0
        if close==openn:
            openn=0
            close=0
    print(wrong)
            