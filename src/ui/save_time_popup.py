
from tkinter import Tk, messagebox, ttk
from services.statistic_service import statistic_service


class SaveTimePopup:
    """
    Class that shows the save time popup.
    """

    def __init__(self, time, difficulty, date, show_game):
        """
         Class constructor for the save time popup. Initializes and shows the popup.

         Args:
                 time: time in which the game was completed in seconds.
                 difficulty: The difficulty of the completed game.
                 date: The date of completion.
                 show_game: function to show the game window.
        """
        self.time = time
        self.difficulty = difficulty
        self.date = date
        self.name = None
        self._show_game = show_game

        self._root = Tk()
        self._root.title("Save Time")
        self._root.geometry("+811+439")
        self._style = ttk.Style()
        self._style.configure("TFrame", background="#FFCCCC")
        self._root.eval("tk::PlaceWindow . center")

        self._frame = ttk.Frame(master=self._root)

        self._add_widgets()
        self._frame.pack()

        self._root.mainloop()

    def _add_widgets(self):
        label = ttk.Label(master=self._frame, text="Name:",
                          background="#FFCCCC")
        label.grid(row=0, column=0, padx=5, pady=5)
        entry = ttk.Entry(master=self._frame)
        entry.grid(row=0, column=1, padx=5, pady=5)
        save_button = ttk.Button(
            master=self._frame, text="Save", command=self._save)
        save_button.grid(row=1, column=0, padx=5, pady=5)
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._cancel)
        cancel_button.grid(row=1, column=1, padx=5, pady=5)

    def _save(self):
        self.name = self._frame.children["!entry"].get()
        if self.name == "":
            self._display_error_message()
        else:
            statistic_service.create_statistic(
                self.name, self.time, self.difficulty, self.date)
            self._root.destroy()
            self._show_game()

    def _cancel(self):
        self._root.destroy()
        self._show_game()

    def _display_error_message(self):
        messagebox.showerror("Error", "Input a name!")
