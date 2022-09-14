package main

func main() {
	n, m := swap(10, 20)
	println(n, m)
}

func swap(x int, y int) (int, int) {
	return y, x
}
