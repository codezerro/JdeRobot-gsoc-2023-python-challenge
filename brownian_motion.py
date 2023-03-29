import pygame,sys

x_speed, y_speed = 3,0


# circle
class Circle_Mov:
    
    def __init__(self,screen,color,x,y,screen_width,screen_height,circle_radius) -> None:
        self.x = x
        self.y = y
        self.screen_width = screen_width - 25
        self.screen_height = screen_height - 25
        self.circle_radius = circle_radius

        pygame.draw.circle(screen,color,(x,y),circle_radius,0)
    
    def circle_pos(self):
        self.x -= x_speed
        self.y += y_speed
        
        return [self.x,self.y]
    
    def circle_boundary(self):
        global x_speed, y_speed
        
        # width
        if self.x >= self.screen_width - self.circle_radius or self.x <= 0 + (self.circle_radius + 25):
            
            if y_speed == 0: 
                y_speed = 4
            
            x_speed *= -1
        
        # height
        if self.y >= self.screen_height - self.circle_radius or self.y <= 0 + (self.circle_radius + 25):
            y_speed *= -1

class BrownianMotion:
    
    # init pygame
    pygame.init()
    
    def __init__(self) -> None:
        self.Circle_Mov = Circle_Mov
        self.clock = pygame.time.Clock()
        self.screen_width = 800
        self.screen_height = 800
        self.screen = pygame.display.set_mode([self.screen_width,self.screen_height])
        
        self.pos_x = self.screen_width // 2 
        self.pos_y = self.screen_height // 2
        self.circle_radius = 20
        self.color = (255,0,0)

    def run_bm(self):
        while True:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # window title
            pygame.display.set_caption('Brownian Motion Simulation')
            # screen fill 
            self.screen.fill((13,62,74))
            
            # draw rectangle boundary
            pygame.draw.rect(self.screen, (0,255,200), pygame.Rect(15, 15, 770, 770),  10)

            # circle func
            c1 = self.Circle_Mov(self.screen,self.color,self.pos_x,self.pos_y,self.screen_width,self.screen_height,self.circle_radius)
            self.pos_x,self.pos_y = c1.circle_pos()
            c1.circle_boundary()
            
            # screen update
            pygame.display.flip()
            self.clock.tick(60)
        
        
        

