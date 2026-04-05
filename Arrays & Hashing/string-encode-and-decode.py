import json


class Solution:
    def encode(self, strs: list[str]) -> str:
        return json.dumps(strs)

    def decode(self, s: str) -> list[str]:
        return json.loads(s)


solution = Solution()
print(solution.encode(["hello", "world"]))  # Output: '["hello", "world"]'
print(solution.decode('["hello", "world"]'))  # Output: ["hello", "world"]
