import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-Нолики")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            button = tk.Button(frame, text="", font=('normal', 20, 'bold'), height=3, width=6,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.status_label = tk.Label(self.root, text=f"Ходит игрок: {self.current_player}", font=('normal', 15, 'bold'))
        self.status_label.pack()

    def on_button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Игра окончена", f"Игрок {self.current_player} победил!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Игра окончена", "Ничья!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Ходит игрок: {self.current_player}")

    def check_winner(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.status_label.config(text=f"Ходит игрок: {self.current_player}")

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()