package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	data, err := os.ReadFile("01/input.txt")

	if err != nil {
		log.Fatal(err)
	}

	firstMinusOneLocation := -1
	currentLocation := 0

	for i, b := range data {
		switch b {
		case '(':
			currentLocation++
		case ')':
			currentLocation--
		}

		if firstMinusOneLocation == -1 && currentLocation == -1 {
			firstMinusOneLocation = i + 1
		}
	}

	fmt.Println("Task 1: ", currentLocation)
	fmt.Println("Task 2: ", firstMinusOneLocation)
}
