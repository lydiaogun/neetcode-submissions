class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for i in strs:
            sorteds = "".join(sorted(i))
            if sorteds in hmap:
                hmap[sorteds].append(i)
            else:
                hmap[sorteds] = [i]
        return list(hmap.values())