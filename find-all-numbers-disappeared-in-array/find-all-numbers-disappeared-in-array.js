
var findDisappearedNumbers = function (nums) {
    for (let i = 0; i < nums.length; i++) {
        nums[Math.abs(nums[i]) - 1] = -Math.abs(nums[Math.abs(nums[i]) - 1])
    }

    ans = []
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 0) {
            ans.push(i + 1)
        }
    }
    return ans
};