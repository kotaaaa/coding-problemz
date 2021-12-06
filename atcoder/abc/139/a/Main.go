package main

import "fmt"

func main() {
	// fmt.Printf("Hello world\n")
	var s, t string
	fmt.Scan(&s, &t)
	// fmt.Println("s " + s + " t " + t)
	cnt := 0
	for i := 0; i < len(s); i++ {
		// fmt.Println(s[i], t[i])
		if s[i] == t[i] {
			cnt += 1
		}
	}
	fmt.Println(cnt)
}
