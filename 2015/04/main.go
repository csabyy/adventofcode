package main

import (
	"crypto/md5"
	"fmt"
	"strconv"
)

func Solve(secret string) (int, int) {
	answer1 := -1
	answer2 := -1

	prefix := []byte(secret)
	buf := make([]byte, len(prefix), len(prefix)+16)
	copy(buf, prefix)

	for i := 1; ; i++ {
		data := strconv.AppendInt(buf, int64(i), 10)
		md5Sum := md5.Sum(data)

		if md5Sum[0] == 0 && md5Sum[1] == 0 {
			if answer1 == -1 && md5Sum[2] < 16 {
				answer1 = i
			}
			if md5Sum[2] == 0 {
				answer2 = i
				break
			}
		}
	}

	return answer1, answer2
}

func main() {
	part1, part2 := Solve("yzbqklnj")
	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}
