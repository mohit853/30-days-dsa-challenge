class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}
        stk =[]
        for ch in s:
            
            if ch in pairs:
                stk.append(ch)
            elif stk and ch == pairs[stk[-1]]:
                stk.pop()
            else:
                return False
        if stk:
            return False
        
        
        return True
        
