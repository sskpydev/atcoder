def main ():
    N = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    while all([x % 2 == 0 for x in a]):
        a = [x / 2 for x in a]
        cnt += 1
    
    print(cnt) 


if __name__ == '__main__':
    main()
