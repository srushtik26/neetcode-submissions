class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        i,j=0,0

        
        while i< len(word1) and j<len(word2):
            result += word1[i]
            result += word2[j]
            i+=1
            j+=1

        result += word1[i:]
        result += word2[j:]

        return result 

        # result = ""
        # i, j = 0, 0

        # while i < len(word1) and j < len(word2):
        #     result += word1[i]
        #     result += word2[j]
        #     i += 1
        #     j += 1

        # result += word1[i:]  # If word1 has remaining letters
        # result += word2[j:]  # If word2 has remaining letters

        # return result

        
        