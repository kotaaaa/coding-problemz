package main

import "fmt"

func main() {
	var N int
	var K int
	fmt.Scan(&N)
	fmt.Scan(&K)

	var maxVal int
	maxVal = 0
	Pz := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&Pz[i])
		if maxVal < Pz[i] {
			maxVal = Pz[i]
		}
	}

	vals := make([]float64, maxVal)
	var sum float64
	for i := 1; i <= maxVal; i++ {
		sum += float64(i)
		vals[i-1] = sum / float64(i)
	}

	var maxSum float64
	maxSum = 0
	var ans float64
	ans = 0
	for i := 0; i < N; i++ {
		if i < K {
			maxSum += vals[Pz[i]-1]
		} else {
			maxSum -= vals[Pz[i-K]-1]
			maxSum += vals[Pz[i]-1]
		}
		if ans < maxSum {
			ans = maxSum
		}
		// fmt.Println(ans)
	}
	fmt.Println(ans)
	// fmt.Println(maxJump)
}

// 	maxJump := 0
// 	tmpJump := 0
// 	for i := 0; i < N-1; i++ {
// 		if Hz[i] >= Hz[i+1] {
// 			tmpJump++
// 		} else {
// 			tmpJump = 0
// 		}
//
// 		if tmpJump > maxJump {
// 			maxJump = tmpJump
// 		}
// 	}
