import math
import pygame as pg
def init():
    """
    Empty
    """
    global WHITE
    WHITE = (255,255,255)
    global BLACK
    BLACK = (0,0,0)
    global GRAY
    GRAY = (65,65,65)
    global GREEN
    GREEN = (0,255,0)
    global PURPLE
    PURPLE = (150, 5, 245)
    global BLUE
    BLUE = (5, 75, 245)
    global RED
    RED = (255,0,0)
    global ORANGE
    ORANGE = (245, 120, 5)
    global TEAL
    TEAL = (5, 245, 140)
    global LIMEGREEN
    LIMEGREEN = (120, 245, 5)
    global CYAN
    CYAN = (5, 245, 235)
    global DARKBLUE
    DARKBLUE = (5, 10, 245)
    global PINK
    PINK = (245, 5, 193)
    global YELLOW
    YELLOW = (255,255,0)
    global DARKRED
    DARKRED = (110, 0, 0)

class utility:
    """
    Main class of the library
    it offers a variety of pygame shortcuts to ease the pain

    :param: none
    :type: none
    """
    def __init__(self):
        pass

    class sprite:
        """
        used when creating a pygame.sprite.Sprite object in pygame
        offers simplefied methods  

        :param: none
        :type: none
        """
        def move_tp(object, x, y):
            """
            moves an object to a set cordinate in the screen

            :param: pygame object to be moved
            :type: object
            """
            object.rect.center = (x, y)

    def gravity_set_values(au, scale, timestep):
            global AU, G, SCALE, TIMESTEP
            AU = au # astronomical units --149.6e6 * 1000
            SCALE = scale / AU # 1AU = 100px --200
            TIMESTEP = timestep # 1 day --3600*24
            G = 6.67428e-11 # gravitational constant
    def gravity_set_timestep(timestep):
        try: 
            TIMESTEP = timestep
        except:
            pass
    class gravity():       
        def path_track(self):
            self.path = []
            self.tracking = True
        
        def draw(self, win, width, height):
            x = self.x * SCALE + width / 2
            y = self.y * SCALE + height / 2
            pg.draw.circle(win, self.color, (x, y), self.radius)

        def attraction(self, other):
            other_x, other_y = other.x, other.y
            distance_x = other_x - self.x
            distance_y = other_y - self.y
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

            #if other.sun:
                #self.distance_to_sun = distance
            
            force = G * self.mass * other.mass /distance**2
            v = math.atan2(distance_y, distance_x)
            force_x = math.cos(v) * force
            force_y = math.sin(v) * force
            return force_x, force_y
        
        def update_pos(self, objects):
            total_fx = total_fy = 0

            for object in objects:
                if self == object:
                    continue
                total_fx, total_fy = self.attraction(object)

            self.x_vel += total_fx / self.mass * TIMESTEP
            self.y_vel += total_fy / self.mass * TIMESTEP

            self.x += self.x_vel * TIMESTEP
            self.y += self.y_vel * TIMESTEP

            if self.tracking:
                self.path.append((self.x, self.y))

    class gravity_create_object(gravity):
        def __init__(self, x, y, radius, mass, color=(255,255,255)): 
            self.tracking = False
            self.x = x * AU
            self.y = y 
            self.radius = radius
            self.mass = mass
            self.color = color

            #self.sun = False
            #self.distance_to_sun = 0

            self.y_vel = 0
            self.x_vel = 0
        

