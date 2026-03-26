if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    first=-101
    runner=-101
    for score in arr:
        if score>first:
            temp=first
            first=score
            runner=temp
        elif score>runner and score<first:
            runner=score
    print(runner)
