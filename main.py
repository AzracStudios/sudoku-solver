import argparse

from grid import Grid
from shell import *


def main():
    ## ARGPARSE ##
    parser = argparse.ArgumentParser()
    parser.add_argument("--text",
                        help="Text Mode",
                        dest="text",
                        action="store_true")
    parser.add_argument("--gui",
                        help="GUI Mode",
                        dest="gui",
                        action="store_true")

    args = parser.parse_args()

    grid = Grid()

    if args.text:
        print(HELP_TEXT)
        grid.render_grid()

        exit = False

        while not exit:
            try:
                exit = shell(grid)
            except KeyboardInterrupt:
                quit()

    elif args.gui:
        from gui import main as gui_main
        gui_main()

    else:
        print("UNRECOGNIZED FLAG!")


if __name__ == "__main__":
    main()