class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        vector<int> res;

        int left = 0;
        int right = nums.size() - 1;

        while (left <= right)
        {
            int n1 = abs(nums[left]);
            int n2 = abs(nums[right]);

            if (n1 > n2)
            {
                res.push_back(n1 * n1);
                left += 1;
            }
            else
            {
                res.push_back(n2 * n2);
                right -= 1;
            }
        }
        reverse(res.begin(), res.end());

        return res;
    }
};