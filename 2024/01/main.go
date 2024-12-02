package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func task1(arrayA, arrayB []int) {
	sort.Ints(arrayA)
	sort.Ints(arrayB)

	var sum int
	for i := 0; i < len(arrayA); i++ {
		diff := int(math.Abs(float64(arrayA[i] - arrayB[i])))
		sum += diff
	}

	fmt.Printf("[Task1] Sum of absolute differences: %d\n", sum)
}

func task2(arrayA, arrayB []int) {
	countMap := make(map[int]int)
	for _, value := range arrayB {
		countMap[value]++
	}

	var sum int
	for i := 0; i < len(arrayA); i++ {
		sum += arrayA[i] * countMap[arrayA[i]]
	}

	fmt.Printf("[Task2] Similarity score: %d\n", sum)
}

func readFile(filePath string) ([]int, []int, error) {
	var arrayA, arrayB []int
	file, err := os.Open(filePath)
	if err != nil {
		return nil, nil, fmt.Errorf("failed to open file: %v", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		columns := strings.Fields(line)
		if len(columns) != 2 {
			fmt.Printf("Skipping invalid line: %s\n", line)
			continue
		}

		numA, err := strconv.Atoi(columns[0])
		if err != nil {
			return nil, nil, fmt.Errorf("error parsing number in column A: %v", err)
		}

		numB, err := strconv.Atoi(columns[1])
		if err != nil {
			return nil, nil, fmt.Errorf("error parsing number in column B: %v", err)
		}

		arrayA = append(arrayA, numA)
		arrayB = append(arrayB, numB)
	}

	if err := scanner.Err(); err != nil {
		return nil, nil, fmt.Errorf("error reading file: %v", err)
	}

	return arrayA, arrayB, nil
}

func main() {
	// Specify the file path
	filePath := "input.txt"

	// Read the file and get the arrays
	arrayA, arrayB, err := readFile(filePath)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Execute the tasks
	task1(arrayA, arrayB)
	task2(arrayA, arrayB)
}
