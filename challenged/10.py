def ant(n):
    if n == 1:
        return "1"
    
    pre_ant = ant(n-1)
    result = ""
    count = 1
    
    for i in range(len(pre_ant)):
        if i + 1 < len(pre_ant) and pre_ant[i] == pre_ant[i+1]:
            count += 1
        else:
            result += str(count) + pre_ant[i]
            count = 1
            
    return result

if __name__ == "__main__":
    n = 31
    print(len(ant(n)))