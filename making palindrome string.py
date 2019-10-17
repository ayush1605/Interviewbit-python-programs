class Solution:
    # @param A : string
    # @return an integer
    def solve(A):
        x = int(len(A)/2)
        i = 0
        y = len(A)
        new_string = ""
        count = 0
        while i <= x:
            if(A[i] != A[y-1]):
                if (i == y-1):
                    return (count)
                else:
                    new_string = new_string + A[y-1]
                    count = count + 1
                    y=y-1
            elif (A[i] == A[y-1]):
                if (i == y-1):
                    return (count)
                else:
                    i = i + 1
                    y = y - 1

    print(solve ("pggxrpnrvystmwcysyy"))

