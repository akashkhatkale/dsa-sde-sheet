// https://leetcode.com/problems/maximum-subarray/
// Solve using Kadane's Algorithm

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int maximum = nums[0];
        int current_max = maximum;

        for (int i = 1; i < nums.size(); i++)
        {
            current_max = max(nums[i], current_max + nums[i]);
            if (current_max > maximum)
            {
                maximum = current_max;
            }
        }

        return maximum;
    }
};