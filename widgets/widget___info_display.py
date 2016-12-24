import pygame
import os
from creatures import *
from pygame.locals import *
from properties import *

from widgets import creatures


class InfoDisplay:
    def __init__(self, species):
        # get the species
        self.species = species
        if self.species == "wolf":
            self.animal = Wolf()
        elif self.species == "deer":
            self.animal = Deer()
        elif self.species == "bees":
            self.animal = Bee()
        elif self.species == "plant":
            self.animal = Plant()
        elif self.species == "fish":
            self.animal = Fish()
        elif self.species == "bear":
            self.animal = Bear()
        else:
            self.animal = NoName()

        # set various fonts
        pygame.font.init()
        margin = 154
        x = margin + 30
        y = 300
        white = (255, 255, 255, 100)
        name_font = pygame.font.SysFont("arial", 60, bold=True)
        sci_font = pygame.font.SysFont("times", 24, italic=True)
        normal_font = pygame.font.SysFont("arial", 24)

        # draw a background rectangle
        bg = (20, 20, 20, 100)
        background_rect = Rect((margin, 0), (screen.get_size()[0] - margin, screen.get_size()[1]))
        pygame.draw.rect(screen, bg, background_rect)

        # display image
        img = pygame.image.load(os.path.join(infoscreen_dir, self.animal.get_image()))
        img_rect = Rect((margin, 0), (200, 200))
        screen_rect = Rect((margin, 0), (screen.get_size()[0] - margin, screen.get_size()[1]))
        screen_img = aspect_scale(img, (screen.get_size()[0] - margin, screen.get_size()[1]))
        screen.blit(screen_img, screen_rect)

        # create gradient
        gradient = pygame.image.load(os.path.join(infoscreen_dir, "testgradient" + png_ext))
        gradient_rect = Rect((margin, 0), (screen.get_size()[0] - margin, screen.get_size()[1]))
        screen.blit(gradient, gradient_rect)

        # write text
        name_text = name_font.render(self.animal.get_name(), 1, white)
        screen.blit(name_text, (x, y))
        y += 72
        sci_text = sci_font.render(self.animal.get_sci_name(), 1, white)
        screen.blit(sci_text, (x, y))
        y += 28
        con_text = normal_font.render("Conservation Status: "+ self.animal.get_con_status(), 1, white)
        screen.blit(con_text, (x, y))
        y += 60

        # use text wrap for description
        wrap_rect = Rect((x, y), (screen.get_size()[0] - x - 30, screen.get_size()[1] - y - 30))
        drawText(screen, self.animal.get_desc(), white, wrap_rect, normal_font)

        pygame.display.update()


# taken from http://www.pygame.org/wiki/TextWrap
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text


# taken from http://www.pygame.org/pcr/transform_scale/
def aspect_scale(img, (bx, by)):
    """ Scales 'img' to fit into box bx/by.
     This method will retain the original image's aspect ratio """
    ix, iy = img.get_size()
    if ix > iy:
        # fit to width
        scale_factor = bx / float(ix)
        sy = scale_factor * iy
        if sy > by:
            scale_factor = by / float(iy)
            sx = scale_factor * ix
            sy = by
        else:
            sx = bx
    else:
        # fit to height
        scale_factor = by / float(iy)
        sx = scale_factor * ix
        if sx > bx:
            scale_factor = bx / float(ix)
            sx = bx
            sy = scale_factor * iy
        else:
            sy = by

    return pygame.transform.scale(img, (int(sx), int(sy)))