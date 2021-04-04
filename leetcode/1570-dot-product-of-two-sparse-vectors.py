# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/


class SparseVector:
    def __init__(self, nums: List[int]):
        self.values = {}
        for i, v in enumerate(nums):
            if v == 0:
                continue
            self.values[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        if len(self.values.keys()) > len(vec.values.keys()):
            return vec.dotProduct(self)
        ans = 0
        for k, v in self.values.items():
            if k not in vec.values:
                continue
            ans += v * vec.values[k]
        return ans


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)