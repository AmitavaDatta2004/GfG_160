class Solution:
    def maximumProfit(self, prices):
        # Initialize variables
        min_price = float('inf')  # Start with the highest possible value
        max_profit = 0            # Maximum profit is initially zero

        # Loop through each price in the array
        for price in prices:
            # Update the minimum price encountered so far
            if price < min_price:
                min_price = price
            # Calculate profit and update max_profit if the current profit is greater
            elif price - min_price > max_profit:
                max_profit = price - min_price

        # Return the maximum profit found
        return max_profit