if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    output = [[i,j,k] for i in (x+1) for j in (y+1) for k in (z+1) if i+j+k != n]
    
    print(output)
