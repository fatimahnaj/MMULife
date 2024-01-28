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

#FATIMAH NAJIHAH :
#code the overall GUI (displaying everything for each screen)
#used reference.py as pygame GUI reference
#used https://www.youtube.com/watch?v=GMBqjxcKogA&t=46s logic on how to display each scenes

import pygame
from pygame import mixer
from Text import * 

#initialize pygame so that the code will work
pygame.init()

#to be used for the game fps
clock = pygame.time.Clock()
fps = 15

# set up the display
screen_size = (720,480) # give screen size
screen = pygame.display.set_mode(screen_size) # opens up a window 
pygame.display.set_caption('MMULife') # window name


# stores the width of the screen into a variable
# to be used for centering objects
width = screen.get_width()  

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
        if text[68] or text[69] != " ":
            text_split = text[0:69] + "-"
            set_text = font.render(text_split, True, color)
            rect_text = set_text.get_rect(center=(x,y))
            screen.blit(set_text, rect_text)
            
            new_line = text[69:]
            set_text = font.render(new_line, True, color)
            rect_text = set_text.get_rect(center=(x,y+26))
            screen.blit(set_text, rect_text)

        else:
            text_split = text[0:69]
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


#play_bgm and play_sound function : followed by a youtube tutorial (https://www.youtube.com/watch?v=pcdB2s2y4Qc)  
def play_bgm(bgm_file):
    mixer.music.load(bgm_file)
    mixer.music.play(-1)

def play_sound(sound_file):
    sound = mixer.Sound(sound_file)
    sound.play()

#navigation (move to -- screen when -- choice is made)
def navigate(y):
    set_button = pygame.Rect((width - 280) // 2, y, 280, 60)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if set_button.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] == 1:
        play_sound('buttonSound.mp3')
        return True
    else:
        return False
    
#saving data - YANG ALYA MYSARAH
def savedata(button):
    with open ('Savedata.txt', 'a') as file:
        file.write(f'Player choose "{button}" button in screen{current_screen}\n')

#add ---- line to know that the player has exited the game
def newgame():
    with open ('Savedata.txt', 'a') as file:
        file.write('-------------------------------------------------------\n')


#screens - FATIMAH NAJIHAH
#scene: introduction       
def screen1():
    bg('opening.png')
    play_bgm('bgm.mp3')
    draw_box() #dialogue box
    draw_text(dialogue_list[0]) #dialogue text
    draw_text("click anywhere to continue", 15,white,610,450) #instruction
    pygame.display.flip() #update the display
def screen2():
    bg('opening.png')
    draw_box() #dialogue box
    draw_text(dialogue_list[1]) #dialogue text
    draw_text("click anywhere to continue", 15,white,610,450) #instruction
    pygame.display.flip()
def screen3():
    bg('opening.png')
    draw_box() #dialogue box
    draw_text(dialogue_list[2]) #dialogue text
    draw_text("click anywhere to continue", 15,white,610,450) #instruction
    pygame.display.flip()
def screen4():
    bg('opening.png')
    draw_box() #dialogue box
    draw_text(dialogue_list[3]) #dialogue text
    pygame.display.flip()
def screen5():
    bg('opening.png')
    draw_box() #dialogue box
    draw_text(dialogue_list[4]) #dialogue text
    pygame.display.flip()
def screen6():
    bg('opening.png')
    draw_box() #dialogue box
    draw_text(dialogue_list[5]) #dialogue text
    draw_button((width - 150) // 2, 390, 150, 50, darkMaroon, maroon)
    draw_text(choice_list[0], 25, (255,255,255), 360, 418)
    pygame.display.flip()

#scene:bedroom
def screen7():
    bg('bedroom.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart score text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[6]) #dialogue text
    pygame.display.flip()
def screen8():
    bg('bedroom.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[7]) #dialogue text
    pygame.display.flip()
def screen9():
    bg('bedroom.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_button((width - 280) // 2, 100, 280, 60)
    draw_text(choice_list[1], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60)
    draw_text(choice_list[2], 20, font_color, 365, 220)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[7]) #dialogue text
    pygame.display.flip()
def screen10():
    bg('bedroom.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[8]) #dialogue text
    pygame.display.flip()
def screen11():
    bg('bedroom.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[9]) #dialogue text
    pygame.display.flip()
def screen12():
    bg('bedroom.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[10])
    pygame.display.flip()
def screen13():
    bg('bedroom.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[11], 20, (255,0,0), 370, 360)
    pygame.display.flip()

#scene:morning
def screen14():
    bg('morning.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[12])
    pygame.display.flip()
def screen15():
    bg('morning.jpg')
    draw_button((width - 280) // 2, 100, 280, 60)
    draw_text(choice_list[3], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60)
    draw_text(choice_list[4], 20, font_color, 365, 220)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[12])
    pygame.display.flip()
def screen16():
    bg('morning.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[13])
    pygame.display.flip()

#scene:walking
def screen17():
    bg('walking.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[14])
    pygame.display.flip()
def screen18():
    bg('walking.jpg')
    draw_button((width - 280) // 2, 100, 280, 60)
    draw_text(choice_list[5], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60)
    draw_text(choice_list[6], 20, font_color, 365, 220)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[14])
    pygame.display.flip()
def screen19():
    bg('walking.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[15])
    pygame.display.flip()
def screen20():
    bg('walking.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[16])
    pygame.display.flip()
def screen21():
    bg('walking.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[17])
    pygame.display.flip()

#scene:entering class
def screen22():
    bg('class.png')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[18])
    pygame.display.flip()
def screen23():
    bg('class.png')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[19])
    pygame.display.flip()
def screen24():
    bg('class.png')
    popup_image('silhouette.png', 230, 100)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[20])
    pygame.display.flip()
def screen25():
    bg('class.png')
    popup_image('silhouette.png', 230, 100)
    draw_button((width - 280) // 2, 100, 280, 60)
    draw_text(choice_list[7], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60)
    draw_text(choice_list[8], 20, font_color, 365, 220)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[20])
    pygame.display.flip()
def screen26():
    bg('class.png')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[21])
    pygame.display.flip()
def screen27():
    bg('class.png')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[22])
    pygame.display.flip()
#scene:in class
def screen28():
    bg('class.png')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[23])
    pygame.display.flip()
def screen29():
    bg('class.png')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[24])
    pygame.display.flip()
def screen30():
    bg('class.png')
    draw_button((width - 280) // 2, 70, 280, 60)
    draw_text(choice_list[9], 20, font_color, 365, 100)
    draw_button((width - 280) // 2, 140, 280, 60)
    draw_text(choice_list[10], 20, font_color, 365, 170)
    draw_button((width - 280) // 2, 210, 280, 60)
    draw_text(choice_list[11], 20, font_color, 365, 240)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[24])
    pygame.display.flip()
def screen31():
    bg('class.png')
    popup_image('mrbean.jpg', 270, 100)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[25])
    pygame.display.flip()
def screen32():
    bg('class.png')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[26])
    pygame.display.flip()
def screen33():
    bg('class.png')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[27])
    pygame.display.flip()
def screen34():
    bg('class.png')
    popup_image('silhouette.png', 230, 100)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[28])
    pygame.display.flip()
def screen35():
    bg('class.png')
    popup_image('silhouette.png', 230, 100)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[29])
    pygame.display.flip()
def screen36():
    bg('class.png')
    popup_image('meme.jpg', 270, 100)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[30])
    pygame.display.flip()
#scene:class ending
def screen37():
    bg('class.png')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[31])
    pygame.display.flip()
def screen38():
    bg('class.png')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[32])
    pygame.display.flip()
def screen39():
    bg('class.png')
    popup_image('silhouette.png', 230, 100)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[33])
    pygame.display.flip()
def screen40():
    bg('class.png')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[34])
    pygame.display.flip()
def screen41():
    bg('class.png')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[35])
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
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text 
    popup_image('heart.png', 585, 3) #heart image
    pygame.display.flip()

#scene:walking back
def screen43():
    bg('walking.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[37])
    pygame.display.flip()
def screen44():
    bg('stall.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[38])
    pygame.display.flip()
def screen45():
    bg('stall.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[39])
    pygame.display.flip()
def screen46():
    bg('stall.jpg')
    draw_button((width - 280) // 2, 100, 280, 60)
    draw_text(choice_list[12], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60)
    draw_text(choice_list[13], 20, font_color, 365, 220)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[40])
    pygame.display.flip()
def screen47():
    bg('stall.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[41])
    pygame.display.flip()
def screen48():
    bg('stall.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[42])
    pygame.display.flip()
def screen49():
    bg('stall.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[43])
    pygame.display.flip()
def screen50():
    bg('walking.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[44])
    pygame.display.flip()
def screen51():
    bg('walking.jpg')
    draw_button((width - 280) // 2, 100, 280, 60)
    draw_text(choice_list[14], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60)
    draw_text(choice_list[15], 20, font_color, 365, 220)
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[44])
    pygame.display.flip()
def screen52():
    bg('walking.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[45])
    pygame.display.flip()
def screen53():
    bg('walking.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[46])
    pygame.display.flip()
def screen54():
    bg('walking.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[47])
    pygame.display.flip()
def screen55():
    bg('walking.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[48])
    pygame.display.flip()
def screen56():
    bg('walking.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[49])
    pygame.display.flip()
def screen57():
    bg('walking.jpg')
    popup_image('heartscore_bg.png',(width-150),-14) #heartscore background
    draw_text(f"Heart: {heart_score}", 25, score_color, 660, 20) #heart text
    popup_image('heart.png', 585, 3) #heart image
    draw_box() #dialogue box
    draw_text(dialogue_list[50])
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
           screen34, screen35, screen36, screen37, screen38, screen39, screen40, screen41, screen42, screen43, screen44, screen45, screen46, screen47, screen48, screen49, screen50,
           screen51, screen52, screen53, screen54, screen55, screen56, screen57, screen58]
    
#initialize the screen number
current_screen = 1

#initialize the score, the score starts with 3 hearts - LEE CHIA YING
heart_score = 3

#setting as False to repeat the loop when the user clicks on the incorrect button - LEE CHIA YING
loop_chosen = False


# Main loop
run = True
while run:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            newgame()
            run = False

        #navigation & saving data - YANG ALYA MYSARAH
        #heart score = LEE CHIA YING
        else:
                if current_screen == 6: #screen with choices
                    if navigate(380):
                        current_screen = 7 #the next screen that we want to navigate to
                        savedata(choice_list[0])
                    else:
                        current_screen = current_screen #the screen wont change if we click places other than the button
                elif current_screen == 0: #game over screen
                    heart_score = 3 #restart the heart score (now the player can restart the game)
                    if navigate(380):
                        current_screen = 1
                        savedata('play again')
                        newgame()
                    else:
                        current_screen = current_screen
                elif heart_score <= 0:
                    play_sound('badEnd.mp3')
                    current_screen = 0
                    heart_score = 3        
                elif current_screen == 9:
                    if navigate(100):
                        current_screen = 10
                        heart_score += 1
                        savedata(choice_list[1])
                    elif navigate(190):
                        play_sound('genshin.mp3')
                        current_screen = 11
                        heart_score -= 1
                        savedata(choice_list[2])
                    else:
                        current_screen = current_screen
                elif current_screen == 10:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen = 14
                elif current_screen == 15:
                    if navigate(100):
                        current_screen = 16
                        heart_score -= 1
                        savedata(choice_list[3]) 
                    elif navigate(190):
                        current_screen = 17
                        heart_score += 1
                        savedata(choice_list[4])
                    else:
                        current_screen = current_screen
                elif current_screen == 18:
                    if navigate(100):
                        play_sound('meow.mp3')
                        current_screen = 19
                        heart_score -= 1
                        savedata(choice_list[5])
                    elif navigate(190):
                        current_screen = 21
                        heart_score += 1
                        savedata(choice_list[6])
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
                        savedata(choice_list[7])
                    elif navigate(190):
                        current_screen = 27
                        heart_score -= 1
                        savedata(choice_list[8])
                    else:
                        current_screen = current_screen
                elif current_screen == 26:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen = 28
                elif current_screen == 30:
                    if navigate(70):
                        current_screen = 31
                        heart_score += 1
                        savedata(choice_list[9])
                    elif navigate(140):
                        current_screen = 32
                        heart_score -= 1
                        savedata(choice_list[10])
                    elif navigate(210):
                        current_screen = 33
                        heart_score -= 2
                        savedata(choice_list[11])
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
                        savedata(choice_list[12])
                    elif navigate(190):
                        current_screen = 48
                        savedata(choice_list[13])
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
                        savedata(choice_list[14])
                    elif navigate(190):
                        current_screen = 51
                        heart_score += 1
                        savedata(choice_list[15])
                    else:
                        current_screen = current_screen 
                elif current_screen == 54:
                    if pygame.mouse.get_pressed()[0] == 1:
                        current_screen = 57 
                elif current_screen == 58:
                    if navigate(380):
                        savedata('play again')
                        heart_score = 3
                        current_screen = 1
                        newgame()
                elif current_screen != 42:
                    if pygame.mouse.get_pressed()[0] == 1: #change to the next screen in order
                        current_screen += 1
            
    #loop for quiz game in screen 42 - LEE CHIA YING
    if current_screen == 42:    
            correct_ans_chosen = False  #setting as False to repeat the loop when the user clicks on the incorrect button
            
            if heart_score > 1:    #first choice made (happens outside the loop)
                if navigate(140):   # correct answer -> move to next page
                    savedata('correct answer')  
                    current_screen = 43  
                elif navigate(70) or navigate(210):
                    savedata('wrong answer')
                    heart_score -= 1
                    screen42()

                    while not correct_ans_chosen: #second and next choice made (in a loop)
                        for event in pygame.event.get(): #make sure the game can be properly exit even when inside the loop
                            if event.type == pygame.QUIT:
                                newgame()
                                run = False

                            elif event.type == pygame.MOUSEBUTTONDOWN: # when mouse button is clicked
                                if navigate(140):
                                    savedata('correct answer')
                                    correct_ans_chosen = True  # Exit the loop when the correct button is chosen
                                elif navigate(70) or navigate(210):
                                    if heart_score > 1:
                                        savedata('wrong answer')
                                        heart_score -= 1
                                        correct_ans_chosen = False # wrong answer; loop the question again
                                        screen42()
                                    else:
                                        correct_ans_chosen = True
                                else:
                                    correct_ans_chosen = False

            elif heart_score == 1: # final choice made (outside the loop)
                if navigate(140):
                    savedata('correct answer')
                    current_screen = 43
                elif navigate(70) or navigate(210): #if wrong answer is made, heart = 0 ; game over
                    savedata('wrong answer')
                    heart_score -= 1
                    play_sound('badEnd.mp3')
                    current_screen = 0

            
    #calling the screen function - FATIMAH NAJIHAH
    if 0 <= current_screen < len(screens): #the code will only work for the range of the existing number of screen
        screens[current_screen]()
    
    pygame.display.flip() #updates the display

pygame.quit() #quit pygame
