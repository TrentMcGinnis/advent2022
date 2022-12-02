from numpy import Infinity, sort

def main():
    high = -Infinity
    totals = []
    with open("./input", "r") as f:
        sum = 0
        vals = []
        for v in f:
            try:
                d = int(v)
                sum += d
                vals.append(d)
            except ValueError as e:
                totals.append(sum)
                if sum > high:
                    high = sum
                sum = 0
                vals = []
                
    sorted = sort(totals)
    return sorted

if __name__ == "__main__":
    final = main()
    print(final)