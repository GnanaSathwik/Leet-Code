class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        count = 0
        n = len(points)
        if n<=2: 
            return n
        for i in range(n):
            slope = defaultdict(int)
            max_count = 0
            for j in range(i+1,n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]

                g = gcd(x,y)
                x = x//g
                y = y//g
                if(x<0):
                    x = -x
                    y = -y
                elif(x==0):
                    y = 7 # U can take any number here
                
                slope[(x,y)] += 1
                max_count = max(max_count, slope[(x,y)])
            count = max(count ,max_count +1)
        
        return count
        