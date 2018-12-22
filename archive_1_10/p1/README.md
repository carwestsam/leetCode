# 1. [Two Sum](https://leetcode.com/problems/two-sum/)

**Easy**

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```


## Solution walk through

1. make it runnable
2. double loop to find answer
3. loop first element, and use divide to find j in sorted array
4. given random array list, sort and preserve index
