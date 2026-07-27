class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create hashmap to group words
        wordCount = defaultdict(list)

        # Iterate word in strs:
        for word in strs:
            # Initialise list of 26 chars (a - z)
            count = [0] * 26

            # Iterate char in word:
            for char in word:
                # Convert char to index, then append to countList
                count[ord(char) - ord('a')] += 1

            # Set the current countList and corresponding word into the hashmap
            wordCount[tuple(count)].append(word)

        # Return the values in the hashmap
        return list(wordCount.values())