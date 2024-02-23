class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        output = [False]*len(candies)
        maxCandy = 0

        for kid in candies:
            maxCandy = max(kid, maxCandy)

        for i in range(len(candies)):
            if(candies[i] + extraCandies >= maxCandy):
                output[i] = True
        
        return output
    
candies = [2,3,5,1,3]
extraCandies = 3

result = Solution().kidsWithCandies(candies, extraCandies)
print(result)
