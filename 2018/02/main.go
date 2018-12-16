package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

const file = "./input.txt"

func main() {
	var boxIDsWithTwoIdenticalChars, boxIDsWithThreeIdenticalChars int

	boxIDs := make([]string, 0)
	file, err := os.Open(file)

	check(err)

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		boxIDs = append(boxIDs, scanner.Text())
	}

	for _, boxID := range boxIDs {
		var hasTwoIdenticalChars, hasThreeIdenticalChars bool

		s := strings.Split(boxID, "")
		sort.Sort(sort.StringSlice(s))

		for _, c := range s {
			switch strings.Count(boxID, c) {
			case 2:
				hasTwoIdenticalChars = true
			case 3:
				hasThreeIdenticalChars = true
			}
		}

		if hasTwoIdenticalChars {
			boxIDsWithTwoIdenticalChars += 1
		}

		if hasThreeIdenticalChars {
			boxIDsWithThreeIdenticalChars += 1
		}
	}

	fmt.Printf("Part 1: %d\n", boxIDsWithTwoIdenticalChars*boxIDsWithThreeIdenticalChars)

	for _, boxID := range boxIDs {
		s1 := strings.Split(boxID, "")

		for i := 0; i < len(boxIDs); i++ {
			diffs := 0

			s2 := strings.Split(boxIDs[i], "")

			for idx, c := range s1 {
				if c != s2[idx] {
					diffs += 1
				}
			}

			if diffs == 1 {
				fmt.Printf("Part 2: %s %s\n", strings.Join(s1, ""), strings.Join(s2, ""))
				os.Exit(0)
			}

		}
	}

}

func check(err error) {
	if err != nil {
		panic(err)
	}
}
