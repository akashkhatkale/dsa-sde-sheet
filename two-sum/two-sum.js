// https://leetcode.com/problems/two-sum/

var twoSum = function (nums, target) {
    // initialise a dictionary
    var map = {}

    for (let i = 0; i < nums.length; i++) {
        // calculate the difference
        var diff = target - nums[i]

        if (map[diff] != undefined) {
            // if the difference is in the seen, return it
            return [i, map[diff]]
        } else {
            // if not, set it
            map[nums[i]] = i
        }
    }
};