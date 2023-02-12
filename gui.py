import pygame
from grid import Grid

def main():
    ## VARS ##
    CELL_WIDTH = 60
    GRID_LINE_WIDTH = 1

    FPS = 60

    WIN_RES = CELL_WIDTH * 9 + GRID_LINE_WIDTH + 4

    ## INIT ##
    pygame.init()

    SCREEN = pygame.display.set_mode((WIN_RES, WIN_RES))
    FONT = pygame.font.SysFont("firacode.ttf", 30)

    pygame.display.set_caption("Sudoku Solver")
    clock = pygame.time.Clock()
    grid = Grid()

    def render(_grid):
        SCREEN.fill((10, 10, 10))

        for x, row in enumerate(_grid):
            for y, cell in enumerate(row):
                grid_x = 4 if x % 3 == 0 else 2
                grid_y = 4 if y % 3 == 0 else 2

                cell_rect = pygame.Rect(
                    (x * CELL_WIDTH) + grid_x * GRID_LINE_WIDTH,
                    (y * CELL_WIDTH) + grid_y * GRID_LINE_WIDTH,
                    CELL_WIDTH - (grid_x * GRID_LINE_WIDTH),
                    CELL_WIDTH - (grid_y * GRID_LINE_WIDTH))

                pygame.draw.rect(SCREEN,
                                 (255, 255, 255) if cell.selected == False else
                                 (240, 240, 240), cell_rect)

                ## TEXT ##
                color = (0, 0, 0) if cell.selected == True else (100, 100, 100)
                text = FONT.render(cell.as_string(), True, color)
                text_rect = text.get_rect()
                text_rect.center = ((x * CELL_WIDTH) +
                                    grid_x * GRID_LINE_WIDTH +
                                    (CELL_WIDTH // 2), (y * CELL_WIDTH) +
                                    grid_y * GRID_LINE_WIDTH +
                                    (CELL_WIDTH // 2))

                SCREEN.blit(text, text_rect)

        pygame.display.update()

    selected = ()
    selected_temp = ()
    key = -1

    while True:
        clock.tick(240)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                selected = (min(pos[1] // CELL_WIDTH, 8), min(pos[0] // CELL_WIDTH, 8))

                grid.grid[selected[1]][selected[0]].selected = True

                if selected_temp != selected and len(selected_temp) > 0:
                    grid.grid[selected_temp[1]][
                        selected_temp[0]].selected = False

                selected_temp = selected

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    key = 0
                elif event.key == pygame.K_1:
                    key = 1
                elif event.key == pygame.K_2:
                    key = 2
                elif event.key == pygame.K_3:
                    key = 3
                elif event.key == pygame.K_4:
                    key = 4
                elif event.key == pygame.K_5:
                    key = 5
                elif event.key == pygame.K_6:
                    key = 6
                elif event.key == pygame.K_7:
                    key = 7
                elif event.key == pygame.K_8:
                    key = 8
                elif event.key == pygame.K_9:
                    key = 9

                if event.key == pygame.K_SPACE and grid.get_filled_count(
                ) >= 17:
                    grid.solve_sudoku(run_per_ittr=render, fps=FPS)

                if key != -1:
                    if grid.is_valid(selected, key):
                        grid.grid[selected[1]][selected[0]].value = key
                    elif key == 0:
                        grid.grid[selected[1]][selected[0]].value = 0


        render(grid.grid)