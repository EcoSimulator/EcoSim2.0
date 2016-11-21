import pygame
from pygame.locals import *
from Species import creature

def display_info(screen, species):
    # get the species
    # Should improve this later. Maybe fix it up in creature.py.
    if(species == "wolf"):
        animal = creature.Wolf()
    elif(species == "deer"):
        animal = creature.Deer()
    elif(species == "bees"):
        animal = creature.Bee()
    elif(species == "plant"):
        animal = creature.Plant()
    else:
        animal = creature.NoName()

    # set various fonts
    pygame.font.init()
    margin = 154
    x = margin + 30
    y = 260
    white = (255, 255, 255, 100)
    nameFont = pygame.font.SysFont("arial", 60, bold=True)
    sciFont = pygame.font.SysFont("times", 24, italic=True)
    normalFont = pygame.font.SysFont("arial", 24)

    # draw a background rectangle
    background_rect = Rect((margin, 0), (screen.get_size()[0] - margin, screen.get_size()[1]))
    pygame.draw.rect(screen, (20, 20, 20, 100), background_rect)

    # write text
    nameText = nameFont.render(animal.getName(), 1, white)
    screen.blit(nameText, (x, y))
    y += 72
    sciText = sciFont.render(animal.getSciName(), 1, white)
    screen.blit(sciText, (x, y))
    y += 28
    conText = normalFont.render("Conservation Status: "+animal.getConStatus(), 1, white)
    screen.blit(conText, (x, y))
    y += 60

    # use text wrap for description
    wrap_rect = Rect((x, y), (screen.get_size()[0] - x - 30, screen.get_size()[1] - y - 30))
    drawText(screen, animal.getDesc(), white, wrap_rect, normalFont)

    pygame.display.flip()


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