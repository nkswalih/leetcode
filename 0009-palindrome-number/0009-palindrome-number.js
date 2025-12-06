/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    str = "";
    str += x;
    reverse = "";
    for(let i = str.length - 1;i >= 0;i--){
       reverse += str[i];
    }
        if(str === reverse){
            return true;
        }else{
            return false;
        }
};