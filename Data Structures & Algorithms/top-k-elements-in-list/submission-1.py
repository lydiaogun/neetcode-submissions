class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequent_elements=[]
        map ={}

       #iterate through list and put the counts in the hashmap
        for i in nums:
            if i in map:
                map[i] +=1
            else:
                map[i] = 1


        #quit tricky bit but we need to extract the top k amounts but we need to sort the top based on the counts in the hashmap
        top_k = sorted(map.items(), key = lambda x : x[1], reverse= True ) [:k] #we have reverse true so that it displays the largest counts the top largest counts instead of the smallest ones
        result = [item[0] for item in top_k]
        return result
        