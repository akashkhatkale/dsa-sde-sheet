// Moore's voting algorithm

var majorityElement = function (nums) {
    majority = nums[0];
    count = 1;

    for (let i = 0; i < nums.length; i++) {
        if (majority == nums[i]) {
            count += 1;
        } else {
            count -= 1;
        }


        if (count == 0) {
            majority = nums[i];
            count = 1;
        }
    }

    return majority;


};