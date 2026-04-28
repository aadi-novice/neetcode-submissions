class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {i: [] for i in range(1,len(nums)+1)} #hash map with indexes
        for i in range(len(nums)):
            found = False
            
    
         # Check if nums[i] exists in any list
            for key, value_list in count.items():
                if nums[i] in value_list:
                    # Value exists at this key
                    found = True
                    # Do something with the key
                    count[key].remove(nums[i])
                    count[key+1].append(nums[i])
                    break
    
            if not found:
                # Value not found, add to key 1
                count[1].append(nums[i])
        k = -k
        last_k = [item for value_list in count.values() for item in value_list][k:]
        return last_k
                