if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    scores = sorted(list(set([x[1] for x in students])))
    second = scores[1]
    low = [x[0] for x in students if x[1] == second]
    low.sort()
    for name in low:
        print(name)
