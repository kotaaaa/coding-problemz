package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	Hz := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&Hz[i])
	}

	maxJump := 0
	tmpJump := 0

	for i := 0; i < N-1; i++ {
		if Hz[i] >= Hz[i+1] {
			tmpJump++
		} else {
			tmpJump = 0
		}

		if tmpJump > maxJump {
			maxJump = tmpJump
		}
	}
	fmt.Println(maxJump)
}
