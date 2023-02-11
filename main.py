from grid import Grid
from shell import *

def main():
    print(HELP_TEXT)

    grid = Grid()
    grid.render_grid()

    exit = False

    while not exit:
        try:
            exit = shell(grid)
        except KeyboardInterrupt:
            quit()

if __name__ == "__main__":
    main()