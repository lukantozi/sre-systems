import sys

def solve(data: str) -> str:
    it = iter(data.split())
    numbers = list(map(int, it))

    nums = numbers[:len(numbers)-1]
    sum = numbers[-1]

    seen = {}
    for i, num in enumerate(nums):
        y = sum - num
        if y in seen:
            return f"{seen[y]} {i}"
        seen[num] = i
    return ""

def main() -> None:
    data = sys.stdin.read()
    sys.stdout.write(solve(data))

if __name__ == "__main__":
    main()
