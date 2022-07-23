from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.game_is_on = True
        self.winner = ''

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f'Player1: {self.l_score}', align='center',
                   font=('Courier', 22, 'normal'))
        self.goto(100, 200)
        self.write(f'Player2:{self.r_score}', align='center',
                   font=('Courier', 22, 'normal'))

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def check_score(self):
        if self.l_score >= 5 or self.r_score >= 5:
            self.game_is_on = False
            self.goto(0, 0)
            if self.l_score >= 5:
                self.winner = 'Left'
            else:
                self.winner = 'Right'
            self.write(f"Winner is {self.winner}", align='center',
                       font=('Courier', 50, 'normal'))
