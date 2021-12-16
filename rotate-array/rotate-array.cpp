class Solution
{
public:
    void rotate(vector<int> &nums, int k)
    {
        k = k % nums.size();

        int left = 0;
        int right = nums.size() - 1;
        while (left < right)
        {
            swap(left, right, nums);
            left += 1;
            right -= 1;
        }

        left = 0;
        right = k - 1;
        while (left < right)
        {
            swap(left, right, nums);
            left += 1;
            right -= 1;
        }

        left = k;
        right = nums.size() - 1;
        while (left < right)
        {
            swap(left, right, nums);
            left += 1;
            right -= 1;
        }
    }

    void swap(int left, int right, vector<int> &nums)
    {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }
};