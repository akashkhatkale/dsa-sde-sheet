var sortedSquares = function (nums) {
    res = [];

    left = 0;
    right = nums.length - 1;

    while (left <= right) {
        n1 = Math.abs(nums[left]);
        n2 = Math.abs(nums[right]);

        if (n1 > n2) {
            res.unshift(n1 * n1);
            left += 1;
        } else {
            res.unshift(n2 * n2);
            right -= 1;
        }
    }

    return res;
};