package main

import "testing"

func TestSolve(t *testing.T) {
	tests := []struct {
		name      string
		input     string
		wantPart1 int
		wantPart2 int
	}{
		{name: "balanced parens", input: "(())", wantPart1: 0, wantPart2: -1},
		{name: "alternating parens", input: "()()", wantPart1: 0, wantPart2: -1},
		{name: "three opening", input: "(((", wantPart1: 3, wantPart2: -1},
		{name: "nested opening", input: "(()(()(", wantPart1: 3, wantPart2: -1},
		{name: "net three opening", input: "))(((((", wantPart1: 3, wantPart2: 1},
		{name: "basement level 1", input: "())", wantPart1: -1, wantPart2: 3},
		{name: "immediate basement", input: ")", wantPart1: -1, wantPart2: 1},
		{name: "fifth character basement", input: "()())", wantPart1: -1, wantPart2: 5},
		{name: "basement level 3", input: ")))", wantPart1: -3, wantPart2: 1},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			gotPart1, gotPart2 := Solve(tc.input)
			if gotPart1 != tc.wantPart1 || gotPart2 != tc.wantPart2 {
				t.Errorf("Solve(%q) = (%d, %d); want (%d, %d)",
					tc.input, gotPart1, gotPart2, tc.wantPart1, tc.wantPart2)
			}
		})
	}
}
