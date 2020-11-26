
## write your code here
def response(lines):
    ## copy following code in TOSA console ## 
    os1 = lines[1].split(' ')[1]
    os2 = lines[2].split(' ')[1]
    
    result = 0
    if os1 == os2:
        same = True
        production = 3
        while(same):
            if lines[production].split(' ')[1] == os1:
                production += 1
            else:
                same = False
                result = lines[production].split(' ')[0]
    else:
        if lines[3].split(' ')[1] == os1:
            result = lines[2].split(' ')[0]
        else:
            result = lines[1].split(' ')[0]
    print(result)
