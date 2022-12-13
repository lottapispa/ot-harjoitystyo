# Arkkitehtuuri
## Ohjelma
Ohjelmassa on 3 eri luokkaa: Snake, Food ja GameLoop.
## Luokkakaavio
<img width="642" alt="Screenshot 2022-12-13 at 19 31 10" src="https://user-images.githubusercontent.com/101987621/207403505-d0b36808-b6a0-4fba-a187-328311651c6b.png">

## Toiminnallisuus
Kuvataan ohjelman toiminnallisuutta sekvenssikaaviolla
### Keyboard ja turn funktioiden toiminta:

```mermaid
sequenceDiagram
    actor Player
    participant Snake().keyboard()
    participant Snake().turn_up()
    participant Snake().__init__()
    Player ->> Snake().keyboard(): press up on keyboard
    Snake().keyboard() ->> Snake().turn_up(): self.turn_up()
    Snake().turn_up() ->> Snake().__init__(): direction = up
```

### Funktion move toiminta:

```mermaid
sequenceDiagram
    participant Main
    participant Snake
```
