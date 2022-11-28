 def keyboard(self):
      for tapahtuma in pygame.event.get():
           if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_UP:
                    self.turn_up()
                if tapahtuma.key == pygame.K_DOWN:
                    self.turn_down()
                if tapahtuma.key == pygame.K_LEFT:
                    self.turn_left()
                if tapahtuma.key == pygame.K_RIGHT:
                    self.turn_right()
            if tapahtuma.type == pygame.QUIT:
                exit()
