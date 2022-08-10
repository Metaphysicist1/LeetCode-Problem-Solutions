# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


def containsDuplicate(self, nums: list[int]) -> bool:
        length=len(nums)
        nums=len(set(nums))
        if length==nums:
            return False
        else:
            return True