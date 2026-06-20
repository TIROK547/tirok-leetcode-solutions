package main

import "fmt"

func main() {
	list := []int{1, 2, 3, 1, 2, 3}
	res := containsNearbyDuplicate(list, 2)
	fmt.Println(res)
}
func containsNearbyDuplicate(nums []int, k int) bool {
	seen := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		if _, exists := seen[nums[i]]; exists {
			if i-seen[nums[i]] <= k {
				return true
			}
		}
		seen[nums[i]] = i
	}
	return false
}
