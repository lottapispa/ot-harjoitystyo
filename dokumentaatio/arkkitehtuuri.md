# Arkkitehtuuri
## Ohjelman rakenne
Ohjelmassa on 8 eri luokkaa: Snake, Food, Score, Death, Fonts, KeyBoard, KeyboardEvents ja GameLoop. Luokka KeyboardEvents on tehty riippuvuuksien injektointia varten.
### Luokkakaavio

```mermaid
classDiagram
    GameLoop ..> Snake
    GameLoop ..> Food
    GameLoop ..> Score
    GameLoop ..> Death
    GameLoop ..> KeyBoard
    GameLoop ..> KeyboardEvents
    Death ..> Fonts
    class Snake{
        +int length
        +tuple color
        +tuple screen_size
        +list location
        +dict directions
        +tuple direction
        +int counter
        +int step
        +bool dead
        +head_location()
        +head_rect()
        +draw_snake()
        +turn_up()
        +turn_down()
        +turn_left()
        +turn_right()
        +move()
    }
    class Food{
        +int size
        +tuple color
        +tuple location
        +random_location()
        +draw_food()
    }
    class Score{
        +int points
        +int highscore
        +eating()
    }
    class Death{
        +snake
        +score
        +fonts
        +events
        +tuple screen_size
        +screen
        +dict directions
        +bool die_called
        +bool call_main
        +die()
        +gameover_loop()
        +reset()
    }
    class Fonts{
        +tuple font
        +tuple bigfont
        +game_over
        +points
        +time
        +highscore
        +play_again
        +quit_game
        +rendering_text()
    }
    class GameLoop{
        +caption
        +tuple screen_size
        +screen
        +snake
        +food
        +score
        +death
        +events
        +keyboard()
        +main()
    }
    class KeyBoard{
        +snake
        +screen_size
        +events
        +keyboard()
    }
    class KeyboardEvents{
        +get()
    }
```

## Toiminnallisuus
Kuvataan ohjelman toiminnallisuutta sekvenssikaavioilla.
### Keyboard ja turn funktioiden toiminta:

```mermaid
sequenceDiagram
    actor Player
    participant KeyBoard().keyboard()
    participant Snake().turn_up()
    participant Snake().__init__()
    Player ->> KeyBoard().keyboard(): press "up" on keyboard
    KeyBoard().keyboard() ->> Snake().turn_up(): turn_up()
    Snake().turn_up() ->> Snake().__init__(): direction = up
```

### Funktion move toiminta:

```mermaid
sequenceDiagram
    participant GameLoop().main()
    participant Snake().move()
    participant Snake().__init__()
    GameLoop().main() ->> Snake().move(): move()
    Snake().move() ->> Snake().__init__(): location = new
```

## Ohjelman rakenteen puutteita
Attribuuttien m????r?? on liian suuri luokassa Snake. Muutama attribuutti on m????ritelty konstruktorin ulkopuolella, mutta ne ovat attribuutteja, joita k??ytet????n vain omissa funktioissaan.
