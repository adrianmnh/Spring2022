class LPS(object):
    def longestPalindrome(self, s):
        if s == "":
            return ""
        temp=0
        start,end=0,0
        for i in range(len(s)):
            len1 = self.expandFromMiddle(s,i,i)
            len2 = self.expandFromMiddle(s,i,i+1)
            currLen=max(len1,len2)
            if currLen > temp:
                temp=currLen
                start = i-((temp-1)//2)
                end = i + (temp//2) +1
        return s[start+1:end-1]
    
    def expandFromMiddle(self, s,start,end):
        while start>=0 and end<len(s) and s[start]==s[end]:
            start -= 1
            end += 1
        return end-start+1
    return longestPalindrome(s)
    

def myLP():
    s=sets()
    table=[[0]*len(s) for i in range(len(s))]
    arr=[0 for i in s]

    ## Length 1
    for i in range(len(table)):
        table[i][i]=1
        temp=s[i:i+1]

    ## Length 2
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            table[i][i+1]=1
            arr[i]=i+1

##    prin(table)

    ##Length > 2
    for j in range(2,len(s)):
        for i in range(len(s)):
##            j=i+k
            print(s[i:j+1], i, j)
            if j<len(s) and s[i]==s[j] and table[i+1][j-1]==1: 
                table[i][j]=1

##    for i in range(

##    for k in range(2,len(s)):
##        for i in range(



    for i in range(len(table)):
        for j in range(len(table[i])):
            if j>=i and table[i][j]==1:
                if len(s[i:j+1]) > len(temp):
                    temp=s[i:j+1]
                    start=i
                    end=j
    print(arr)
    prin(table)

    return temp, start, end

def myLP2():
    s=sets()
    if s == "":
        return ""
    result=""
    table=[0 for i in range(len(s))]

    for i in range(len(s)):
        for j in range(i+1):
            if i==j:
                table[j]=1
            elif i == j+1:
                table[j]=int(s[i]==s[j])
            else:
                table[j]=int(table[j+1] and s[i] == s[j])

    print(table)


def Sol3():
        s=sets()
        res = ""
        arr = [None for i in range(len(s))]
        for j in range(len(s)):
            print("max: ",j, arr)
            for i in range(j+1):
                print((i,j))
                if i == j:
                    print("if i==j arr[i]=1")
                    arr[i] = 1
                elif j == i+1:
                    print("if j==i+1, arr[i]= s(i) AND s(j)")
                    arr[i] = int(s[i] == s[j])
                else:
                    print("arr[i] = nexti AND s(i)==s(j)")
                    arr[i] = int(arr[i+1] and s[i] == s[j])
                    
                print(arr, s[i:j+1], sep=" ")

                
                if arr[i] and j - i + 1 >= len(res):
                    res = s[i:j+1]
                    print("%% arr[i]==1 AND s[i:j]>res =>", res)
        return res

##def Sol4():
##    s=sets()
##    table=[[0]*len(s) for i in range(len(s))]
##    for i in range(len(table)):
##        table[i][i]=1
##
##        for
def Solution4():
    def longestPalindrome(s):
        if s == '': 
            return s
##        max_len = 0 
        start, end = 0, 0
        for i in range(len(s)):
            len1 = expandFromCenter(s, i, i)
            len2 = expandFromCenter(s, i, i+1)
            l = max(len1, len2)
            print(l, start, end)
            if l > end - start:
                print(s[start:end+1])
                start = i - (l - 1) // 2
                end = i + l // 2

        return s[start:end+1]

    def expandFromCenter(s, idx1, idx2):
        print("EFC",(idx1, idx2))
        while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
            idx1 -= 1
            idx2 += 1
            print(idx1, idx2)
        print(idx2-idx1-1)
        return idx2 - idx1 - 1

    print(longestPalindrome(sets()))
    
##print(myLP())
##print(myLP2())
##print(Sol3())
##print(Sol4())
Solution4()
