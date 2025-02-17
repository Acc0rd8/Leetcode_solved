# 2942. Find Words Containing Character #

You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

 

__Example 1:__

> __Input:__ words = ["leet","code"], x = "e"
> __Output:__ [0,1]
> __Explanation:__ "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

__Example 2:__

> __Input:__ words = ["abc","bcd","aaaa","cbc"], x = "a"
> __Output:__ [0,2]
> __Explanation:__ "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.

__Example 3:__

> __Input:__ words = ["abc","bcd","aaaa","cbc"], x = "z"
> __Output:__ []
> __Explanation:__ "z" does not occur in any of the words. Hence, we return an empty array.
 

__Constraints:__

- 1 <= words.length <= 50
- 1 <= words[i].length <= 50
- x is a lowercase English letter.
- words[i] consists only of lowercase English letters.