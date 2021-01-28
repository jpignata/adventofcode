import { numbers } from "../../ts/input.ts";

function twoSum(values: number[], target: number, lo: number = 0): number {
  let hi = values.length - 1;

  while (lo < hi) {
    const sum = values[lo] + values[hi];

    if (sum < target) {
      lo += 1;
    } else if (sum > target) {
      hi -= 1;
    } else {
      return values[lo] * values[hi];
    }
  }

  return -1;
}

function threeSum(values: number[], target: number): number {
  for (const [idx, value] of values.entries()) {
    const candidate = twoSum(values, target - value, idx + 1);

    if (candidate !== -1) {
      return candidate * value;
    }
  }

  return -1;
}

const values = (await numbers()).sort();

console.log("Part 1:", twoSum(values, 2020));
console.log("Part 2:", threeSum(values, 2020));
