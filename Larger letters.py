def solve(n, string):
    result = "-1"
    # Write your code here
        
    for j in range(0,n):
        count=0
        for k in range(0,n):
            if (string[j] < string[k]):
                count = count+1
                if (result == "-1"):
                    result = " "
        result += str(count) + " "
    print(result)

n = int(input())
string = input()
solve(n, string)
