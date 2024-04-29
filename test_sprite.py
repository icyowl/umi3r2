import pygame

def test_rect():
    image = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.circle(image, (255,0,0), (20, 20), 20)
    rect = image.get_rect()
    assert rect.top == 0
    assert rect.bottom == 40