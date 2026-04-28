class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post , pre = 1,1
        i = 0
        j = -1
        l = len(nums)
        output = [1] * l
       
        while True:
            output[i] = output[i] * pre
            pre = nums[i] * pre
            i += 1

            output[j] = output[j] * post
            post = nums[j] * post
            j -= 1

            if i == len(nums) or abs(j) == len(nums)+ 1:
                break
        return output