# Arkkitehtuuri
## Ohjelma
Ohjelmassa on 3 eri luokkaa: Snake, Food ja GameLoop.
## Luokkakaavio

```mermaid
classDiagram
    Snake -- GameLoop
    Food -- GameLoop
    Score -- GameLoop
    Death -- GameLoop
    class Snake{
        +int length
        +tuple color
        +tuple screen_proportions
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
        +tuple screen_proportions
        +tuple font
        +tuple bigfont
        +dict directions
        +bool die_called
        +bool call_main
        +die()
        +gameover_loop()
        +reset()
    }
    class GameLoop{
        +snake
        +food
        +score
        +death
        +tuple screen_proportions
        +caption
        +screen
        +events
        +keyboard()
        +main()
    }
```

## Toiminnallisuus
Kuvataan ohjelman toiminnallisuutta sekvenssikaavioilla
### Keyboard ja turn funktioiden toiminta:

```mermaid
sequenceDiagram
    actor Player
    participant Snake().keyboard()
    participant Snake().turn_up()
    participant Snake().__init__()
    Player ->> Snake().keyboard(): press "up" on keyboard
    Snake().keyboard() ->> Snake().turn_up(): turn_up()
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
