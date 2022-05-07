/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} threshold
 * @return {number}
 */
var numOfSubarrays = function(arr, k, threshold) {
    var i = 0, j =0;
    var sum = 0, cnt = 0;
    for(; i < arr.length; ++i) {
        if(i - j === k) {
            sum -= arr[j];
            j++;
        }
        sum += arr[i];
        let avg = sum/k;
        if(i - j +1 === k && avg >= threshold) {
            ++cnt;
        }
    } 
    return cnt;
    
};