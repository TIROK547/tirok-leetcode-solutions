package main

import "fmt"

func main() {
	longestPalindromeSubseq("total")
}

func longestPalindromeSubseq(s string) int {
	n := len(s)
	prev := make([]int, n)
	curr := make([]int, n)
	for i := 0; i < 0; i++ {
		prev = append(prev, 0)
		curr = append(curr, 0)
	}
	fmt.Println(prev, curr)
	return 0
}
