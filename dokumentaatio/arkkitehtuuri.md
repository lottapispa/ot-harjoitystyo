# Arkkitehtuuri
## Ohjelma
Ohjelmassa on 3 eri luokkaa: Snake, Food ja GameLoop.
## Luokkakaavio
<img width="642" alt="Screenshot 2022-12-13 at 19 31 10" src="https://user-images.githubusercontent.com/101987621/207403505-d0b36808-b6a0-4fba-a187-328311651c6b.png">

```mermaid
classDiagram
    class Snake{
        +int length
        +tuple color
        +int screen_width
        +int screen_height
        +list location
        +tuple up
        +tuple down
        +tuple left
        +tuple right
        +tuple direction
        +int points
        +int highscore
        +int step
        +int duration
        +bool die_called
        +bool reset_called
        +bool dead
        +head_location()
        +head_rect()
        +draw_snake()
        +turn_up()
        +turn_down()
        +turn_left()
        +turn_right()
        +move()
        +reset()
    }
    class Food{
        +int size
        +tuple color
        +tuple location
        +random_location()
        +draw_food()
        +eating()
    }
    class GameLoop{
        +int screen_width
        +int screen_height
        +tuple font
        +tuple bigfont
        +keyboard()
        +die()
        +gameover_loop()
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
    participant Main
    participant Snake().move()
    participant Snake().__init__()
    Main ->> Snake().move(): move()
    Snake().move() ->> Snake().__init__(): location = new
```
