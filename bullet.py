import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # 飞船发射子弹的类
    def __init__(self, ai_settings, screen, ship):
        # 飞船位置创建一个子弹对象
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)  # 创造子弹矩形
        self.rect.centerx = ship.rect.centerx  # 子弹的横向位置在飞船中心
        self.rect.top = ship.rect.top  # 子弹的顶端与飞船顶端对齐
        
        # 小数表示子弹位置， 子弹的纵坐标
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # 向上移动子弹
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        # 屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)