from collections import defaultdict

def merge_the_tools(string, k):
    
    
    n=len(string)
    res=[]
    
    for i in range(0,n,k):
        chunk = string[i:i+k]
        ##chunk ="AAB"
        seen=defaultdict(int)
        temp =""
        for char in chunk:
            if char not in seen:
                
                temp+=char
                seen[char] +=1
        res.append(temp)
    
    for r in res:
        print(r)
        
    # your code goes here

