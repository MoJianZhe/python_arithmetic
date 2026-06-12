def circle():
    arr = [1,2,3,4,5]
    i = 0
    j = 0
    while i <len(arr):
        i = (i+1)%len(arr)
        j = j+1
        print(j)
        if(j==1000):
            break

if __name__ == "__main__":
    print("hello world")
    circle()


