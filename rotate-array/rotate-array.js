var rotate = function (nums, k) {
    k = k % nums.length;

    left = 0;
    right = nums.length - 1
    while (left < right) {
        swap(left, right, nums)
        left += 1
        right -= 1
    }

    left = 0;
    right = k - 1
    while (left < right) {
        swap(left, right, nums)
        left += 1
        right -= 1
    }

    left = k;
    right = nums.length - 1
    while (left < right) {
        swap(left, right, nums)
        left += 1
        right -= 1
    }
};

var swap = function (left, right, nums) {
    temp = nums[left];
    nums[left] = nums[right];
    nums[right] = temp;
}