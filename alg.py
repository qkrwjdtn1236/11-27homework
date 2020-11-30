def money(n):
    count = 0
    arr = [500,100,50,10]

    for i in arr:
        count+=n//i
        n%=i

    return count

def while1(n,k):
    result = 0

    while True:

        target = (n//k)*k
        result+= n-target

        if n<k:
            break

        result+=1
        n//=k
    result +=(n-1)
    return result

def mulPlus(data):

    result = int(data[0])

    for i in range(1,len(data)):
        num = int(data[i])
        if num<=1 or result<=1:
            result+=num
        else:
            result*=num

    return result

def time(h):
    count = 0

    for i in range(h+1):
        for j in range(60):
            for k in range(60):

                if '3' in str(i) + str(j) + str(k):
                    count+=1


    return count

def VertialHorizontal(n,plans):
    x,y = 1,1

    dx = [0,0,-1,1]
    xy = [-1,1,0,0]

    move_types = ['L','R','U','D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x+dx[i]
                ny = y+dy[i]

        if nx<1 or ny<1 or nx>n or ny>n:
            continue

        x,y = nx,ny

    print(x,y)

def alnumSort(text):
    result = []
    value = 0

    for x in text:
        if x.isalpha():
            result.append(x)
        else:
            value+=int(x)

    result.sort()

    if value!=0:
        result.append(str(value))

    print(''.join(result))