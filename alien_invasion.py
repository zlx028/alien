import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load(r"music/bg_music.mp3")
    pygame.mixer.music.play(-1)

    # 游戏初始化
    pygame.init()
    # 创建一个窗口对象
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 存储子弹的编组
    bullets = Group()

    # 存储外星人的编组，创建一组外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 存储游戏统计的信息
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 游戏主循环
    while True:
        # 事件驱动，循环检查所有事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        
        # 刷新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()


