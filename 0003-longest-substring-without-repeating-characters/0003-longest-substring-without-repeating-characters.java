class Solution {
    public int lengthOfLongestSubstring(String s) 
    {
        List<Character> n = new ArrayList<>(); 
        int maxi = 0;   
        for(char c: s.toCharArray())
        {
            while(n.contains(c))
            {
                n.remove(0);
            }
            n.add(c);
            maxi = Math.max(maxi ,n.size());
        }
        return maxi;

    }
}