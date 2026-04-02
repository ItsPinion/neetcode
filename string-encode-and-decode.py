import json


class Solution:
    def encode(self, strs: list[str]) -> str:

        return json.dumps(strs)

    def decode(self, s: str) -> list[str]:
        return json.loads(s)


dummy_input = [""]
solution = Solution()
encoded = solution.encode(dummy_input)
print(encoded)
decoded = solution.decode(encoded)
print(decoded)
