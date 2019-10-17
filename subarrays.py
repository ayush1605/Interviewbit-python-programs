class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve( A, B):
        sub = []
        G=[]
        final = []

        for i in range(len(A) ):
            for j in range(i+1, len(A)+1):
                sub.append(A[i:j])
        print(sub)

        for k in sub:
            G.append(max(k))

        print (sorted(G))

        for no in G:
            div = 1
            for l in range(1, no):
                print("l")
                if no % l == 0:
                    div = no*l
            print("lm")
            final.append(div)
        return sorted(final, reverse=-1)

    print(solve([39, 99, 70, 24, 49, 13, 86, 43, 88, 74, 45, 92, 72, 71, 90, 32, 19, 76, 84, 46, 63, 15, 87, 1, 39, 58, 17, 65, 99, 43, 83, 29, 64, 67, 100, 14, 17, 100, 81, 26, 45, 40, 95, 94, 86, 2, 89, 57, 52, 91, 45],[1, 2, 3, 4, 5, 6]))
