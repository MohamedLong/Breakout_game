import time
from turtle import Screen
from board import Board
from ball import Ball
from score import Score
from targets import Targets

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=1000)
screen.title("Breakout Game")
screen.tracer(0)  # this to stop the animation


board = Board((0, -250))
ball = Ball()
score = Score()
bricks = Targets()
bricks.create_bricks()


def motion(event):
    mouse_x = event.x - screen.window_width() / 2
    board.goto(mouse_x, -250)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    canvas = screen.getcanvas()
    canvas.bind('<Motion>', motion)

    # Detect collision with board
    if ball.ycor() < -250 and ball.distance(board) < 60:
        ball.bounce_z()

    # Detect collision with UP wall
    if ball.ycor() > 290:
        ball.bounce_y()

    if ball.ycor() < -300:
        ball.reset_position()
        score.update_lives()
        if score.lives == 0:
            score.game_over()
            game_is_on = False

    # Detect collision with Right and Left wall
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    for brick in bricks.all_targets:
        if ball.distance(brick) < 35:
            ball.bounce_y()
            brick.hideturtle()
            bricks.all_targets.remove(brick)
            score.point()
screen.mainloop()
