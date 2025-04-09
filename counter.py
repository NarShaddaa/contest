def find_winner(n: int, k: int) -> int:
    if n == 1:
        return 1
    return (find_winner(n - 1, k) + k - 1) % n + 1


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print(find_winner(n, k))
