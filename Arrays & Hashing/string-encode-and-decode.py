import json

class Solution:
    def encode(self, strs: list[str]) -> str:
        return json.dumps(strs)

    def decode(self, s: str) -> list[str]:
        return json.loads(s)
