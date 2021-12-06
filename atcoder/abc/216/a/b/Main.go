package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var s string
	fmt.Scan(&s)
	arr := strings.Split(s, ".")
	int_arr1, _ := strconv.Atoi(arr[1])
	if 0 <= int_arr1 && int_arr1 < 3 {
		fmt.Println(arr[0] + "-")
	} else if 3 <= int_arr1 && int_arr1 < 7 {
		fmt.Println(arr[0] + "")
	} else {
		fmt.Println(arr[0] + "+")
	}
}
