package main

import (
	"fmt"
	"sort"
)

const (
	serial   = 7347
	gridSize = 300
)

func main() {
	grid := buildGrid(gridSize)
	index := buildIndex(grid)
	results := findLargestSquares(grid, index)

	fmt.Printf("%d,%d\n", results[3][0], results[3][1])

	sort.Slice(results, func(i, j int) bool {
		return results[i][3] > results[j][3]
	})

	fmt.Printf("%d,%d,%d\n", results[0][0], results[0][1], results[0][2])
}

func buildGrid(gridSize int) [][]int {
	grid := make([][]int, gridSize)

	for y := 0; y < gridSize; y++ {
		row := make([]int, gridSize)

		for x := 0; x < gridSize; x++ {
			rackID := x + 10
			powerLevel := ((rackID * y) + serial) * rackID

			row[x] = (powerLevel / 100 % 10) - 5
		}

		grid[y] = row
	}

	return grid
}

func buildIndex(grid [][]int) [][]int {
	index := make([][]int, len(grid))

	for y, row := range grid {
		index[y] = make([]int, len(grid))

		for x, cell := range row {
			var a, b, c int

			if y-1 >= 0 {
				a = index[y-1][x]

				if x-1 >= 0 {
					b = index[y][x-1]
					c = index[y-1][x-1]
				}
			}

			index[y][x] = cell + a + b - c
		}
	}

	return index
}

func findLargestSquares(grid, index [][]int) [][]int {
	results := make([][]int, gridSize)

	for s := 0; s <= gridSize; s++ {
		for y, row := range grid {
			for x, _ := range row {
				if x+s >= gridSize || y+s >= gridSize {
					break
				}

				a := index[y][x]
				b := index[y][x+s]
				c := index[y+s][x]
				d := index[y+s][x+s]
				p := d + a - b - c

				if len(results[s]) == 0 || p > results[s][3] {
					results[s] = []int{x + 1, y + 1, s, p}
				}
			}
		}
	}

	return results
}
