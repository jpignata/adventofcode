package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
)

var (
	patternRule  = regexp.MustCompile(`([#\.]{5}) => ([#\.])`)
	patternState = regexp.MustCompile(`initial state: ([#\.]+)`)
)

func main() {
	var state []string
	var next []string
	var rules []string
	var found bool
	var seen [][]string

	file, err := os.Open("input.txt")
	check(err)

	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		switch {
		case patternState.Match(scanner.Bytes()):
			matches := patternState.FindStringSubmatch(scanner.Text())
			state = strings.Split(matches[1], "")
		case patternRule.Match(scanner.Bytes()):
			matches := patternRule.FindStringSubmatch(scanner.Text())

			if matches[2] == "#" {
				rules = append(rules, matches[1])
			}
		}
	}

	prevtotal := 0

	for i := 0; i < 500; i++ {
		next = []string{}

		for pi, pot := range state {
			found = false
			combination := []string{}

			if pi-2 > 0 {
				combination = append(combination, state[pi-2])
			} else {
				combination = append(combination, ".")
			}

			if pi-1 > 0 {
				combination = append(combination, state[pi-1])
			} else {
				combination = append(combination, ".")
			}

			combination = append(combination, pot)

			if pi+1 < len(state) {
				combination = append(combination, state[pi+1])
			} else {
				combination = append(combination, ".")
			}

			if pi+2 < len(state) {
				combination = append(combination, state[pi+2])
			} else {
				combination = append(combination, ".")
			}

			for _, rule := range rules {
				if strings.Join(combination, "") == rule {
					next = append(next, "#")
					found = true
					break
				}
			}

			if !found {
				next = append(next, ".")
			}
		}

		state = next
		seen = append(seen, next)

		total := 0

		for i, pot := range next {
			if pot == "#" {
				total += i - 3
			}
		}

		fmt.Printf("Total %d: %d (%d)\n", i+1, total, prevtotal-total)
		prevtotal = total
	}
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}
