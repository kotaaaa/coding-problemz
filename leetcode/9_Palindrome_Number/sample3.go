package main

import "fmt"

func checkSlice(x int) {
	// 構造体の内部のフィールドが書き換わる。
	// sli := []struct{ N int }{{N: 10}, {N: 20}}
	sli := []struct {
		N    int
		name string
	}{{N: 10, name: "taro"},
		{N: 20, name: "keiko"}}
	for i := range sli {
		sli[i].N *= 10
		sli[i].name = "taro2"
	}
	fmt.Println("1:", sli)

	// ポインタを一回コピーしている。
	sli = []struct {
		N    int
		name string
	}{
		{N: 10, name: "taro"},
		{N: 20, name: "keiko"},
	}
	for _, v := range sli {
		v.N *= 10
		v.name = "taro2"
	}
	fmt.Println("2:", sli)
}

func main() {
	checkSlice(-101)
}
