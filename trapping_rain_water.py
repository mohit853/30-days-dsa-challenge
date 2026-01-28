
class Solution:
    def trap(self, height: List[int]) -> int:
        
    
        
        n= len(height)
        
        if n<=2:
            return 0
        
        left,right = 0,n-1
        max_wall_left ,max_wall_right = 0 ,0
        water=0
        
        while left<right:
            if height[left] < height[right]:
                ### decide wall left or right
                
                ## is this left_max or water gets trapped
                
                if height[left] >= max_wall_left:
                    max_wall_left = height[left]
                else:
                    water = water + max_wall_left - height[left]
                left+=1
            else:
                if height[right] >= max_wall_right:
                    max_wall_right = height[right]
                else:
                    water = water + max_wall_right - height[right]
                right-=1
        
        return water
                    
            
                    
                    
        
