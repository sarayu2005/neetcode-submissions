

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            # Sort the word and use it as a key
            key = ''.join(sorted(word))
            groups[key].append(word)

        # Return all grouped anagrams as a list of lists
        return list(groups.values())