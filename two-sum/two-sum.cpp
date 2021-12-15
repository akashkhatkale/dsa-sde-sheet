class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map <int, int> seen; 
        vector<int> result; 
        
        for(int i = 0; i < nums.size(); i++){
            int difference = target - nums[i];
            
            if (seen.find(difference) != seen.end()){
                result.push_back(seen.find(difference)->second);
                result.push_back(i);
            }else{
                seen.insert(pair<int,int>(nums[i], i));
            }
        }
        
        return result;
    }
};