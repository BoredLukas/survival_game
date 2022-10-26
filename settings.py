class Settings:
    """
    class containing all settings
    remember: use CAPITAL letters for CONSTANTS (variables that don't change)
    """
    def __init__(self,win_height=680,win_width=1080,bg_color=(255,255,255),fps=30,speed=12,player_size=(90,70), tree_size=(300,300), stone_size=(200,200)):
        self.NAME = "Survival"

        # WINDOWS SIZE
        self.WIN_HEIGHT = win_height
        self.WIN_WIDTH = win_width
        
        # COLOR SETTINGS
        self.BG_COLOR = bg_color
    
        # FRAMERATE
        self.FPS = fps # frames per second
        self.TIME_DELAY = int(1000 / self.FPS) # calculate delay time between two frames

        # GAME CONSTANTS
        self.SPEED = speed
        self.PLAYER_SIZE = player_size
        self.TREE_SIZE = tree_size
        self.STONE_SIZE = stone_size