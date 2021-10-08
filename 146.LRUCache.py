class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.keys = []
        self.capacity = capacity
        print("Null")

    def get(self, key: int) -> int:
        if(key not in self.keys):
            print(-1)
            return -1
        else: 
            self.keys.pop(self.keys.index(key))
            self.keys.insert(0,key)
            print(self.dict[key])
            return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if (key in self.keys): #存在 然后更新 key也要换位置
            self.dict.update({key:value})
            self.keys.pop(self.keys.index(key))
            self.keys.insert(0,key)
        elif (len(self.dict)< self.capacity):#不存在 小于容量 直接插入
            self.dict.update({key:value})
            self.keys.insert(0,key)    
        else: #不存在 且 大于等于容量 把最后一位踢出去，新的插进来
        # elif ((len(self.dict) == self.capacity) and (key not in self.keys)):
            self.dict.pop(self.keys[-1])
            self.keys.pop(-1)
            self.dict.update({key:value})
        print(self.dict)
        print(self.keys)
        print("Null")
# Your LRUCache object will be instantiated and called as such:


lRUCache = LRUCache(2)
lRUCache.get(2); 
lRUCache.put(2, 6);
lRUCache.get(1);
lRUCache.put(1, 5);
lRUCache.put(1, 2);

lRUCache.get(1);    
lRUCache.get(2);    

