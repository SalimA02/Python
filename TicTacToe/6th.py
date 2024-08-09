import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("800x800")
        self.window.configure(bg="lightblue")
        self.player_turn = "X"

        self.turn_label = tk.Label(self.window, text="Player X's Turn", font=("Arial", 24), bg="lightblue")
        self.turn_label.pack(pady=20)

        self.frame = tk.Frame(self.window, bg="gray")
        self.frame.pack(pady=100)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.frame, command=lambda row=i, column=j: self.click(row, column), height=3, width=6, font=("Arial", 24), bg="white")
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.restart_button = tk.Button(self.window, text="Restart", command=self.restart, font=("Arial", 18), bg="white")
        self.restart_button.pack(pady=20)

    def click(self, row, column):
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.check_win():
                self.game_over()
            elif self.check_draw():
                self.draw()
            else:
                self.player_turn = "O" if self.player_turn == "X" else "X"
                self.turn_label['text'] = f"Player {self.player_turn}'s Turn"

    def check_win(self):
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button['text'] == "":
                    return False
        return True

    def game_over(self):
        for row in self.buttons:
            for button in row:
                button['state'] = 'disabled'
        self.turn_label['text'] = f"Player {self.player_turn} wins!"
        self.window.title(f"Player {self.player_turn} wins!")

    def draw(self):
        for row in self.buttons:
            for button in row:
                button['state'] = 'disabled'
        self.turn_label['text'] = "It is a draw!"
        self.window.title("It is a draw!")

    def restart(self):
        for row in self.buttons:
            for button in row:
                button['text'] = ""
                button['state'] = 'normal'
        self.player_turn = "X"
        self.turn_label['text'] = "Player X's Turn"
        self.window.title("Tic Tac Toe")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()