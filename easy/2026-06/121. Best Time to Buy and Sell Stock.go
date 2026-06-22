package main

func maxProfit(prices []int) int {
	n := len(prices)
	curMin := prices[0]
	dp := 0
	for i := 1; i < n; i++ {
		dp = max(prices[i]-curMin, dp)
		curMin = min(curMin, prices[i])
	}
	return dp
}
