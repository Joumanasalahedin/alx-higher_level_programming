#!/usr/bin/node
exports.esrever = function (list) {
    const rev_arr = [];

    for (let i = list.length - 1; i >= 0; i--) {
        rev_arr.push(list[i]);
    }
    return rev_arr
}
