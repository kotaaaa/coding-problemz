package main

import "fmt"

func checkSlice(x int) {
	a := []int{10, 20, 30}
	fmt.Println(cap(a))
	a = append(a, 3)
	fmt.Println("a", a)
	fmt.Println(cap(a))
	// b := a[:2]
	// fmt.Println(cap(a), cap(b))
	// fmt.Println(a, b)
	// a[0] = 100
	// fmt.Println(a, b)
}

func main() {
	checkSlice(-101)
}
