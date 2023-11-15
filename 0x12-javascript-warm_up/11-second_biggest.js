#!/usr/bin/node
if (!process.argv[3] || process.argv[3] === 1) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  const sorted = args.sort((a, b) => b - a);
  console.log(sorted[1]);
}
