# Sekvenssikaavio

```mermaid
sequenceDiagram
  Main ->> Machine: Machine(tank, engine)
  Main ->> Machine: tank.fill(40)
  Machine ->> Drive: 
