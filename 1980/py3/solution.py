class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        '''
        My solution here is basically brute force but with o(1) lookup.
        First we convert the nums to a set, then we create a new string of the
        same length and change each digit, checking if it's valid until we get there.
        This is o(n) to cast the nums to list, o(1) to lookup, and o(n) to brute
        force the options, so the algorithm is o(n).
        '''
        num_lookup = set()
        for num in nums:
            num_lookup.add(num)

        answer = [0 for _ in range(len(nums[0]))]
        index = 0
        while (''.join(map(str, answer)) in num_lookup):
            answer[index] = 0 if answer[index] == 1 else 1
            index += 1

        return ''.join(map(str, answer))
        
