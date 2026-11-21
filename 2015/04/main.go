package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
	"strings"
)

func main() {
	input := "yzbqklnj"
	answer1 := -1
	answer2 := -1
	for i := 1; ; i++ {
		md5Sum := md5.Sum([]byte(input + strconv.Itoa(i)))
		txt := hex.EncodeToString(md5Sum[:])

		if answer1 == -1 && strings.HasPrefix(txt, "00000") {
			answer1 = i
		}

		if strings.HasPrefix(txt, "000000") {
			answer2 = i
			break
		}
	}

	fmt.Println("Part 1: ", answer1)
	fmt.Println("Part 2: ", answer2)
}
