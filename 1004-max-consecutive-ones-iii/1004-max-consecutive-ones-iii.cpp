class Solution {
public:
    int longestOnes(vector<int>& arr, int k) {
        int canFlip = k;
        int i = 0, j = 0;
        int max = 0, length = 0;
        while(i < arr.size()) {
            if(arr[i] == 1) {
                length++;
                i++;
            } else {
                if (canFlip != 0) {
                    length++;
                    i++;
                    canFlip--;      
                } else {
                    if(arr[j++] == 0) canFlip++;
                    length--;
                }
            } 
            max = max > length ? max : length;
        }
        return max;
    }
};