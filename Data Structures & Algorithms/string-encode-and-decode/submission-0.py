class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            length = len(s)
            encoded.append(str(length) + '#' + s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        solution = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j + 1
            original_str = s[i:i+length]
            solution.append(original_str)
            i = i + length
        return solution
        

