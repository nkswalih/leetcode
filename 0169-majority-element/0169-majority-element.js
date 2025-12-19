/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let c = null;
    let count = 0;
    
    for(let i = 0;i<nums.length;i++){
        if(count === 0){
            c = nums[i];
        }
        
        if(nums[i] === c){
            count++;
        }
        else {
            count--;
        }
    }
    return c;
};