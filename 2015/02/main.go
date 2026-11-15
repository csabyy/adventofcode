package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func SolveBox(line string) (int, int, error) {
	dimensions := strings.Split(line, "x")
	if len(dimensions) != 3 {
		return 0, 0, fmt.Errorf("invalid dimension format: %q", line)
	}

	l, err1 := strconv.Atoi(dimensions[0])
	w, err2 := strconv.Atoi(dimensions[1])
	h, err3 := strconv.Atoi(dimensions[2])
	if err1 != nil || err2 != nil || err3 != nil {
		return 0, 0, fmt.Errorf("parsing dimensions for line %q: %v, %v, %v", line, err1, err2, err3)
	}

	side1 := l * w
	side2 := w * h
	side3 := h * l
	minSide := min(side1, side2, side3)
	surfaceArea := 2*side1 + 2*side2 + 2*side3 + minSide

	perim1 := 2 * (l + w)
	perim2 := 2 * (w + h)
	perim3 := 2 * (h + l)
	minPerim := min(perim1, perim2, perim3)
	volume := l * w * h
	ribbon := minPerim + volume

	return surfaceArea, ribbon, nil
}

func Solve(input string) (int, int, error) {
	totalSurface := 0
	totalRibbon := 0

	scanner := bufio.NewScanner(strings.NewReader(input))
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line == "" {
			continue
		}

		surface, ribbon, err := SolveBox(line)
		if err != nil {
			return 0, 0, err
		}

		totalSurface += surface
		totalRibbon += ribbon
	}

	if err := scanner.Err(); err != nil {
		return 0, 0, fmt.Errorf("reading input: %w", err)
	}

	return totalSurface, totalRibbon, nil
}

func main() {
	data, err := os.ReadFile("02/input.txt")
	if err != nil {
		log.Fatalf("reading file: %v", err)
	}

	totalSurface, totalRibbon, err := Solve(string(data))
	if err != nil {
		log.Fatalf("solving puzzle: %v", err)
	}

	fmt.Println("Total required surface:", totalSurface)
	fmt.Println("Total required bow:", totalRibbon)
}
