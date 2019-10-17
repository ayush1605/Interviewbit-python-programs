class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(arrive, depart, K):

        arrive = sorted(arrive)
        depart = sorted(depart)
        count = 0
        n = len(arrive) - K

        if (n <= 0):
            return 1

        for i in range(len(arrive) - 1):
            print(arrive[i + 1])
            print(range(len(arrive) - 2))
            print(i)
            if (arrive[i + 1] - depart[i] >= 0):
                print(str(count) + "b")
                count += 1
            else:
                pass
            print(i)

        if (count == len(arrive) - 1):
            return 1
        else:
            return 0

    print(hotel([1 ,2, 3],[2,3,4],1))




