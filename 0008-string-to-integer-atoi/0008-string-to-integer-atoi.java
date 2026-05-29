class Solution {
    public int myAtoi(String s) 
    {
        int i = 0; 
        while(i<s.length() && s.charAt(i) == ' ')
        {
            i++;
        }

        int sign = 1;
        if(i<s.length())
        {
            if (s.charAt(i) == '-')
            {
                sign = -1;
                i++;
            }
            else if (s.charAt(i) == '+')
            {
                i++;
            }
        }
        long num = 0;
        while(i<s.length() && Character.isDigit(s.charAt(i)))
        {
            int d = s.charAt(i) - '0';
            if(num > (Integer.MAX_VALUE - d) / 10)
            {
                return sign == 1
                ? Integer.MAX_VALUE
                : Integer.MIN_VALUE;
            }
            num = num*10 +d;
            i++;
        }
        num = num *sign;
        if(num > Integer.MAX_VALUE)
        {
            num = Integer.MAX_VALUE;
            }
        else if( num < Integer.MIN_VALUE)
        {
             num = Integer.MIN_VALUE;
        }
        return (int) num;
        

    }
}