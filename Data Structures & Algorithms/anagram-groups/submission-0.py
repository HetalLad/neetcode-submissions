class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            word= tuple(sorted(i))
            if word not in d:
                d[word]=[i]
            else:
               d[word].append(i)
        return (list(d.values()))