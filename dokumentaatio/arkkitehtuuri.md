# Arkkitehtuuri
## Ohjelman rakenne
Ohjelmassa on 6 eri luokkaa: Snake, Food, Score, Death, Fonts ja GameLoop.
### Luokkakaavio

```mermaid
classDiagram
    Snake -- GameLoop
    Food -- GameLoop
    Score -- GameLoop
    Death -- GameLoop
    Fonts -- Death
    Snake -- Score
    Food -- Score
    class Snake{
        +int length
        +tuple color
        +tuple screen_size
        +list location
        +dict directions
        +tuple direction
        +int counter
        +int step
        +int duration
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
```

## Toiminnallisuus
Kuvataan ohjelman toiminnallisuutta sekvenssikaavioilla.
### Keyboard ja turn funktioiden toiminta:

```mermaid
sequenceDiagram
    actor Player
    participant GameLoop().keyboard()
    participant Snake().turn_up()
    participant Snake().__init__()
    Player ->> GameLoop().keyboard(): press "up" on keyboard
    GameLoop().keyboard() ->> Snake().turn_up(): turn_up()
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
Attribuuttien määrä on liian suuri luokassa Snake. Muutama attribuutti on määritelty konstruktorin ulkopuolella, mutta ne ovat attribuutteja, joita käytetään vain omissa funktioissaan.
