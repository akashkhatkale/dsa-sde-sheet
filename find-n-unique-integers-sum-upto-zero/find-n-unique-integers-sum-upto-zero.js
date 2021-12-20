var sumZero = function (n) {
    isEven = n % 2 == 0

    left = 0;
    res = [];
    num = -Math.floor(n / 2);

    while (left < n) {
        res.push(num);
        if (num == -1 && isEven) {
            num += 2
        } else {
            num += 1
        }
        left += 1
    }

    return res
};