package main

import (
	"fmt"
)

func isPalindrome(x int) {
	var sum int
	sum = 5 + 6 + 3
	// avg := sum / 3
	// var avg float64 = sum / 3
	avg := float64(sum) / 3
	if avg > 4.5 {
		fmt.Println("Good")
	}
	for i, v := range []int{4, 5, 6} {
		fmt.Println(i, ": ", v)
	}

}

func main() {
	isPalindrome(-101)
}
