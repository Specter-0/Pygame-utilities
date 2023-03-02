import math
import pygame as pg
def init(): #kalles for å lage farger
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

class utility: # main klasse
    #""" notatene er for autodocs
    """
    Main class of the library
    it offers a variety of pygame shortcuts to ease the pain

    :param: none
    :type: none
    """
    def __init__(self):#her skjer det ingenting
        pass

    class sprite: #du kan inherite for å få metoder fra denne når du bruker pygame.sprite.Sprite
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

    class Gravity(): #kalles for å lage objekter med gravitajon, tror den bare fungerer med planeter
        def set_values(scale = 200, timestep = 3600*24, au = 149.6e6 * 1000, g = 6.67428e-11): # set universale verier til gravitjons objekter må kalles først
            global AU, G, SCALE, TIMESTEP
            AU = au # astronomical units --149.6e6 * 1000
            SCALE = scale / AU # 1AU = 100px --200
            TIMESTEP = timestep # 1 day --3600*24
            G = g # gravitational constant 6.67428e-11

        def set_timestep(timestep = 3600*24): # samme som set_values men bare for timestep
            global TIMESTEP
            TIMESTEP = timestep

        """ funker ikke
        def get_instances():
            try:
                return all_instances
            except NameError:
                print("does not work")
        """

        def __init__(self, x, y, y_vel, radius, mass, color=(255,255,255)): #lager et gavitajons objekt
            self.tracking = False
            self.x = x * AU
            self.y = y 
            self.radius = radius
            self.mass = mass
            self.color = color
            self.path = []

            #self.sun = False
            #self.distance_to_sun = 0

            self.y_vel = y_vel
            self.x_vel = 0
            all_instances = []
           
        def path_track(self): #set path tracking for et gravitajon objekt
            self.tracking = True
        
        def draw(self, win, width, height): #tegn et gravitajon objekt
            x = self.x * SCALE + width / 2
            y = self.y * SCALE + height / 2
            pg.draw.circle(win, self.color, (x, y), self.radius)

        def draw_path(self, win, width, height): #tegn pathen til et gravitajon objekt
            x = self.x * SCALE + width / 2
            y = self.y * SCALE + height / 2

            if len(self.path) > 2: #gjør at points i path listen er riktig plasert
                updated_path = []
                for point in self.path:
                    x, y = point
                    x = x * SCALE + width / 2
                    y = y * SCALE + height / 2
                    updated_path.append((x, y))

                pg.draw.lines(win, self.color, False, updated_path, 2)

        def path_clear(self): #ganske klart hva denne gjør
            self.path.clear()

        def attraction(self, other): #regner ut gravitajon
            #quick math
            other_x, other_y = other.x, other.y
            distance_x = other_x - self.x
            distance_y = other_y - self.y
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
            
            force = G * self.mass * other.mass / distance**2
            v = math.atan2(distance_y, distance_x)
            force_x = math.cos(v) * force
            force_y = math.sin(v) * force
            return force_x, force_y
            
        
        def update_pos(self, objects): #gir gravitajon objekter sin plassering på skjermen
            total_fx = total_fy = 0

            # more quick math
            for object in objects:
                if self == object:
                    continue
                fx, fy = self.attraction(object)
                total_fx += fx
                total_fy += fy

            self.x_vel += total_fx / self.mass * TIMESTEP
            self.y_vel += total_fy / self.mass * TIMESTEP

            self.x += self.x_vel * TIMESTEP
            self.y += self.y_vel * TIMESTEP

            if self.tracking:
                self.path.append((self.x, self.y))
        
        def lock(self, width, height): #gjør at objekte ikke kan bevege seg fra midten av skjermen
            self.x = width
            self.y = height
        

