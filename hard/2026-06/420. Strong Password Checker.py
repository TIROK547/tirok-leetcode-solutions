class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        lowercase = set(string.ascii_lowercase)
        uppercase = set(string.ascii_uppercase)
        digits = set([str(n) for n in range(10)])

        deletions = max(0, len(s) - 20)

        has_lowercase = any([c in lowercase for c in s])
        has_uppercase = any([c in uppercase for c in s])
        has_digit = any([n in digits for n in s])
        missing_types = (not has_lowercase) + (not has_uppercase) + (not has_digit)

        substring_length = self.count_substring_length(s)
        self.break_substring_by_deletion(substring_length, deletions)

    def break_substring_by_deletion(self, substring_length, deletions):
        while deletions > 0: 
            best_string_to_delete = min(enumerate(substring_length), key = lambda pair: pair[1] % 3 if pair[1] >= 3 else float("inf"))
            best_index_to_delete = best_string_to_delete[0]
            substring_length[best_index_to_delete] -= 1
            deletions -= 1

    def count_substring_length(self, s):
        res = [1]
        curr = s[0]
        for i in range(1, len(s)):
            if curr == s[i]:
                res[-1] += 1
            else:
                res.append(1)
                curr = s[i]
        return res

s = Solution()
print(s.count_substring_length("aaaAA1"))
