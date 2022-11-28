 def keyboard(self):
      for tapahtuma in pygame.event.get():
           if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_UP:
                    self.turn(up)
                if tapahtuma.key == pygame.K_DOWN:
                    self.turn(down)
                if tapahtuma.key == pygame.K_LEFT:
                    self.turn(left)
                if tapahtuma.key == pygame.K_RIGHT:
                    self.turn(right)
            if tapahtuma.type == pygame.QUIT:
                exit()
