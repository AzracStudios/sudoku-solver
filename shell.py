HELP_TEXT = "List of inputs:\n  - 'h' : Print this help screen\n  - 's' : Solve board\n  - 'e' : Exit\n  - 'c' : Clear Board\n  -  X (int, 0 < x < 10)  Y (int, 0 < y < 10)  Val (int, 0 < val < 10)\n"


def shell(grid):
    inp = input("> ").lower()

    if inp == "s":
        grid.solve_sudoku()
        grid.render_grid()

    elif inp == "e":
        return True

    elif inp == "c":
        grid.grid = grid.create_grid()
        print("Cleared Board\n")
        grid.render_grid()

    elif inp == "h":
        print(HELP_TEXT)

    else:
        inp = inp.replace(" ", "")

        if len(inp) != 3:
            print("Invalid Input!\n")

        else:
            x, y, v = int(inp[0]), int(inp[1]), int(inp[2])

            if grid.is_valid((x - 1, y - 1), v):
                grid.grid[y - 1][x - 1].value = v
                print(f"Put {v} in spot ({x}, {y})\n")
                grid.render_grid()

            else:
                print(f"Cannot put {v} in spot ({x}, {y}) : INVALID\n")

    return False
