class Solution
{
public:
    void nextPermutation(vector<int> &nums)
    {
        int n = nums.size();

        if (n == 1)
        {
            return;
        }

        // find the peak element
        int lastPeak = -1;
        int i = 1;
        while (i < n)
        {
            if (nums[i] > nums[i - 1])
            {
                lastPeak = i;
            }
            i += 1;
        }

        // no peak found
        // just return the sorted array
        if (lastPeak == -1)
        {
            for (int i = 0; i < n / 2; i++)
            {
                swap(nums[i], nums[n - i - 1]);
            }
            return;
        }

        // peak found, swap the peak index
        // sort the rightmost of the peak
        int mn = nums[lastPeak];
        int index = lastPeak;
        for (i = lastPeak; i < n; i++)
        {
            if (nums[i] > nums[lastPeak - 1] and nums[i] < nums[index])
            {
                index = i;
            }
        }
        swap(nums[lastPeak - 1], nums[index]);
        sort(nums.begin() + lastPeak, nums.end());
    }
};
