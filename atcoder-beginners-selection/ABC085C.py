def main ():
    n, y = map(int, input().split())
    
    ans = [-1, -1, -1]
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if 10000*i + 5000*j + 1000*k == y:
                    ans = [i, j, k]
                    break

    print(' '.join([str(x) for x in ans]))


if __name__ == '__main__':
    main()
