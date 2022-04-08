#!/usr/bin/node
const nextMax = process.argv;
const args = [];
if (nextMax.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < nextMax.length; i++) {
    args.push(parseInt(nextMax[i]));
    args.sort((a, b) => a - b);
  }
  const index = args.length;
  const max = args[index - 2];
  console.log(max);
}
exports.nextMax = nextMax;
