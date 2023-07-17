#color setter file
class Color:
    dark_grey = (26, 31, 40)
    blue = (13, 64, 216)
    cyan = (21, 204, 209)
    purple = (166, 0, 247)
    yellow = (237, 234, 4)
    orange = (226, 116, 17)
    red = (232, 18, 18)
    green = (47, 230, 13)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod #call methods directly
    def get_cell_colors(cls):
         return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, 
                 cls.purple, cls.cyan, cls.blue]
    