if __name__ == '__main__':
    N = int(input())
    l = [] 
    for _ in range(N):
        com = input().split()
        c_type = com[0]   
        if c_type == "insert":
            l.insert(int(com[1]), int(com[2]))
        elif c_type == "print":
            print(l)
        elif c_type == "remove":
            l.remove(int(com[1]))
        elif c_type == "append":
            l.append(int(com[1]))
        elif c_type == "sort":
            l.sort()
        elif c_type == "pop":
            l.pop()
        elif c_type == "reverse":
            l.reverse()
