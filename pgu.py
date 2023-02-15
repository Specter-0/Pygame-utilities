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
        class movement:
            """
            contains all methods that alter movement
            can be used when creating class or as .movement

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

            def gravity_ir(object1, strength1, object2, strength2):
                """
                empty
                """
        

