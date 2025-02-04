if __name__ == '__main__':
    records = []
    scores = []
    second = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name, score])
        scores.append(score) 
        
    scores.sort()
    
    for i in range(1, len(scores)):
        if scores[i] != scores[i-1]:
            second = scores[i]
            break       
    
            
    names = [record[0] for record in records if record[1] == second]
            
    names.sort()
    
    for name in names:
        print(name)
