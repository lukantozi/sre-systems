import sys

def solve(data: str) -> str:
    nums = list(map(int, iter(data.split())))
    target = nums.pop()
    k = 0
    for i, n in enumerate(nums):
        curr_sum = n
        for m in nums[i+1:]:
            curr_sum += m
            if curr_sum == target:
                k += 1
    return str(k)

def main() -> None:
    data = sys.stdin.read()
    sys.stdout.write(solve(data))

if __name__ == "__main__":
    main()
