class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int count = 0;
        int result = 0;
        int index = 0;

        while (index < nums.size())
        {
            if (count == 0)
            {
                nums[result] = nums[index];
                result += 1;
            }

            if (index < nums.size() - 1 and nums[index] == nums[index + 1])
            {
                count += 1;
            }
            else
            {
                count = 0;
            }
            index += 1;
        }

        return result;
    }
};