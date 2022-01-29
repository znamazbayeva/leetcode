class Solution {
public:
    string reverseWords(string s) {
        size_t len = s.length();
        size_t l = 0,  r, last = 0;
        do {
            r = s.find(" ", last+1)-1;
            if (r+1 != std::string::npos)  last = r+1;
            else {r = len-1; last = len;}
            while(l < r) swap(s[l++], s[r--]);
            l = last+1;
        } while(l < len);

        return s;
    }
};