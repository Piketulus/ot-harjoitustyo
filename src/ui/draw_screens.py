import pygame
from .button import Button


class DrawScreens:
    """
    Class that draws the start screen and the wait screen.
    """

    def __init__(self, increase_difficulty, decrease_difficulty, sudoku_screen, quit_screen, difficulty, show_statistics_view):
        """
         Initialize the drawer.

         Args:
                 increase_difficulty: function to increase the difficulty of the sudoku.
                 decrease_difficulty: function to decrease the difficulty of the sudoku.
                 sudoku_screen: function to display the sudoku screen.
                 quit_screen: function to quit the game.
                 difficulty: The difficulty of the game.
                 show_statistics_view: function to show the statistics view.
        """

        self._increase_difficulty = increase_difficulty
        self._decrease_difficulty = decrease_difficulty
        self._sudoku_screen = sudoku_screen
        self._quit_screen = quit_screen
        self.objects = []
        self._font = pygame.font.SysFont("comicsans", 30)
        self._difficulty = difficulty
        self._show_statistics_view = show_statistics_view

    def draw_wait_screen(self, screen):
        """
         Draws the loading screen while the sudoku is being generated.

         Args:
                 screen: the pygame screen to draw on
        """

        screen.fill((255, 192, 203))

        screen.blit(self._font.render(
            "Generating your sudoku,", 1, (0, 0, 0)), (100, 200))
        screen.blit(self._font.render(
            "please wait...", 1, (0, 0, 0)), (180, 300))

        pygame.display.flip()

    def draw_start_screen(self, screen):
        """
         Draws the start screen / main menu.

         Args:
                 screen: The screen to draw on
        """

        self.objects = []

        screen.fill((255, 192, 203))

        self.objects.append(Button(175, 100, 200, 50, "Start", (255, 255, 255),
                                   (200, 200, 200), (0, 0, 0), self._font, self._sudoku_screen))
        self.objects.append(Button(175, 550, 200, 50, "Quit", (255, 255, 255),
                                   (200, 200, 200), (0, 0, 0), self._font, self._quit_screen))
        self.objects.append(Button(175, 450, 200, 50, "Saved Times", (255, 255, 255),
                                   (200, 200, 200), (0, 0, 0), self._font, self._show_statistics_view))

        screen.blit(self._font.render(
            "Difficulty:", 1, (0, 0, 0)), (200, 200))
        screen.blit(self._font.render(
            str(self._difficulty), 1, (0, 0, 0)), (250, 270))

        up = "/\|"

        self.objects.append(Button(
            325, 250, 50, 50, up[:-1], (255, 255, 255), (200, 200, 200), (0, 0, 0), self._font, self._increase_difficulty))
        self.objects.append(Button(325, 300, 50, 50, "\/", (255, 255, 255),
                                   (200, 200, 200), (0, 0, 0), self._font, self._decrease_difficulty))
