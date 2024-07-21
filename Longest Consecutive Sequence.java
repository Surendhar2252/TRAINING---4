import java.util.HashSet;

public class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);

        int longest = 0;
        for (int num : nums) {
            if (!set.contains(num - 1)) {
                int currentNum = num;
                int length = 1;

                while (set.contains(currentNum + 1)) {
                    currentNum++;
                    length++;
                }

                longest = Math.max(longest, length);
            }
        }
        return longest;
    }
}
