class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # s1=sorted(s1)
        # for i in range(len(s2)):
        #     for j in range(i,len(s2)):
        #         substr=s2[i:j+1]
        #         substr=sorted(substr)
        #         if substr==s1:
        #             return True
        # return False           
        count = Counter(s1)
        window=defaultdict(int)

        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            window[s2[i]] += 1

        left=0

        for right in range(len(s1),len(s2)):
            if count == window:
                return True
            else:
                window[s2[right]] +=  1
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left+=1

        return count == window

            





        

        
        