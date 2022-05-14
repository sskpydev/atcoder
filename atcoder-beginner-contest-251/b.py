import itertools


def main ():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))

    ans = []
    for i in range(1, 4):
        for team in itertools.combinations(a, i):
            if sum(list(team)) <= w:
                ans.append(sum(list(team)))

    print(len(set(ans)))


if __name__ == '__main__':
    main()
