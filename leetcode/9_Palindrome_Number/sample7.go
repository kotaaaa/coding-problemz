package main

// https://docs.google.com/presentation/d/1DtWB-8FcnNb9asxSpIaOLYbAEc9OjBAwMLNxKnPA8pc/edit#slide=id.g4cbe4d134e_0_324
func main() {
	n, m := 10, 20
	swap2(&n, &m)
	println(n, m)
}

func swap2(x *int, y *int) { // x,y: int のポインタ型
	println(x, y)
	*y, *x = *x, *y
}
