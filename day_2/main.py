if __name__ == "__main__":
    with open("input") as f:
        sorted = list(map(lambda x: int(x) if x != '\n' else 0, f.readlines()))
        print(sum(sorted[-3:]))