/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
function findAnswer(nums, set) {
    var answer = new Set()
    nums.forEach(element => {
        if (!set.has(element)) {
            answer.add(element)
            }
    })

    return Array.from(answer)
}

var findDifference = function(nums1, nums2) {
    var answer = []
    var set1 = new Set()
    var set2 = new Set()
    
    nums1.forEach(element => set1.add(element))
    nums2.forEach(element => set2.add(element))

    answer.push(findAnswer(nums1, set2))
    answer.push(findAnswer(nums2, set1))
    
    return answer
        
};