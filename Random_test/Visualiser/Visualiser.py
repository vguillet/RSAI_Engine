
################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs
import pygame as pg

# Own modules
from RSAI_Engine.Settings.SETTINGS import SETTINGS
from Random_test.Visualiser.Visualiser_tools import Visualiser_tools
from Random_test.Visualiser.Background_visu import Background
from Random_test.Visualiser.Button import Button

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2020'

################################################################################################################


class Visualiser:
    def __init__(self, run_name: str, environment: "Environment object", agents_dict, press_start=True):
        # ======================== START VISUALISER ANIMATION ===========================
        if press_start:
            input("\n\n -- Press enter to start visualiser animation -- \n")

        # ======================== INITIALISATION =======================================
        # ----- Initialise packages and tools
        pg.init()
        pg.font.init()
        pg.mixer.init()
        
        visualiser_tools = Visualiser_tools()
        
        # --> Setup visualiser settings
        fps = 30
        margin = 0
        scale_factor = 2

        # --> Setup visualizer window
        screen_size = (environment.shape[1] * scale_factor + margin,
                       environment.shape[0] * scale_factor + margin)

        screen = pg.display.set_mode(screen_size)                               # Window size
        pg.display.set_caption("Visualiser: " + run_name)                       # Window name

        background = Background(environment, [0, 0], screen_size)

        # --> Setup visualizer clock (to keep track of visualiser run speed)
        clock = pg.time.Clock()

        # --> Create sprite groups and lists
        all_sprites_group = pg.sprite.Group()
        POI_sprite_group = pg.sprite.Group()
        agent_sprite_group = pg.sprite.Group()

        # ----- Create POIs
        POIs_visu_dict = visualiser_tools.gen_POI_visu_dict(environment, scale_factor, margin)

        # --> Add sprites to group
        for sprite in POIs_visu_dict.keys():
            all_sprites_group.add(POIs_visu_dict[sprite]["Sprite"])
            POI_sprite_group.add(POIs_visu_dict[sprite]["Sprite"])
                
        # ----- Create agents
        agents_visu_dict = visualiser_tools.gen_agents_visu_dict(agents_dict, margin)

        # --> Add sprites to group
        for sprite in agents_visu_dict.keys():
            all_sprites_group.add(agents_visu_dict[sprite]["Sprite"])
            agent_sprite_group.add(agents_visu_dict[sprite]["Sprite"])

        # ======================== PROCESS ==============================================
        running = True
        step = -1
        while running:
            # --> Add map view button
            Button(screen,
                   10, environment.shape[0] * scale_factor - 10,
                   80, 20,
                   "View toggle",
                   action=background.switch_view(environment))

            # --> Set step
            step += 1
            settings = SETTINGS()
            settings.agent_settings.gen_agent_settings()
            max_step = settings.agent_settings.max_age

            if step > max_step:
                step = max_step

            # ----- Process input (events)
            for event in pg.event.get():
                # --> Close windows/exit pygame if window is closed
                if event.type == pg.QUIT:
                    running = False

            # ----- Update all sprites
            agent_sprite_group.update(step)

            visualiser_tools.update_dynamic_labels(agents_visu_dict, step)

            # ----- Draw/render
            # --> Fill screen with white
            screen.fill((255, 255, 255))

            # --> Add background map
            screen.blit(background.image, background.rect)

            # --> Draw all sprites
            all_sprites_group.draw(screen)

            # --> Add POI label to image
            visualiser_tools.blit_all_labels(POIs_visu_dict, screen)

            # --> Add agents label to image
            visualiser_tools.blit_all_labels(agents_visu_dict, screen)

            # --> Add step label
            step_font = pg.font.SysFont("comicsansms", 25)
            step_label = step_font.render("Step: " + str(step), False, (0, 0, 0))
            screen.blit(step_label, (20, 20))

            # --> Flip display *after* drawing everything
            pg.display.flip()

        pg.quit()

    def Button(self, screen, x, y, w, h, label, action=None):
        self.label = label

        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        self.button_width = w
        self.button_height = h

        self.button_x = x
        self.button_y = y - self.button_height

        # --> If mouse is on button
        if self.button_x + self.button_width > mouse[0] > self.button_x \
                and self.button_y + self.button_height > mouse[1] > self.button_y:
            pg.draw.rect(screen, (255, 255, 200), (self.button_x, self.button_y, self.button_width, self.button_height))

            if click[0] == 1 and action is not None:
                action()

        else:
            pg.draw.rect(screen, (255, 255, 255), (self.button_x, self.button_y, self.button_width, self.button_height))
        pg.display.update()

        smallText = pg.font.Font("freesansbold.ttf", 10)

        text_surface = smallText.render(self.label, True, (0, 0, 0))
        text_rect = text_surface.get_rect()

        text_rect.center = ((self.button_x + (self.button_width / 2)), (self.button_y + (self.button_height / 2)))
        screen.blit(text_surface, text_rect)

        # pg.display.update()
        # time.sleep(0.2)
