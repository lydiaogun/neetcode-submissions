class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}  # hashmap: key = sorted word, value = list of words with that key

        for w in strs:
            # sort letters in the word
            key = ''.join(sorted(w))

            # if key not in groups, initialize with empty list
            if key not in groups:
                groups[key] = []

            # add word to the right group
            groups[key].append(w)

        # return all the grouped lists
        return list(groups.values())  