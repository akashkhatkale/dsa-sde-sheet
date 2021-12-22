class Solution
{
public:
    vector<vector<int> > threeSum(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int i = 0;
        vector<vector<int> > result;

        while (i < n)
        {
            if (i > 0 and nums[i - 1] == nums[i])
            {
                i++;
                continue;
            }

            int left = i + 1;
            int right = n - 1;

            while (left < right)
            {
                int threeSum = nums[i] + nums[left] + nums[right];
                vector<int> pair;
                if (threeSum == 0)
                {
                    pair.push_back(nums[i]);
                    pair.push_back(nums[left]);
                    pair.push_back(nums[right]);
                    result.push_back(pair);
                    left += 1;
                    while (nums[left] == nums[left - 1] and left < right)
                    {
                        left += 1;
                    }
                }
                else if (threeSum < 0)
                {
                    left += 1;
                }
                else
                {
                    right -= 1;
                }
            }
            i++;
        }

        return result;
    }
};