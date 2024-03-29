# *********************************************************
# Program: main.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL10
# Year: 2023/24 Trimester 1
# Names: FATIMAH NAJIHAH | YANG ALYA MYSARAH | LEE CHIA YING
# IDs: 1221109554 | 1221106489 | 1221108988
# Emails: 1221109554@student.mmu.edu.my | 1221106489@student.mmu.edu.my | 1221108988@student.mmu.edu.my
# Phones: 01160577079 | 0133935166 | 0165378895
# ********************************************************* 

import pygame
from pygame import mixer
from Text import *

pygame.init()

#to used for the game fps
clock = pygame.time.Clock()
fps = 15

# set up the display
screen_size = (720,480) # give screen size
screen = pygame.display.set_mode(screen_size) # opens up a window 
pygame.display.set_caption('MMULife') # window name


# stores the width & height of the screen into a variable
# to be used for centering objects
width = screen.get_width()  
height = screen.get_height() 

#define font color
font_color = (91, 72, 59)
#font color for heart score
score_color = (153, 0, 0)
#define color
blue = (0, 0, 153)
maroon = (141, 35, 21)
darkMaroon = (82, 22, 14)
white = (255,255,255)

#background image
def bg(image):
    load_image = pygame.image.load(image)
    screen.blit(load_image, (0,0))

#popup any image
def popup_image(image_link,x,y):
    image = pygame.image.load(image_link)
    screen.blit(image, (x, y))
    
#button for the choices
def draw_button(x, y, width, height, hover_color=(146, 146, 145), normal_color=(184, 174, 159)):
    set_button = pygame.Rect(x, y, width, height)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if set_button.collidepoint(mouse_x, mouse_y):
        color = hover_color
    else:
        color = normal_color
    pygame.draw.rect(screen, color, set_button)
    
#box (will act as background for text)
def draw_box(x=10, y=330, width=700, height=140, color=(184, 174, 159)):
    set_box = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, set_box)

#draw text
def draw_text(text, size=20, color=font_color, x=370, y=360):
    font = pygame.font.SysFont('corbel',size,bold=True)

    #making new line (in case the sentence is too long)
    if len(text) > 69:
        text_split = text[0:69] + "-"
        set_text = font.render(text_split, True, color)
        rect_text = set_text.get_rect(center=(x,y))
        screen.blit(set_text, rect_text)
        
        new_line = text[69:]
        set_text = font.render(new_line, True, color)
        rect_text = set_text.get_rect(center=(x,y+26))
        screen.blit(set_text, rect_text)
    else:
         set_text = font.render(text, True, color)
         rect_text = set_text.get_rect(center=(x,y))
         screen.blit(set_text, rect_text)


#line 95-101 : followed by a youtube tutorial (https://www.youtube.com/watch?v=pcdB2s2y4Qc)  
def play_bgm(bgm_file):
    mixer.music.load(bgm_file)
    mixer.music.play(-1)

def play_sound(sound_file):
    sound = mixer.Sound(sound_file)
    sound.play()

def navigate(y):
    set_button = pygame.Rect((width - 280) // 2, y, 280, 60)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if set_button.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] == 1:
        play_sound('buttonSound.mp3')
        return True
    else:
        return False

#screens

#scene: introduction       
def screen1():
    bg('opening.png')
    play_bgm('bgm.mp3')
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[0])
    pygame.display.flip()
def screen2():
    bg('opening.png')
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[1])
    pygame.display.flip()
def screen3():
    bg('opening.png')
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[2])
    pygame.display.flip()
def screen4():
    bg('opening.png')
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[3])
    pygame.display.flip()
def screen5():
    bg('opening.png')
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[4])
    pygame.display.flip()
def screen6():
    bg('opening.png')
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[5])
    draw_button((width - 150) // 2, 390, 150, 50, darkMaroon, maroon)
    draw_text(choice_list[0], 25, (255,255,255), 360, 418)
    pygame.display.flip()

#scene:bedroom
def screen7():
    bg('bedroom.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[6])
    pygame.display.flip()
def screen8():
    bg('bedroom.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[7])
    pygame.display.flip()
def screen9():
    bg('bedroom.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    draw_button((width - 280) // 2, 100, 280, 60)
    draw_text(choice_list[1], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60)
    draw_text(choice_list[2], 20, font_color, 365, 220)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[7])
    pygame.display.flip()
def screen10():
    bg('bedroom.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[8])
    pygame.display.flip()
def screen11():
    bg('bedroom.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[9])
    pygame.display.flip()
def screen12():
    bg('bedroom.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[10])
    pygame.display.flip()
def screen13():
    bg('bedroom.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[11], 20, (255,0,0), 370, 360)
    pygame.display.flip()

#scene:morning
def screen14():
    bg('morning.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[12])
    pygame.display.flip()
def screen15():
    bg('morning.jpg')
    draw_button((width - 280) // 2, 100, 280, 60)
    draw_text(choice_list[3], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60)
    draw_text(choice_list[4], 20, font_color, 365, 220)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[12])
    pygame.display.flip()
def screen16():
    bg('morning.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[13])
    pygame.display.flip()

#scene:walking
def screen17():
    bg('walking.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[14])
    pygame.display.flip()
def screen18():
    bg('walking.jpg')
    draw_button((width - 280) // 2, 100, 280, 60)
    draw_text(choice_list[5], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60)
    draw_text(choice_list[6], 20, font_color, 365, 220)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[14])
    pygame.display.flip()
def screen19():
    bg('walking.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[15])
    pygame.display.flip()
def screen20():
    bg('walking.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[16])
    pygame.display.flip()
def screen21():
    bg('walking.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[17])
    pygame.display.flip()

#scene:entering class
def screen22():
    bg('class.png')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[18])
    pygame.display.flip()
def screen23():
    bg('class.png')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[19])
    pygame.display.flip()
def screen24():
    bg('class.png')
    popup_image('silhouette.png', 230, 100)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[20])
    pygame.display.flip()
def screen25():
    bg('class.png')
    popup_image('silhouette.png', 230, 100)
    draw_button((width - 280) // 2, 100, 280, 60)
    draw_text(choice_list[7], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60)
    draw_text(choice_list[8], 20, font_color, 365, 220)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[20])
    pygame.display.flip()
def screen26():
    bg('class.png')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[21])
    pygame.display.flip()
def screen27():
    bg('class.png')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[22])
    pygame.display.flip()
#scene:in class
def screen28():
    bg('class.png')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[23])
    pygame.display.flip()
def screen29():
    bg('class.png')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[24])
    pygame.display.flip()
def screen30():
    bg('class.png')
    draw_button((width - 280) // 2, 70, 280, 60)
    draw_text(choice_list[9], 20, font_color, 365, 100)
    draw_button((width - 280) // 2, 140, 280, 60)
    draw_text(choice_list[10], 20, font_color, 365, 170)
    draw_button((width - 280) // 2, 210, 280, 60)
    draw_text(choice_list[11], 20, font_color, 365, 240)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[24])
    pygame.display.flip()
def screen31():
    bg('class.png')
    popup_image('mrbean.jpg', 270, 100)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[25])
    pygame.display.flip()
def screen32():
    bg('class.png')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[26])
    pygame.display.flip()
def screen33():
    bg('class.png')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[27])
    pygame.display.flip()
def screen34():
    bg('class.png')
    popup_image('silhouette.png', 230, 100)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[28])
    pygame.display.flip()
def screen35():
    bg('class.png')
    popup_image('silhouette.png', 230, 100)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[29])
    pygame.display.flip()
def screen36():
    bg('class.png')
    popup_image('meme.jpg', 270, 100)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[30])
    pygame.display.flip()
#scene:class ending
def screen37():
    bg('class.png')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[31])
    pygame.display.flip()
def screen38():
    bg('class.png')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[32])
    pygame.display.flip()
def screen39():
    bg('class.png')
    popup_image('silhouette.png', 230, 100)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[33])
    pygame.display.flip()
def screen40():
    bg('class.png')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[34])
    pygame.display.flip()
def screen41():
    bg('class.png')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[35])
    pygame.display.flip()
def screen42():
    bg('class.png')
    draw_button((width - 280) // 2, 70, 280, 60, (153, 204, 255))
    draw_text(quiz_options_list[0], 20, blue, 365, 100)
    draw_button((width - 280) // 2, 140, 280, 60, (153, 204, 255))
    draw_text(quiz_options_list[1], 20, blue, 365, 170)
    draw_button((width - 280) // 2, 210, 280, 60, (153, 204, 255))
    draw_text(quiz_options_list[2], 20, blue, 365, 240)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[36], 20, font_color, 370, 360)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) 
    heart_img = popup_image('heart.png', 585, 3)
    pygame.display.flip()

#scene:walking back
def screen43():
    bg('walking.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[37])
    pygame.display.flip()
def screen44():
    bg('stall.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[38])
    pygame.display.flip()
def screen45():
    bg('stall.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[39])
    pygame.display.flip()
def screen46():
    bg('stall.jpg')
    draw_button((width - 280) // 2, 100, 280, 60)
    draw_text(choice_list[12], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60)
    draw_text(choice_list[13], 20, font_color, 365, 220)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[40])
    pygame.display.flip()
def screen47():
    bg('stall.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[41])
    pygame.display.flip()
def screen48():
    bg('stall.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[42])
    pygame.display.flip()
def screen49():
    bg('stall.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[43])
    pygame.display.flip()
def screen50():
    bg('walking.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[44])
    pygame.display.flip()
def screen51():
    bg('walking.jpg')
    draw_button((width - 280) // 2, 100, 280, 60)
    draw_text(choice_list[14], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60)
    draw_text(choice_list[15], 20, font_color, 365, 220)
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[44])
    pygame.display.flip()
def screen52():
    bg('walking.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[45])
    pygame.display.flip()
def screen53():
    bg('walking.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[46])
    pygame.display.flip()
def screen54():
    bg('walking.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[47])
    pygame.display.flip()
def screen55():
    bg('walking.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[48])
    pygame.display.flip()
def screen56():
    bg('walking.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[49])
    pygame.display.flip()
def screen57():
    bg('walking.jpg')
    heart_bg = draw_box((width-150),0,150,37,white)
    heart_text = draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20)
    heart_img = popup_image('heart.png', 585, 3)
    dialogue_box = draw_box()
    dialogue = draw_text(dialogue_list[50])
    pygame.display.flip()
def screen58():
    bg('opening.png')
    draw_text(dialogue_list[51], 25, maroon, 370, 310)
    draw_text(dialogue_list[52], 25, maroon, 370, 340)
    draw_button((width - 140) // 2, 380, 140, 50, (169, 202, 221),(143, 161, 171))
    draw_text(game_over_list[3], 20, white, 360, 408)
    pygame.display.flip()

def screen0():
    bg('gameOver.png')
    draw_text(game_over_list[0], 30, white, 370, 270)
    draw_text(game_over_list[1], 18, white, 370, 310)
    draw_text(game_over_list[2], 18, white, 370, 330)
    draw_button((width - 120) // 2, 380, 120, 50)
    draw_text(game_over_list[3], 20, white, 360, 408)
    popup_image('heart.png', 230, 250)
    pygame.display.flip()



#putting all the screens into a list
screens = [screen0, screen1,screen2, screen3, screen4, screen5, screen6, screen7, screen8, screen9, screen10, screen11, screen12, screen13, screen14, screen15, screen16, screen17,
           screen18, screen19, screen20, screen21, screen22, screen23, screen24, screen25, screen26, screen27, screen28, screen29, screen30, screen31, screen32, screen33, 
           screen34, screen35, screen36, screen37, screen38, screen39,  screen41, screen42, screen43, screen44, screen45, screen46, screen47, screen48, screen49, screen50,
           screen51, screen52, screen53, screen54, screen55, screen56, screen57, screen58]
    
#initialize the score, the score starts with 3 hearts
heart_score = 3

#initialize the screen number
current_screen = 1

#setting as False to repeat the loop when the user clicks on the incorrect button
loop_chosen = False


# Main loop
while True:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        #navigation
        else:
                if current_screen == 6: #screen with choices
                    if navigate(380):
                        current_screen = 7 #next screen that we want to navigate to
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'start_button:{current_screen}')
                    else:
                        current_screen = current_screen #the screen wont change if the button isnt pressed
                elif current_screen == 0:
                    heart_score = 3
                    if navigate(380):
                        current_screen = 1
                    with open ('Savedata.txt', 'a') as file:
                            file.write(f'play_again_button:{current_screen}\n')
                elif heart_score <= 0:
                    play_sound('badEnd.mp3')
                    current_screen = 0
                    heart_score = 3
                elif current_screen == 9:
                    if navigate(100):
                        current_screen = 10
                        heart_score += 1
                        with open ('Savedata.txt', 'a') as file:
                            file.write(' \n')
                            file.write(f'sleep_first_button:{current_screen}\n')
                    elif navigate(190):
                        play_sound('genshin.mp3')
                        current_screen = 11
                        heart_score -= 1
                        with open ('Savedata.txt', 'a') as file:
                            file.write(' \n')
                            file.write(f'play_game_button:{current_screen}\n')
                    else:
                        current_screen = current_screen
                elif current_screen == 10:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen = 14
                elif current_screen == 15:
                    if navigate(100):
                        current_screen = 16
                        heart_score -= 1 
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'skip_button:{current_screen}\n')
                    elif navigate(190):
                        current_screen = 17
                        heart_score += 1
                        play_sound('meow.mp3')
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'take_a_bath_button:{current_screen}\n')
                    else:
                        current_screen = current_screen
                elif current_screen == 18:
                    if navigate(100):
                        current_screen = 19
                        heart_score -= 1
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'play_with_the_cat_button:{current_screen}\n')
                    elif navigate(190):
                        current_screen = 21
                        heart_score += 1
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'ignore_the_cat_button:{current_screen}\n')
                    else:
                        current_screen = current_screen
                elif current_screen == 20:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen = 22
                elif current_screen == 18:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen = 22
                elif current_screen == 25:
                    if navigate(100):
                        current_screen = 26
                        heart_score += 1
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'accept_mr_winwin_suggestion_button:{current_screen}\n')
                    elif navigate(190):
                        current_screen = 27
                        heart_score -= 1
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'continue_searching_for_a_seat_button:{current_screen}\n')
                    else:
                        current_screen = current_screen
                elif current_screen == 26:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen = 28
                elif current_screen == 30:
                    if navigate(70):
                        current_screen = 31
                        heart_score += 1
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'use_matches_button:{current_screen}\n')
                    elif navigate(140):
                        current_screen = 32
                        heart_score -= 1
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'pinch_yourself_button:{current_screen}\n')
                    elif navigate(210):
                        current_screen = 33
                        heart_score -= 2
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'make_an_escape_button:{current_screen}\n')
                    else:
                        current_screen = current_screen 
                elif current_screen == 31:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen = 37
                elif current_screen == 32:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen = 37 
                elif current_screen == 45:
                    if navigate(100):
                        current_screen = 46
                        heart_score -= 2
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'buy_at_pop_up_stall_button:{current_screen}\n')
                    elif navigate(190):
                        current_screen = 48
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'save_money_button:{current_screen}\n')
                    else:
                        current_screen = current_screen 
                elif current_screen == 47:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen = 49 
                elif current_screen == 48:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen = 50 
                elif current_screen == 50:
                    if navigate(100):
                        current_screen = 56
                        heart_score -= 1
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'go_back_to_hostel_button:{current_screen}\n')
                    elif navigate(190):
                        current_screen = 51
                        heart_score += 1
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'walk_around_campus_for_a_while_button:{current_screen}\n')
                    else:
                        current_screen = current_screen 
                elif current_screen == 54:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen = 57 
                elif current_screen == 58:
                    if navigate(380):
                        current_screen = 1
                        heart_score = 3
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'play_again_button:{current_screen}\n')
                else:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen += 1
            

                
    if current_screen == 42:    
        correct_ans_chosen = False  #setting as False to repeat the loop when the user clicks on the incorrect button
        
        while not correct_ans_chosen: #while True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if navigate(140):
                        current_screen += 1
                        correct_ans_chosen = True  # Exit the loop when the correct button is chosen
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'x_button:{current_screen}\n')
                    elif navigate(70) or navigate(210):
                        heart_score -= 1
                        correct_ans_chosen = False
                        screen42()
                        with open ('Savedata.txt', 'a') as file:
                            file.write(f'E/t_button:{current_screen}\n')
                    else:
                        correct_ans_chosen = False
                        screen42()
   
    if 0 <= current_screen < len(screens):
        screens[current_screen]()

