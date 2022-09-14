package main

import (
	"fmt"
	"strings"
)

// key map 使い方
func checkSlice(x int) {
	m := map[string]int{"x": 10, "y": 20}
	println(m["x"])
	m["z"] = 30
	n, ok := m["z"]
	println(n, ok)
	delete(m, "z")
	n, ok = m["z"]
	println(n, ok)
	println(len(m))

	counts := map[string]int{}

	str := "dog dog dog cat dog"
	for _, s := range strings.Split(str, " ") {
		counts[s]++
	}
	fmt.Println(counts, counts["dog"], counts["cat"], counts["fox"])

	flag := map[string]bool{}
	flag["dog"] = true
	if flag["dog"] {
		println("dog!")
	}
	if flag["cat"] {
		println("cat!")
	}

	var sum int
	for i := 1; i <= 10; i++ {
		sum += i
	}
	println(sum)

}

func main() {
	checkSlice(-101)
}
