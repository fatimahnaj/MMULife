import pygame
from Text import choice_list, quiz_options_list, dialogue_list

pygame.init()

# set up the display
screen_size = (720,480) # give screen size
screen = pygame.display.set_mode(screen_size) # opens up a window 
pygame.display.set_caption('MMULife') # window name

#images
bg_opening = pygame.image.load('opening.jpg')
bg_bedroom = pygame.image.load('bedroom.jpg')
bg_morning = pygame.image.load('morning.jpg')
bg_walking = pygame.image.load('walking.jpg')
bg_class = pygame.image.load('class.png')
bg_stall = pygame.image.load('stall.jpg')

# stores the width & height of the screen into a variable
# to be used for centering objects
width = screen.get_width()  
height = screen.get_height() 

#define font color
font_color = (91, 72, 59)

#font color for heart score
score_color = (255, 0, 0)

#font color for quiz 
quiz_color = (0, 0, 153)

#button color
button_color = (184, 174, 159)

# #button color for quiz
# button_quiz_color = (153, 255, 255)

#button for the choices
def popup_image(image_link,x,y):
    image = pygame.image.load(image_link)
    screen.blit(image, (x, y))
    

def draw_button(x, y, width, height, color):
    set_button = pygame.Rect(x, y, width, height)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if set_button.collidepoint(mouse_x, mouse_y):
        color = (146, 146, 145)
    else:
        color = (184, 174, 159)
    pygame.draw.rect(screen, color, set_button)
    
#box (will act as background for text)
def draw_box(x, y, width, height, color):
    set_box = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, set_box)

#draw text
def draw_text(text, size, color, x, y):
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
    

#screens

#scene: introduction       
def screen1():
    screen.blit(bg_opening, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[0], 20, font_color, 370, 360)
    pygame.display.flip()
def screen2():
    screen.blit(bg_opening, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[1], 20, font_color, 370, 360)
    pygame.display.flip()
def screen3():
    screen.blit(bg_opening, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[2], 20, font_color, 370, 360)
    pygame.display.flip()
def screen4():
    screen.blit(bg_opening, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[3], 20, font_color, 370, 360)
    pygame.display.flip()
def screen5():
    screen.blit(bg_opening, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[4], 20, font_color, 370, 360)
    pygame.display.flip()
def screen6():
    screen.blit(bg_opening, (0,0))
    draw_button((width - 280) // 2, 160, 280, 60, button_color)
    draw_text(choice_list[0], 20, font_color, 365, 193)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[5], 20, font_color, 370, 360) 
    pygame.display.flip()

#scene:bedroom
def screen7():
    screen.blit(bg_bedroom, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[6], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()
def screen8():
    screen.blit(bg_bedroom, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[7], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()
def screen9():
    screen.blit(bg_bedroom, (0,0))
    draw_button((width - 280) // 2, 100, 280, 60, button_color)
    draw_text(choice_list[1], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60, button_color)
    draw_text(choice_list[2], 20, font_color, 365, 220)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[7], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()
def screen10():
    screen.blit(bg_bedroom, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[8], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()
def screen11():
    screen.blit(bg_bedroom, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[9], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()
def screen12():
    screen.blit(bg_bedroom, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[10], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()
def screen13():
    screen.blit(bg_bedroom, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[11], 20, (255,0,0), 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()

#scene:morning
def screen14():
    screen.blit(bg_morning, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[12], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()
def screen15():
    screen.blit(bg_morning, (0,0))
    draw_button((width - 280) // 2, 100, 280, 60, button_color)
    draw_text(choice_list[3], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60, button_color)
    draw_text(choice_list[4], 20, font_color, 365, 220)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[12], 20, font_color, 370, 360)
    # correct_button()
    pygame.display.flip()
def screen16():
    screen.blit(bg_morning, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[13], 20, font_color, 370, 360)
    # correct_button()
    pygame.display.flip()

#scene:walking
def screen17():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[14], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()
def screen18():
    screen.blit(bg_walking, (0,0))
    draw_button((width - 280) // 2, 100, 280, 60, button_color)
    draw_text(choice_list[5], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60, button_color)
    draw_text(choice_list[6], 20, font_color, 365, 220)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[14], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()
def screen19():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[15], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()
def screen20():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[16], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()
def screen21():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[17], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()

#scene:entering class
def screen22():
    screen.blit(bg_class, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[18], 20, font_color, 370, 360)
    draw_text(f"Heart: {heart_score}", 20, score_color, 650, 15) 
    pygame.display.flip()
def screen23():
    screen.blit(bg_class, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[19], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen24():
    screen.blit(bg_class, (0,0))
    popup_image('silhouette.png', 230, 100)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[20], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen25():
    screen.blit(bg_class, (0,0))
    popup_image('silhouette.png', 230, 100)
    draw_button((width - 280) // 2, 100, 280, 60, button_color)
    draw_text(choice_list[7], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60, button_color)
    draw_text(choice_list[8], 20, font_color, 365, 220)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[20], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen26():
    screen.blit(bg_class, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[21], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen27():
    screen.blit(bg_class, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[22], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
#scene:in class
def screen28():
    screen.blit(bg_class, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[23], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen29():
    screen.blit(bg_class, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[24], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen30():
    screen.blit(bg_class, (0,0))
    draw_button((width - 280) // 2, 70, 280, 60, button_color)
    draw_text(choice_list[9], 20, font_color, 365, 100)
    draw_button((width - 280) // 2, 140, 280, 60, button_color)
    draw_text(choice_list[10], 20, font_color, 365, 170)
    draw_button((width - 280) // 2, 210, 280, 60, button_color)
    draw_text(choice_list[11], 20, font_color, 365, 240)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[24], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen31():
    screen.blit(bg_class, (0,0))
    popup_image('mrbean.jpg', 270, 100)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[25], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen32():
    screen.blit(bg_class, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[26], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen33():
    screen.blit(bg_class, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[27], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen34():
    screen.blit(bg_class, (0,0))
    popup_image('silhouette.png', 230, 100)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[28], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen35():
    screen.blit(bg_class, (0,0))
    popup_image('silhouette.png', 230, 100)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[29], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen36():
    screen.blit(bg_class, (0,0))
    popup_image('meme.jpg', 270, 100)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[30], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
#scene:class ending
def screen37():
    screen.blit(bg_class, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[31], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen38():
    screen.blit(bg_class, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[32], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen39():
    screen.blit(bg_class, (0,0))
    popup_image('silhouette.png', 230, 100)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[33], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen40():
    screen.blit(bg_class, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[34], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen41():
    screen.blit(bg_class, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[35], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()

def screen42():
    # global correct_ans_chosen
    screen.blit(bg_class, (0,0))
    draw_button((width - 280) // 2, 70, 280, 60, button_color)
    draw_text(quiz_options_list[0], 20, quiz_color, 365, 100)
    draw_button((width - 280) // 2, 140, 280, 60, button_color)
    draw_text(quiz_options_list[1], 20, quiz_color, 365, 170)
    draw_button((width - 280) // 2, 210, 280, 60, button_color)
    draw_text(quiz_options_list[2], 20, quiz_color, 365, 240)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[36], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
#scene:walking back
def screen43():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[37], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen44():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[38], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen45():
    screen.blit(bg_stall, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[39], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen46():
    screen.blit(bg_stall, (0,0))
    draw_button((width - 280) // 2, 100, 280, 60, button_color)
    draw_text(choice_list[12], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60, button_color)
    draw_text(choice_list[13], 20, font_color, 365, 220)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[40], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen47():
    screen.blit(bg_stall, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[41], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen48():
    screen.blit(bg_stall, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[42], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen49():
    screen.blit(bg_stall, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[43], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen50():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[44], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen51():
    screen.blit(bg_walking, (0,0))
    draw_button((width - 280) // 2, 100, 280, 60, button_color)
    draw_text(choice_list[14], 20, font_color, 365, 133)
    draw_button((width - 280) // 2, 190, 280, 60, button_color)
    draw_text(choice_list[15], 20, font_color, 365, 220)
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[44], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen52():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[45], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen53():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[46], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen54():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[47], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen55():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[48], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen56():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[49], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen57():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[50], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()
def screen58():
    screen.blit(bg_walking, (0,0))
    draw_box(10, 330, 700, 140, (184, 174, 159))
    draw_text(dialogue_list[51], 20, font_color, 370, 360)
    draw_text(f"Score: {heart_score}", 20, font_color, 650, 15)
    pygame.display.flip()

#putting all the screens into a list
screens = [screen1,screen2, screen3, screen4, screen5, screen6, screen7, screen8, screen9, screen10, screen11, screen12, screen13, screen14, screen15, screen16, screen17,
           screen18, screen19, screen20, screen21, screen22, screen23, screen24, screen25, screen26, screen27, screen28, screen29, screen30, screen31, screen32, screen33, 
           screen34, screen35, screen36, screen37, screen38, screen39,  screen41, screen42, screen43, screen44, screen45, screen46, screen47, screen48, screen49, screen50,
           screen51, screen52, screen53, screen54, screen55, screen56, screen57, screen58]

#initialize the score, the score starts with 3 hearts
heart_score = 3
#initialize the screen number
current_screen = 0

def navigate(y):
    set_button = pygame.Rect((width - 280) // 2, y, 280, 60)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if set_button.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] == 1:
        return True
    else:
        return False
    
correct_ans_chosen = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Check if left mouse button is clicked (will change later)
        else:
            if current_screen == 5: #screen yg ada choices
                if navigate(160) == True:
                    current_screen = 6 #next screen yg kita nak navigate to
                    heart_score += 1
                    #print(f"Score: {heart_score}, 20, font_color, 100, 50")
                else:
                    current_screen = current_screen #the screen wont change if tak tekan the button

            elif current_screen == 8:
                if navigate(100) == True:
                    current_screen = 10
                    heart_score += 1
                elif navigate(190) == True:
                    current_screen = 11
                    heart_score -= 1
                else:
                    current_screen = current_screen #the screen wont change if tak tekan the button

            elif current_screen == 41 and not correct_ans_chosen:
                while not correct_ans_chosen:
                    if navigate (70) == True:
                        break

            # move to next screen (in order)
            else:
                if pygame.mouse.get_pressed()[0] == 1:
                    current_screen += 1
                

    # Call the current screen function
    screens[current_screen]()


