package main

import "fmt"

// key map 使い方
func checkSlice(x int) {
	fs := make([]func(), 3)
	for i := range fs {
		// i := i
		fmt.Println("i: ", i)
		fs[i] = func() { fmt.Println(i) }
	}
	for _, f := range fs {
		f()
	}

	for i := 0; i < 3; i++ {
		func(i int) { fmt.Println(i) }(i)
	}
}

var ns []int

func f(n int) {

}

func main() {
	checkSlice(-101)
}
