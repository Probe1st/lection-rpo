def solve(width, height):
    print("*" * width)

    row_in_body = ""
    if width > 1:
        row_in_body = "*" + (" " * (width - 2)) + "*"
    else:
        row_in_body = "*"

    for _ in range(1, height - 1):
        print(row_in_body)

    if height > 1:
        print("*" * width)

    print()

solve(1, 1)

solve(1, 5)
solve(5, 1)
solve(2, 2)
solve(4, 4)
