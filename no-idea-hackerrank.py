# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    
    n, m = map(int, input().split())
    
    n_list = list(map(int, input().split()))
    
    a_set = set(map(int, input().split()))
    
    b_set = set(map(int, input().split()))
    
    score = 0
    
    for num in n_list:
        if num in a_set:
            score += 1
        elif num in b_set:
            score -= 1
            
    print(score)
