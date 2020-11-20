

def two_sum(nums: list, target: int) -> list:

    results = []
    data = {}

    for k, v in enumerate(nums):
        complement = target - v
        if complement in data:
            results.append(k)
            results.append(data[complement])
        data[v] = k

    return results
