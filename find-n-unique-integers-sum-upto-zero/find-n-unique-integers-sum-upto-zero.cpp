class Solution
{
public:
    vector<int> sumZero(int n)
    {
        int left = 0;
        int num = -floor((double)n / 2);
        vector<int> res;

        while (left < n)
        {
            res.push_back(num);
            if (num == -1 && n % 2 == 0)
            {
                num += 2;
            }
            else
            {
                num += 1;
            }
            left += 1;
        }

        return res;
    }
};