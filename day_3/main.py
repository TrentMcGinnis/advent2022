MAP = { "a": 1, "A": 27 }

def convert_val(input):
    v = ord(input)
    key = "a" if v > 90 else "A"
    return MAP[key] + (v - ord(key))

def parse_array(arr):
    return list(map(convert_val, arr))

def strip_char(v):
    return v.replace('\n', '')


def split_two(lines):
    e = map(lambda x: set(x[0]).intersection(x[1]).pop(), map(lambda l: [l[:round(len(l)/2)], l[round(len(l)/2):]], lines))
    return list(e)

def group_by_three(file_data):
    i = 0
    end = len(file_data)
    groups = []
    while i < end:
        groups.append([file_data[i], file_data[i + 1], file_data[i + 2]])
        i += 3
    single_val = list(map(lambda g: set(g[0]).intersection(g[1]).intersection(g[2]).pop(), groups))
    return list(single_val)

def main():
    with open("input") as f:
        data = list(map(strip_char, f.readlines()))
        print(sum(parse_array(split_two(data))))
        print(sum(parse_array(group_by_three(data))))

if __name__ == "__main__":
    main()
