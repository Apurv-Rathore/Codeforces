for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    v,s,d=min(a)*max(a),set(),2
    while d*d<=v:
        if not v%d:
            s.add(d)
            s.add(v/d)
        d+=1
    print(v if s==set(a) else -1)