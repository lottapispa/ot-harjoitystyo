# Monopoly luokkakaavio
```mermaid
 classDiagram
 	Monopoly <|-- Player
	Monopoly <|-- Square
	class Dice{
	    +rollDice
	}
	class Player{
	    +Player()
	    +string pawnLocation
	}
	class Monopoly{
	    +int getPlayers(amount)
	    +int getSquares(40)
	}
	class Square{
	    +Square()
	    squareType: aloitusruutu
	    squareType: vankila
	    squareType: sattuma
	    squareType: yhteismaa
	    squareType: asema
	    squareType: laitos
	    squareType: katu
	}
	class Cards{
	    +Card()
	}

