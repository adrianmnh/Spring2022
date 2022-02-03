def prin(a):
    for i in range(len(a)):
        print(f'{i:3d} - [ ', end="")
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print(" ]")

def prina(a):
    print()
    for i in range(len(a)):
        print(f'{i:3d}', end="")
    print()
    for i in range(len(a)):
        print(f'{a[i]:3d}', end="")
    print()

def sets():
    print()
    s="xxfgfxaja"
##    s="babad"
    for i in range(len(s)):
        print(f'{i:>3d}', end="")
    print()
    for i in range(len(s)):
        print(f'{s[i]:>3s}', end="")
    print()

    return s
        
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
        dp = [None for i in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                print(j,i)
                if i == j:
                    dp[i] = 1
                elif j == i+1:
                    dp[i] = int(s[i] == s[j])
                else:
                    dp[i] = int(dp[i+1] and s[i] == s[j])

                print(dp, s[i:j+1])
                if dp[i] and j - i + 1 >= len(res):
                    res = s[i:j+1]
                    print(res)
        return res
##print(myLP())
##print(myLP2())
print(Sol3())

