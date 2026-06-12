
from dataclasses import dataclass
import json
from typing import List
@dataclass
class MyStack:
    arr:List
    def __init__(self):
        self.arr =[]
    def pop(self):
        return self.arr.pop()

    def push(self,x):
        return self.arr.append(x)

    def peek(self):
        return self.arr[-1]
    



if __name__=='__main__':
    s = MyStack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.peek())
    print(s)
    print(json.dumps(s.__dict__))
    