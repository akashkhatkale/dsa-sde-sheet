class Solution
{
public:
    void moveZeroes(vector<int> &nums)
    {
        int count = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++)
        {
            if (nums[i] == 0)
            {
                count += 1;
            }
            else if (count > 0)
            {
                int temp = nums[i - count];
                nums[i - count] = nums[i];
                nums[i] = temp;
            }
        }
    }
};