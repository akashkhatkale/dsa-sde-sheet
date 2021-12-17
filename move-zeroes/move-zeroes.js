
var moveZeroes = function (nums) {
    count = 0
    n = nums.length

    for (let i = 0; i < n; i++) {
        if (nums[i] == 0) {
            count += 1
        } else if (count > 0) {
            temp = nums[i - count];
            nums[i - count] = nums[i];
            nums[i] = temp
        }
    }

};