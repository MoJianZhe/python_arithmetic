


from collections import deque


if __name__ == '__main__':
    a = [1,2,3]
    print(a.pop())
    print(a)

    print("===b====")

    b = deque()
    b.append(1)
    b.append(2)
    b.append(3)
    print(b.popleft())
    print("hello world")