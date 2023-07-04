class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            print(sorted_s)
            if sorted_s in ana_dict.keys():
                ana_dict[sorted_s].append(s)
            else:
                ana_dict[sorted_s] = [s]

        return [ana_dict[i] for i in ana_dict.keys()]
