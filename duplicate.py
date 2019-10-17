class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def duplicate(A):
        for i in A:
            count = 0
            for j in range(0,len(A)):
                if(A[j]==i):
                    count +=1