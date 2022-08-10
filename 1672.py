#1672. Richest Customer Wealth

"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
"""
def maximumWealth(self, accounts: list[list[int]]) -> int:
    mx = sum(accounts[0])

    for i in range(1,len(accounts)):
        if sum(accounts[i])>mx:
            mx = sum(accounts[i])
    return mx