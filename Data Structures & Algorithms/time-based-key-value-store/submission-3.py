class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic.keys():
            self.dic[key].append([value, timestamp])
        else:
            self.dic[key] = [[value, timestamp]]
        print(self.dic)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic.keys():
            return ""
        values = self.dic[key]
        l = 0
        r = len(values) - 1
        ans = ""
        while l <= r:
            m = (l + r) // 2
            if values[m][1] == timestamp:
                return values[m][0]
            if values[m][1] < timestamp:
                ans = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return ans
            
        
