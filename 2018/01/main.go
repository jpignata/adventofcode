package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const file = "./input.txt"

func main() {
	var frequency int64

	changes := make([]int64, 0)
	seen := make(map[int64]struct{}, 0)
	file, err := os.Open(file)

	check(err)

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		change, err := strconv.ParseInt(scanner.Text(), 10, 64)
		check(err)
		changes = append(changes, change)
	}

	for i := 0; true; i++ {
		for _, change := range changes {
			frequency += change

			if _, ok := seen[frequency]; ok {
				fmt.Printf("Duplicate Frequency: %d\n", frequency)
				os.Exit(0)
			}

			seen[frequency] = struct{}{}
		}

		fmt.Printf("Iteration %d: %d\n", i+1, frequency)
	}
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}
