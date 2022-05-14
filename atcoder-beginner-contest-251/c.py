import itertools


def main ():
    n = int(input())
    st = [input().split() for _ in range(n)]

    d = dict()
    for st_r in st:
        d.setdefault(st_r[0], int(st_r[1]))

    max_v = max(d.values())
    max_d = max(d, key=d.get)
    for i, x in enumerate(st):
        if int(x[1]) == max_v and x[0] == max_d:
            print(i+1)
            break
    


if __name__ == '__main__':
    main()
