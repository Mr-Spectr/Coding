class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = {k: v for k, v in knowledge}
        result = []
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                i += 1
                key_start = i
                while i < n and s[i] != ')':
                    i += 1
                key = s[key_start:i]
                result.append(mapping.get(key, "?"))
            else:
                result.append(s[i])
            i += 1
            
        return "".join(result)
