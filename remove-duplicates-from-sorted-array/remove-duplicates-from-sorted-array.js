var removeDuplicates = function (nums) {
    index = 0
    count = 0
    result = 0
    while (index < nums.length) {
        if (count === 0) {
            nums[result++] = nums[index]
        }
        if (index < nums.length && nums[index] === nums[index + 1]) {
            count++
        }
        if (index < nums.length && nums[index] !== nums[index + 1]) {
            count = 0
        }
        index++
    }

    return result
};