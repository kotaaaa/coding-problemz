package main

import (
	"fmt"
	"os"
)

func main() {
	// fmt.Printf("Hello world\n")
	var s, t int
	fmt.Scan(&s, &t)
	if t == 1 {
		fmt.Println(0)
		os.Exit(0)
	}
	// fmt.Println("s ", s, " t ", t)
	tmp := s
	cnt := 1
	for tmp < t {
		tmp += s - 1
		cnt += 1
	}
	fmt.Println(cnt)
	// cnt := 0
	// for i := 0; i < len(s); i++ {
	// 	// fmt.Println(s[i], t[i])
	// 	if s[i] == t[i] {
	// 		cnt += 1
	// 	}
	// }
	// fmt.Println(cnt)
}
