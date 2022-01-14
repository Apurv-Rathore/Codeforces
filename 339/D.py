import sys,os,io
from sys import stdin
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def powerof2(n):
    while n>1:
        if n%2:
            return False 
        n//=2
    return True

class SegmentTree:
    def __init__(self, data, default=0, func=lambda a,b:a+b):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        orl = False
        for i in range(self._size-1,0,-1):
            if powerof2(i+1):
                orl = orl ^ True
            # print(orl,i,self.data[i + i]  , self.data[i + i + 1])
            if orl:
                self.data[i] = (self.data[i + i]  | self.data[i + i + 1])
            else:
                self.data[i] = (self.data[i + i]  ^ self.data[i + i + 1])
        # print(self.data)
        
    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        orl = True
        # print(self.data)
        while idx:
            if orl:
                self.data[idx] = (self.data[2 * idx] |  self.data[2 * idx + 1])
            else:
                self.data[idx] = (self.data[2 * idx] ^  self.data[2 * idx + 1])
            idx >>= 1
            orl^= True
        # print(self.data)

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """Returns the result of function over the range (inclusive)! [start,stop]"""
        start += self._size
        stop += self._size+1

        res_left = res_right = self._default
        orl = True
        while start < stop:
            if start & 1:
                if orl:
                    res_left = (res_left | self.data[start])
                else:
                    res_left = (res_left ^ self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                if orl:
                    res_right = (self.data[stop] | res_right)
                else:
                    res_right = (self.data[stop] ^ res_right)
            start >>= 1
            stop >>= 1
            orl ^= True
        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
seg = SegmentTree(a)
for i in range(m):
    p,b = [int(x) for x in input().split()]
    seg.__setitem__(p-1,b)
    print(seg.data[1])