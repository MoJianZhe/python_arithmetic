from dataclasses import asdict, dataclass
import json


class LinkNode():
    def __init__(self,val):
        self.pre = None
        self.val = val
        



class LinkStack():
    def __init__(self):
        self.tail=None
        
    def push(self,x):
        a =LinkNode(x)
        a.pre = self.tail
        self.tail = a

    def pop(self):
        val = self.tail.val
        if(self.tail.pre is not None):
            self.tail = self.tail.pre
        return val
    
    def peek(self):
        return self.tail.val
    
if __name__=='__main__':
    s = LinkStack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.peek())
    print(s)
    # json 会自动递归处理，把 node1 也转成字典
    json_str = json.dumps(s, default=lambda obj: obj.__dict__, ensure_ascii=False)
    print(json_str)