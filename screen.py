import pygame
import math

class GraphScreen:

    def __init__(self, height, width, color):

        self.screen = pygame.display.set_mode((width, height))
        self.background_color = color
        self.viewpoint = [0, 0]
        self.clock = pygame.time.Clock()
        self.scale = 100
        self.height = height
        self.width = width
        self.cons_a = 0
        self.cons_b = 0
        self.cons_c = 0
        self.cons_d = 0
        self.CURSOR = pygame.image.load('cursor.png').convert_alpha()
        pygame.mouse.set_visible(False)
        pygame.font.init()
        pygame.display.set_caption("Graph window")
        self.font = pygame.font.SysFont('Comic Sans MS', 15)

    def draw_pixel(x, y, color):
        pygame.draw.circle(screen, color, (x, y), 1)  


    def f(self, x, function, const):
        new_func = ''
        for char in function:
            if char == 'A':
                newchar = const[0]
            elif char == 'B':
                newchar = const[1]
            elif char == 'C':
                newchar = const[2]
            elif char == 'D':
                newchar = const[3]
            else:
                newchar = char
            new_func += newchar
        try:
            result = eval(new_func)
            return result
        except:
            raise ValueError
    

    def draw_segment(self, x, function, const, color):
        x1 = (x-1 + self.width/2)
        x2 = (x + self.width/2)
        try:
            y1 = (self.height/2 - self.f((x-1)/self.scale, function, const)*self.scale)
            y2 = (self.height/2 - self.f((x/self.scale), function, const)*self.scale)
            pygame.draw.line(self.screen, color, (x1, y1), (x2, y2),3)
        except (ValueError, ZeroDivisionError, TypeError):
            pass


    def draw_graph(self, function, const, color):
        a = int(0 - (self.width/2))
        z = int(self.width/2)
        for x in range(a, z):
            self.draw_segment(x, function, const, color) 


    def draw_axes(self, color):

        pygame.draw.line(self.screen, color, (0, self.height/2-self.viewpoint[1]), (self.width, self.height/2-self.viewpoint[1]),3)   #x-axis
        pygame.draw.line(self.screen, color, (self.width/2-self.viewpoint[0], 0), (self.width/2-self.viewpoint[0], self.height),3)    #y-axis
        i = int(self.width/2)
        r = i - self.scale
        t = i + self.scale
        for u in range(i):                                                                              #vertical secondary axises
            pygame.draw.line(self.screen, (200, 200, 200), (r-self.viewpoint[0], 0), (r-self.viewpoint[0], self.height),1)
            pygame.draw.line(self.screen, (200, 200, 200), (t-self.viewpoint[0], 0), (t-self.viewpoint[0], self.height),1)
            r = r - self.scale
            t = t + self.scale
        p = int(self.height/2)
        j = p - self.scale
        k = p + self.scale
        for u in range(i):                                                                              #horizontal secondary axises
            pygame.draw.line(self.screen, (200, 200, 200), (0, j-self.viewpoint[1]), (self.width, j-self.viewpoint[1]),1)
            pygame.draw.line(self.screen, (200, 200, 200), (0, k-self.viewpoint[1]), (self.width, k-self.viewpoint[1]),1)
            j = j - self.scale
            k = k + self.scale


    def draw_coodinates(self):

        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        real_x = round((x - self.width/2)/self.scale + 8/self.scale, 2)
        real_y = round(-(y - self.height/2)/self.scale - 8/self.scale, 2)
        coord_string = "(" + str(real_x) + ", " + str(real_y) + ")"

        textsurface = self.font.render(coord_string, False, (50, 50, 255))
        self.screen.blit(textsurface,(x + 16, y + 16))


    def draw_tangent_line(self, x1, x2, y1, y2):
    
        slope = (y2-y1)/(x2-y1)
        pygame.draw.line(self.screen, (10, 10, 10), (x1, y1), (x1+100, (x1+100)*slope))    


    def refresh(self, function_data, scale):

        function_string = function_data[0]
        const = (function_data[1],
                function_data[2],
                function_data[3],
                function_data[4])
        self.scale = scale
        self.screen.fill(self.background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        self.draw_axes((0, 0, 0))
        if function_string[0] != '':
            self.draw_graph(function_string[0], const, (255, 0, 0))
        if function_string[1] != '':
            self.draw_graph(function_string[1], const, (0, 0, 255))    

        self.screen.blit(self.CURSOR, (pygame.mouse.get_pos()))
        self.draw_coodinates()
        pygame.display.flip()
        
        self.clock.tick(60)
        return True
        
