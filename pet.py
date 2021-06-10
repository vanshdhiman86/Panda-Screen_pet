from tkinter import Tk, HIDDEN, NORMAL, Canvas

def toggle_eyes():
    current_state = c.itemcget(pupil_left , 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left , state = new_state)
    c.itemconfigure(pupil_right , state = new_state)

def blink():
    toggle_eyes()
    win.after(250,toggle_eyes)
    win.after(3000,blink)

def toggle_pupils():
    if not c.crossed_eyes:
        c.move(pupil_left , 10,-5)
        c.move(pupil_right , -10,-5)
        c.crossed_eyes = True
    else:
        c.move(pupil_left , -10,5)
        c.move(pupil_right , 10,5)
        c.crossed_eyes = False

def toggle_tongue():
    if not c.tonque_out:
    	c.tonque_out = True#change
    	c.itemconfigure(tongue_tip , state = NORMAL)
    	c.itemconfigure(tongue_main , state = NORMAL)
    else:
        c.itemconfigure(tongue_tip , state = HIDDEN)
        c.itemconfigure(tongue_main , state = HIDDEN)
        c.tonque_out = False

def cheeky(event):
	toggle_tongue()
	toggle_pupils()
	hide_happy(event)
	win.after(1000,toggle_tongue)
	win.after(1000,toggle_pupils)
	return

def show_happy(event):
    if(20<= event.x and event.x <= 350) and (20<= event.y and event.y <= 350):
        c.itemconfigure(cheek_left , state = NORMAL)
        c.itemconfigure(cheek_right , state = NORMAL)
        c.itemconfigure(mouth_happy , state = NORMAL)
        c.itemconfigure(mouth_normal , state = HIDDEN)
        c.itemconfigure(mouth_sad, state = HIDDEN)
        c.happy_level = 10
    return

def hide_happy(event):
	if not c.tonque_out:
		c.itemconfigure(cheek_left , state = HIDDEN)
		c.itemconfigure(cheek_right , state = HIDDEN)
		c.itemconfigure(mouth_happy , state = HIDDEN)
		c.itemconfigure(mouth_normal , state = NORMAL)
		c.itemconfigure(mouth_sad, state = HIDDEN)
	else:
		c.itemconfigure(mouth_happy , state = HIDDEN)    #change
		c.itemconfigure(mouth_normal , state = HIDDEN)
		c.itemconfigure(mouth_sad, state = HIDDEN)
	return

def sad():
    if c.happy_level == 0 :
        c.itemconfigure(mouth_happy , state = HIDDEN)
        c.itemconfigure(mouth_normal , state = HIDDEN)
        c.itemconfigure(mouth_sad , state = NORMAL)
    else:
        c.happy_level -= 1
    win.after(500,sad)

""""def toogle_eye():
	if not c.hehe_eye:
		c.itemconfigure(pupil_left, state = HIDDEN)
		c.itemconfigure(pupil_right, state = HIDDEN)
		c.itemconfigure(eye_right2, state = NORMAL)
		c.itemconfigure(eye_left2, state = NORMAL)
		c.hehe_eye = True
	else:
		c.itemconfigure(eye_right2, state = HIDDEN)
		c.itemconfigure(eye_left2, state = HIDDEN)
		c.itemconfigure(pupil_left, state = NORMAL)
		c.itemconfigure(pupil_right, state = NORMAL)

		c.hehe_eye = False

def hehe(event):
	toogle_eye()
	win.after(1000,toogle_eye)
	return"""

win = Tk()

win.title("Panda")

c = Canvas(win , width=400 , height=400)
c.configure(bg='pink' , highlightthickness=0)

c.body_color = 'white'

ear_left = c.create_oval(75-10,10,75*2-10,80 , outline="grey20" , fill="grey20")
ear_right = c.create_oval(400-(75*2-10),10,400-75+10,80 , outline="grey20" , fill="grey20")

body = c.create_oval(35,20,365,350,outline="black" , fill=c.body_color)

"""foot_left = c.create_oval(65,320,145,360 , outline=c.body_color , fill=c.body_color)
foot_right = c.create_oval(250,320,330,360 , outline=c.body_color , fill=c.body_color)"""


eye_left = c.create_oval(90,110,180,190,outline='grey20' , fill='grey20')
eye_right = c.create_oval(210,110,300,190,outline='grey20' , fill='grey20')
eye_left2 = c.create_oval(130,145,160,155,outline='black' , fill="black",state=HIDDEN)
eye_right2 = c.create_oval(230,145,260,155,outline='black' , fill="black",state=HIDDEN)
pupil_left = c.create_oval(145,140,160,155,outline='black' , fill='black',state=NORMAL)
pupil_right = c.create_oval(230,140,245,155,outline='black' , fill='black',state=NORMAL)


mouth_normal = c.create_line(170+10,270,200+10,272,230+10,250, smooth=1 , width=2 ,state=NORMAL)
mouth_happy = c.create_line(170,250,200,282,230,250,smooth=1 , width=2 , state=HIDDEN)
mouth_sad = c.create_line(170,260,200,232+10,230,260,smooth=1 , width=2 , state=HIDDEN)

tongue_main = c.create_rectangle(170,250,230,290,outline='black' , fill='black',state=HIDDEN)
tongue_tip = c.create_oval(170,275,230,300,outline='black' , fill='red',state=HIDDEN)

cheek_left = c.create_oval(70,180+15,120,230+10,outline='misty rose' , fill='misty rose',state=HIDDEN)
cheek_right = c.create_oval(280,180+15,330,230+10,outline='misty rose' , fill='misty rose',state=HIDDEN)

#nose = c.create_oval(200-30,210,200+30,230, outline="black", fill="black")
nose = c.create_oval(200-20,210,200+20,225, outline="black", fill="black")
nose_curve = c.create_line(150,200,200,180,250,200, smooth=1 , width=1)
#nose_curve = c.create_line(160,215+10,200-40,175,230-20,200-15, smooth=1 , width=1 ,state=NORMAL)
c.pack()

c.bind('<Motion>' , show_happy)
c.bind('<Leave>' , hide_happy)
c.bind('<Double-1>' , cheeky)
#c.bind('<Button-1>', hehe)

c.crossed_eyes = False
c.tonque_out = False
c.happy_level = 10
#c.hehe_eye = False

win.after(1000,blink)
win.after(5000,sad)

win.mainloop()