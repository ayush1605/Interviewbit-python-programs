class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(A):
        sum = 0
        subarray = []

        for i in range(len(A)):
            for j in range(i+1,len(A)):
                sum = abs(A[i] - A[j]) + abs(i - j)
                subarray.append(sum)

        return max(subarray)

    print(maxArr([1, 3, -1]))
