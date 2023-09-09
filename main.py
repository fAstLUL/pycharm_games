import time
import turtle as t
import snake as s
from food import Food
from score import Score

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = s.Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detect collision with food. (If snake head is within 15 pixels of food center pixel)
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.score_up()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
        # If head collides with any segment in the tail:
        # trigger game_over

screen.exitonclick()
