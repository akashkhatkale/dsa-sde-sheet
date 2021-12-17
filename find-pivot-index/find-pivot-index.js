var pivotIndex = function (nums) {
    left_sum = 0;
    right_sum = 0;
    for (let i = 0; i < nums.length; i++) {
        right_sum += nums[i]
    }

    for (let i = 0; i < nums.length; i++) {
        left_sum += nums[i]
        if (left_sum == right_sum) {
            return i
        }
        right_sum -= nums[i]
    }

    return -1
};