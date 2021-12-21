var largestNumber = function (nums) {
    for (let i = 0; i < nums.length; i++) {
        j = i + 1;

        while (j < nums.length && i < nums.length) {
            ij = nums[i].toString() + nums[j].toString()
            ji = nums[j].toString() + nums[i].toString()

            if (parseInt(ij) < parseInt(ji)) {
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            }
            j += 1
        }
    }

    res = ""
    nums.map((e) => {
        res += e.toString()
    })

    return parseInt(res) == 0 ? "0" : res
};