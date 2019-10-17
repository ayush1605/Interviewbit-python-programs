import string
import math
import array
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(A):
        modify_string = (A.upper())
        modify_string1 = modify_string.strip()
        final_String=''
        final1_String = ''
        new_String = ''

        for j in range(0, len(modify_string1)):
            new_String = ord(modify_string1[j])
            print(new_String)
            if new_String >= 65 and new_String <= 90:
                final1_String = modify_string1[j] + final1_String
            elif new_String >= 48 and new_String <= 57:
                final1_String = modify_string1[j] + final1_String
            else:
                pass

        for i in range(0, len(modify_string)):
            new_String = ord(modify_string[i])
            if new_String>=65 and new_String<=90:
                final_String = final_String + modify_string[i]
            elif new_String>=48 and new_String<=57:
                final_String = final_String + modify_string[i]
            else:
                pass

        print(final1_String)
        print(final_String)

        if(final_String == final1_String):
            return True



    print(isPalindrome("1a1"))


