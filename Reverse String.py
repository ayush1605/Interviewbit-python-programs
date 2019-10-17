class Solution:
    # @param A : string
    # @return a strings
    def solve(A):
        A= A.rstrip()+" "
        reverse_string = ""
        new_string = ""

        for i in (A):
            if(i == ' '):
                new_string = reverse_string +" "+  new_string
                reverse_string = ""
            else:
                reverse_string = reverse_string + i
        return  new_string.rstrip()

    print(solve("j"))

