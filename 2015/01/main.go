package main

import (
	"fmt"
	"log"
	"os"
)

func Solve(input string) (int, int) {
	floor := 0
	firstBasementIndex := -1

	for i, ch := range input {
		switch ch {
		case '(':
			floor++
		case ')':
			floor--
		}

		if firstBasementIndex == -1 && floor == -1 {
			firstBasementIndex = i + 1
		}
	}

	return floor, firstBasementIndex
}

func main() {
	data, err := os.ReadFile("01/input.txt")
	if err != nil {
		log.Fatalf("failed to read input: %v", err)
	}

	part1, part2 := Solve(string(data))
	fmt.Println("Task 1:", part1)
	fmt.Println("Task 2:", part2)
}
