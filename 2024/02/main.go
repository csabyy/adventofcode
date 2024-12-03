package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func isSafe(arr []int, isLastAttempt bool, skipIndex int) bool {
	isDirectionSet := false
	var isAscending bool
	for i := 0; i < len(arr)-1; i++ {
		if i == skipIndex {
			continue
		}

		j := i + 1
		if j == skipIndex {
			j++
		}

		if !isDirectionSet {
			isAscending = arr[i] < arr[j]
			isDirectionSet = true
		}

		var diff = math.Abs(float64(arr[i] - arr[j]))

		if arr[i] > arr[j] && isAscending || arr[i] < arr[j] && !isAscending || diff < 1 || diff > 3 {
			if !isLastAttempt {
				if i == len(arr)-2 {
					return true
				}

				if i == 1 && isSafe(arr, true, 0) {
					return true
				}

				return isSafe(arr, true, i) || isSafe(arr, true, j)
			}
			return false
		}
	}
	return true
}

func task2(arr [][]int) {
	safeCount := 0
	for _, row := range arr {
		if isSafe(row, false, -1) {
			safeCount++
		}
	}

	fmt.Printf("[TASK2] Number of safe rows: %d\n", safeCount)

}

func task1(arr [][]int) {
	safeCount := 0
	for _, row := range arr {
		if isSafe(row, true, -1) {
			safeCount++
		}
	}

	fmt.Printf("[TASK1] Number of safe rows: %d\n", safeCount)
}

func main() {
	file, err := os.Open("02/data.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var arr [][]int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		var row []int
		for _, part := range parts {
			num, err := strconv.Atoi(part)
			if err != nil {
				fmt.Println("Error converting to integer:", err)
				return
			}
			row = append(row, num)
		}
		arr = append(arr, row)
	}

	task1(arr)
	task2(arr)
}
