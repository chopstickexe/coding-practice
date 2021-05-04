# https://leetcode.com/problems/lru-cache/


from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.value = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # print(f"get: {self.value}")
        if key not in self.value:
            return -1
        self.value.move_to_end(key)
        return self.value[key]

    def put(self, key: int, value: int) -> None:
        if key in self.value:
            self.value.move_to_end(key)
        self.value[key] = value
        if len(self.value) > self.capacity:
            self.value.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)