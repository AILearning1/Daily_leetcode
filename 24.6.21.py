class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        ##先找到两个变化的列表，0表示平稳，1表示上升，2表示下降
        n = len(temperatureA)
        a = [0] * (n - 1)
        b = [0] * (n - 1)
        for i in range(n - 1):
            if temperatureA[i] == temperatureA[i + 1]:
                a[i] = 0
            elif temperatureA[i] > temperatureA[i + 1]:
                a[i] = 2
            else:
                a[i] = 1
        for i in range(n - 1):
            if temperatureB[i] == temperatureB[i + 1]:
                b[i] = 0
            elif temperatureB[i] > temperatureB[i + 1]:
                b[i] = 2
            else:
                b[i] = 1
        print(a)
        print(b)
        k = 0
        cout = 0
        for i  in range (n - 1):
            if a[i] == b[i]:
                cout += 1
                k = max(k, cout)
            else:
                cout = 0
        return k
