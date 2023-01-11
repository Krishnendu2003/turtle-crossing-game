import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

logo="""___________             __  .__           _________                            .__                
\__    ___/_ __________/  |_|  |   ____   \_   ___ \_______  ____  ______ _____|__| ____    ____  
  |    | |  |  \_  __ \   __\  | _/ __ \  /    \  \/\_  __ \/  _ \/  ___//  ___/  |/    \  / ___\ 
  |    | |  |  /|  | \/|  | |  |_\  ___/  \     \____|  | \(  <_> )___ \ \___ \|  |   |  \/ /_/  >
  |____| |____/ |__|   |__| |____/\___  >  \______  /|__|   \____/____  >____  >__|___|  /\___  / 
                                      \/          \/                  \/     \/        \//_____/  """
print(logo)
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(player.move,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    if player.check_finishline():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    car_manager.move_car()
    for cars in car_manager.allcars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()