# Monopoly luokkakaavio
```mermaid
 classDiagram
 	Monopoly <|-- Player
	Monopoly <|-- GameBoard
	Monopoly <|-- Square
	class Dice{
	    +rollDice
	}
	class Player{
	    +Player()
	    +string pawnLocation
	}
	class GameBoard{
	    +int getPlayers(amount)
	    +int getSquares(40)
	}
	class Square{
	    +Square()
	    squareType:
	    {aloitusruutu, vankila, sattuma, yhteismaa, asema, laitois, katu}
	}
	class Cards{
	    +Card()
	}

