package main

import (
	"fmt"
	"log"
	"os"
)

type Point struct {
	x, y int
}

type Santa struct {
	pos Point
}

func (s *Santa) Move(dir rune) {
	switch dir {
	case '^':
		s.pos.y++
	case 'v':
		s.pos.y--
	case '>':
		s.pos.x++
	case '<':
		s.pos.x--
	}
}

func Solve(input string) (int, int) {
	visitedPart1 := map[Point]bool{{x: 0, y: 0}: true}
	visitedPart2 := map[Point]bool{{x: 0, y: 0}: true}

	soloSanta := &Santa{}
	teamSantas := [2]*Santa{{}, {}}

	for i, ch := range input {

		soloSanta.Move(ch)
		visitedPart1[soloSanta.pos] = true

		activeSanta := teamSantas[i%2]
		activeSanta.Move(ch)
		visitedPart2[activeSanta.pos] = true
	}

	return len(visitedPart1), len(visitedPart2)
}

func main() {
	data, err := os.ReadFile("03/input.txt")
	if err != nil {
		log.Fatalf("reading file: %v", err)
	}

	part1, part2 := Solve(string(data))
	fmt.Println("Part1:", part1)
	fmt.Println("Part2:", part2)
}
