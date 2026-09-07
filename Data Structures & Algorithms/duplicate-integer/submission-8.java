class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> numMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            numMap.put(nums[i], i);
        }

        if(nums.length == numMap.size()){
            return false;
        }
        else{
            return true;
        }
    }
}