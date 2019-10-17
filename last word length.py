class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(A):
        count = 0
        space = ' '

        for i in reversed(range (len(A.rstrip()))):
            print("i")
            if(A[i] == ' '):
                break
            else:
                count = count+1
        print(len(A))
        print(count)
        if(count == len(A)):
            print ('0')
        else:
            print(count)

    lengthOfLastWord("tyu d  ")