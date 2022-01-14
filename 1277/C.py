t = int(input())
for _ in range(t):
    s = input()
    s = 't*o'.join('o*e'.join('tw*ne'.join(s.split('twone')).split('one')).split('two'))
    l = [str(i+1) for i in range(len(s)) if s[i] == '*']
    print(len(l))
    print(' '.join(l))