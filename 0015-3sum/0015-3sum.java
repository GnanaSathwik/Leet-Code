class Solution {
    public List<List<Integer>> threeSum(int[] nums) 
    {
        int i=0;
        List<List<Integer>> arr = new ArrayList<>();
        Arrays.sort(nums);
        for(i=0;i<nums.length-2;i++)
        {
            if(i>0 && nums[i] == nums[i-1])
            {
                continue; 
            }
            int f = i+1;
            int e = nums.length-1;
            while(f<e)
            {
                int sum = nums[i] + nums[f]+nums[e];
                if(sum==0)
                {
                    arr.add(Arrays.asList(nums[i],nums[f],nums[e]));
                    f++;
                    e--;
                    while(f<e && nums[f]==nums[f-1])
                    {
                        f++;
                    }
                    while(f<e && nums[e]==nums[e+1])
                    {
                        e--;
                    }                   
                }
                else if(sum<0)
                {
                    f++;
                }
                else
                {
                    e--;
                }
            }            
        }
        return arr;      
    }
}