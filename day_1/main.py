from numpy import Infinity, sort

def main():
    high = -Infinity
    totals = []
    with open("./input", "r") as f:
        total = 0
        vals = []
        for v in f:
            try:
                d = int(v)
                total += d
                vals.append(d)
            except ValueError as e:
                totals.append(total)
                if total > high:
                    high = total
                total = 0
                vals = []
                
    sorted = sort(totals)
    print(sorted[-1])
    print(sum(sorted[-3:]))

if __name__ == "__main__":
    main()