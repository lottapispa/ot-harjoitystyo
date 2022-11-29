# Arkkitehtuuri 
## Luokkakaavio
<img width="588" alt="Screenshot 2022-11-29 at 18 03 41" src="https://user-images.githubusercontent.com/101987621/204580497-ceed84d1-29b3-4275-98c0-24bd1bcffefc.png">

```mermaid
classDiagram
      Global variables{
      +int screenWidth
      +int screenHeight
      +tuple up
      +tuple down
      +tuple left
      +tuple right
      +screen
      }
      class Snake{
      +int length
      +tuple color
      +list location
      +tuple direction
      +int points
      +head_location()
      +draw_snake()
      +turn()
      +move()
      +keyboard()
      +die()
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
      Main{
      +main()
      }
