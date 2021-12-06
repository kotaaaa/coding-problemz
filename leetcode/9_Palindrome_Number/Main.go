package main

import (
	"fmt"
	"strconv"
	"strings"
)

func isPalindrome(x int) bool {
	str := strconv.Itoa(x)
	fmt.Println(str)

	slice := strings.Split(str, "")
	len_slice := len(slice)
	for i := 0; i < len_slice; i++ {
		if i >= (len_slice+1)/2 {
			break
		}
		if slice[i] != slice[len_slice-i-1] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isPalindrome(-101))
}
