// https://leetcode.com/problems/maximum-subarray/
// Solve using Kadane's Algorithm

var maxSubArray = function (nums) {
    // declare variable to hold maximum
    max = nums[0]

    // declare variable to hold current maximum
    max_current = max

    for (let i = 1; i < nums.length; i++) {
        // set current max variable
        max_current = Math.max(nums[i], max_current + nums[i])

        // set max variable
        if (max_current > max) {
            max = max_current
        }
    }

    return max
};