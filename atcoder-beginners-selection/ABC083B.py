def main ():
    n, a, b = map(int, input().split())

    ans = 0
    for i in range(n+1):
        if a <= sum(list(map(int, str(i)))) <= b:
            ans += i

    print(ans)


if __name__ == '__main__':
    main()