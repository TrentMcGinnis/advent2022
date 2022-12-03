POINTS_MAPPING = {
    "AX": 3,
    "BX": 1,
    "CX": 2,
    "AY": 4,
    "BY": 5,
    "CY": 6,
    "AZ": 8,
    "BZ": 9,
    "CZ": 7,
}


def main():
    with open("input") as f:
        print(sum(map(lambda d: POINTS_MAPPING[d], map(lambda a: a[0]+a[1], map(lambda l: l.split(), f.readlines())))))

if __name__ == "__main__":
    main()