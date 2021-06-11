from psychopy import visual, core, event, gui, sound
import numpy as np 
import random, pandas
import sys
import csv


# GUI that collects pp info 
def PPinfo ():	
	parti_info = gui.Dlg(title = 'Participant Info')
	parti_info.addField('Subject id (iiddmmyy)')
	parti_info.addField('Subject number')
	ok_input = parti_info.show()
	if parti_info.OK:
		if '' in ok_input:
			warningwin = visual.Window(color = (1,1,1), size = (1280,720), monitor='testmonitor')
			warningtext = visual.TextStim(warningwin, text = 'Please fill all the required info',
		                                              height = 0.2,
		                                              pos = (0, 0.1),
		                                              color = (-1,-1,-1))
			warningtext.draw()
			warningwin.flip()
			core.wait(2)
			warningwin.close()
			PPinfo()
		else:
			print(ok_input)
			return ok_input
	else:
		print('Participant cancelled')
		core.quit()
		return [1,2,3]
 
par_info = PPinfo()

#-----RATINGS------#

# INSTRUCTION 1
win1 = visual.Window(color = (-1,-1,-1), size = (1280,720), monitor = 'TestMonitor')
instrct = visual.TextStim(win1, color = (1,1,1), height = 0.05)
win1.mouseVisible = False
instrct.text = 'The scale you will use today starts at "no sensation" and ends at the "strongest imaginable sensation" of any kind. For example, think of staring at the sun, hearing a jet plane take off or a terrible pain. Whatever kind of sensation would be the strongest for you should go at the top of the scale. You will be asked to rate the intensity of a variety of remembered or imagined sensations by indicating where they fall on the scale. \n \n When you are using the scale be sure and separate how intense something is from how much you like it or dislike it. For example, if something is weakly bitter and you dislike bitter, do not be tempted to rate it as more bitter because you do not like it. \n \n Finally, remember that the top is the strongest sensation of any kind which represents the most intense sensation you might experience across any time of sensation. What you perceive to be the strongest sensation across items. It is very important that the same sensation is at the top of the scale for each sensation you rate. Before you begin tasting, you will hear a series of sounds. Please scale them according to their intensity. \n \n \n \n \n \n                                        Press SPACE to continue'
instrct.draw()
win1.flip()
event.waitKeys(maxWait = np.inf, keyList = ['space'])



# RATING LOUDNESS

y = 0	#to be used in line 150
sound_list = [0.2,0.4,0.6,0.8,1] #psychopy levels; DB depend on how loud you play from pc
current_noise =[]		#creating global variables to later be saved in csv
loudness_rating =[]
drop_rating = []

def noise():
	global sound_list
	global current_noise
	from psychopy.sound import Sound
	win1.mouseVisible = False
	win1.flip()
	timer = core.CountdownTimer(4)		
	curr_noise = random.choice(sound_list)
	highA = sound.Sound(value = 1000, secs=2, octave=3, stereo=True, volume = curr_noise, name = curr_noise)
	core.wait(2)
	highA.play()
	core.wait(2) #sound is played for 2 seconds
	highA.stop()
	current_noise.append(curr_noise)
	values = sound_list.remove(curr_noise)	 #removes the random sound that was played in this trial from the sound_list
	if timer.getTime() == 0:
		win1.flip()



def Loudness():
	text_scale = visual.TextStim(win1, text = '''Use the mouse to respond on the scale below 
												\n      and click on the box below to continue''', pos=(0,0.5), height = 0.05)											
	
	No_Sensation = visual.TextStim(win1, text = "*", pos = (-0.734, -0.25), height = 0.08)
	Barely = visual.TextStim(win1, text = "*", pos = (-0.719, -0.25), height = 0.08)
	Weak = visual.TextStim(win1, text = "*", pos = (-0.646, -0.25), height = 0.08)
	Moderate = visual.TextStim(win1, text = "*", pos = (-0.352, -0.25), height = 0.08)
	Strong = visual.TextStim(win1, text = "*", pos = (-0.235, -0.25), height = 0.08)
	VeryStrong = visual.TextStim(win1, text = "*", pos = (0,-0.25), height = 0.08)
	Strongest = visual.TextStim(win1, text = "*", pos = (0.734, -0.25), height = 0.08)

			#Here		Real%
			#734 	= 	100	Strongest Imaginable
			#0		=	50 	Very Strong
			#-235	=	34	Strong
			#-352	= 	26	Moderate
			#-646	= 	6	Weak
			#-719	= 	1	Barely
			#-734	=	0	Not perceptible
			#This applies to the "*" markers. The words I manually tweaked.
			
	No_Sensation1 = visual.TextStim(win1, text = "No Sensation", pos = (-0.735, -0.089), height = 0.04, ori = -90)
	Barely1 = visual.TextStim(win1, text = "Barely Perceptible", pos = (-0.715, -0.048), height = 0.04, ori = -90)
	Weak1 = visual.TextStim(win1, text = "Weak", pos = (-0.646, -0.15), height = 0.04, ori = -90)
	Moderate1 = visual.TextStim(win1, text = "Moderate", pos = (-0.352, -0.12), height = 0.04, ori = -90)
	Strong1 = visual.TextStim(win1, text = "Strong", pos = (-0.235, -0.143), height = 0.04, ori = -90)
	VeryStrong1 = visual.TextStim(win1, text = "Very Strong", pos = (0,-0.10), height = 0.04, ori = -90)
	Strongest1 = visual.TextStim(win1, text = "Strongest imaginable \nsensation of any kind", pos = (0.74, -0.025), height = 0.04, ori = -90)

	scale_1 = visual.RatingScale(win1, 
								   low = 0,
	                               high = 100,
	                               labels = ['0','10','20','30','40','50','60','70','80','90','100'],
								   tickMarks = ['0','10','20','30','40','50','60','70','80','90','100'],
	                               size = 0.7,
	                               stretch = 3.5,
	                        	   textSize = 1,
	                        	   tickHeight = -1, 
	                               precision = 1,
	                               pos = (0, -0.25),
	                               markerStart = np.random.randint(0,100),
	                               lineColor = 'White',
	                               markerColor = 'White',
	                               textColor = 'White',
	                               showValue = True)      
			                                                               	
	while scale_1.noResponse:
		win1.mouseVisible = True
		text_scale.draw()
		scale_1.draw()	
		No_Sensation.draw();	
		Barely.draw()
		Weak.draw()
		Moderate.draw()
		Strong.draw()
		VeryStrong.draw()
		Strongest.draw()
		No_Sensation1.draw()
		Barely1.draw()
		Weak1.draw()
		Moderate1.draw()
		Strong1.draw()
		VeryStrong1.draw()
		Strongest1.draw()
		win1.flip()
	loud_rating = scale_1.getRating()
	loudness_rating.append(loud_rating)


while y < 5:		# The Actual Trial
	noise()
	Loudness()
	y +=1




# INSTRUCTION 2: How bad was the drop?
win1.mouseVisible = False
win1.flip()
instrct.text = 'You will now taste the solution.\n\n\n\n\n\n\n\n\n\n\n    Press SPACE to Continue.' 
instrct.draw()
win1.flip()
event.waitKeys(maxWait = np.inf, keyList = ['space'])

def Drop ():
	text_scale = visual.TextStim(win1, text = 'How strongly did the solution taste to you?', pos=(0,0.5), height = 0.05)											
	
	No_Sensation = visual.TextStim(win1, text = "*", pos = (-0.734, -0.25), height = 0.08)
	Barely = visual.TextStim(win1, text = "*", pos = (-0.719, -0.25), height = 0.08)
	Weak = visual.TextStim(win1, text = "*", pos = (-0.646, -0.25), height = 0.08)
	Moderate = visual.TextStim(win1, text = "*", pos = (-0.352, -0.25), height = 0.08)
	Strong = visual.TextStim(win1, text = "*", pos = (-0.235, -0.25), height = 0.08)
	VeryStrong = visual.TextStim(win1, text = "*", pos = (0,-0.25), height = 0.08)
	Strongest = visual.TextStim(win1, text = "*", pos = (0.734, -0.25), height = 0.08)

	No_Sensation1 = visual.TextStim(win1, text = "No Sensation", pos = (-0.735, -0.089), height = 0.04, ori = -90)
	Barely1 = visual.TextStim(win1, text = "Barely Perceptible", pos = (-0.715, -0.048), height = 0.04, ori = -90)
	Weak1 = visual.TextStim(win1, text = "Weak", pos = (-0.646, -0.15), height = 0.04, ori = -90)
	Moderate1 = visual.TextStim(win1, text = "Moderate", pos = (-0.352, -0.12), height = 0.04, ori = -90)
	Strong1 = visual.TextStim(win1, text = "Strong", pos = (-0.235, -0.143), height = 0.04, ori = -90)
	VeryStrong1 = visual.TextStim(win1, text = "Very Strong", pos = (0,-0.10), height = 0.04, ori = -90)
	Strongest1 = visual.TextStim(win1, text = "Strongest imaginable \nsensation of any kind", pos = (0.74, -0.025), height = 0.04, ori = -90)

	Drop_Scale = visual.RatingScale(win1, 
								  low = 0,
	                               high = 100,
	                               labels = ['0','10','20','30','40','50','60','70','80','90','100'],
								   tickMarks = ['0','10','20','30','40','50','60','70','80','90','100'],
	                               size = 0.7,
	                               stretch = 3.5,
	                        	   textSize = 1,
	                        	   tickHeight = -1, 
	                               precision = 1,
	                               pos = (0, -0.25),
	                               markerStart = np.random.randint(0,100),
	                               lineColor = 'White',
	                               markerColor = 'White',
	                               textColor = 'White',
	                               showValue = True)
	while Drop_Scale.noResponse:
		win1.mouseVisible = True
		text_scale.draw()
		Drop_Scale.draw()	
		No_Sensation.draw()
		Barely.draw()
		Weak.draw()
		Moderate.draw()
		Strong.draw()
		VeryStrong.draw()
		Strongest.draw()
		No_Sensation1.draw()
		Barely1.draw()
		Weak1.draw()
		Moderate1.draw()
		Strong1.draw()
		VeryStrong1.draw()
		Strongest1.draw()
		win1.flip()
	drop_rate = Drop_Scale.getRating()
	drop_rating.append(drop_rate)

Drop()



#OPEN CSV AND SAVE DATA
trials = (' ', 'trial 1', 'trial 2', 'trial 3', 'trial 4', 'trial 5')
noise = ('current_noise',current_noise)
loud = ('loudness_rating', loudness_rating)
drop =('drop_rating', drop_rating)

with open('%s.csv'%(par_info[0]), 'w') as csvfile:
	w = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	w.writerow(trials)
	w.writerow(noise)
	w.writerow(loud)
	w.writerow(drop)
	csvfile.close



#------DROP SELECTON TASK------#


# OPEN CSV FOR NEW TASK 
dataFile = open('%s.csv'%(par_info[0] +'_'+ par_info[1]), 'a')
dataFile.write('Subject id (iiddmmyy)'+','+'Subject number'+','+'\n')

for i in list(range(len(par_info))):
	dataFile.write(par_info[i]+',')
dataFile.write('\n')
# Trials=ijk+1  Trial Num=ij+1  
dataFile.write('Times'+','+'Trial Num'+','
				+'drop Left'+','+'Money Left'+','
				+'drop Right'+','+'Money Right'+','
				+'Choice'+','+'RT'+','
				+'drops for'+','+'FixationTime'+','
				+'\n')


# Present Fixation
def Fixation ():
	ITI = [1, 2, 3]
	FixTime = random.sample(ITI, 1)
	Fixation = visual.TextStim(win1, text = '+', pos =(0,0),
	                             height = 0.3, color = (1,1,1))
	Fixation.draw()
	win1.flip()
	core.wait(FixTime[0])
	return FixTime[0]

# Instruction 3
win1.mouseVisible = False
win1.flip()
instrct.text = '     Please choose between the two choices with \nthe LEFT and RIGHT arrow keys on your keyboard.\n\n\n\n\n\t\tPress SPACE to Continue.'
instrct.draw()
win1.flip()
event.waitKeys(maxWait = np.inf, keyList = ['space'])


# Import trial info
trial_info = pandas.read_csv('trial_info.csv', header = None)
trial_order = list(range(trial_info.iloc[:,0].size))
random.shuffle(trial_order)

# Fixation and Receiver info
# trial_order[ijk] == ij
ijk=-1
for ij in trial_order:
	ijk += 1
	Text_receiverInfo = visual.TextStim(win1, text = '',  height = 0.2)
	backgoundColor = [[0,0,0],[0,0,139]]
	win1.colorSpace = 'rgb255'
	if trial_info.iat[ij,2] == 1:
		dropsfor = 'You'
		win1.color = backgoundColor[0]
		win1.flip()
		win1.flip()
		Fixtime = Fixation()
		if ijk==0 or (ijk>0 and trial_info.iat[trial_order[ijk-1],2]!=1):         
			Text_receiverInfo.text = 'Drops for : YOU'
			Text_receiverInfo.draw()
			win1.flip()
			core.wait(3)
	else:
		dropsfor = 'Receiver'
		win1.color = backgoundColor[1]
		win1.flip()
		win1.flip()
		Fixtime = Fixation()
		if ijk==0 or (ijk>0 and trial_info.iat[trial_order[ijk-1],2]==1):
			Text_receiverInfo.text = 'Drops for : RECEIVER'
			Text_receiverInfo.draw()
			win1.flip()
			core.wait(3)
	dropAmount = [trial_info.iat[ij,0],trial_info.iat[ij,3]]
	moneyAmount = [trial_info.iat[ij,1],trial_info.iat[ij,4]]
	if trial_info.iat[ij,5] == 1:
		dropAmount = [trial_info.iat[ij,3],trial_info.iat[ij,0]]
		moneyAmount = [trial_info.iat[ij,4],trial_info.iat[ij,1]]
	arrow_1 = visual.ImageStim(win1, 'arrow.PNG', pos = (-0.5, 0))
	arrow_2 = visual.ImageStim(win1, 'arrow.PNG', pos = (0.5,0))
	dropMark_left = visual.ImageStim(win1, 'dropmark.png', 
											pos = (-0.66,dropAmount[0]/20-0.5),
											size =(0.04,0.08))	
	dropMark_right = visual.ImageStim(win1, 'dropmark.png', 
										pos = (0.34,dropAmount[1]/20-0.5),
										size = (0.04,0.08))				
	text_leftS = visual.TextStim(win1, text = '', 
										height = 0.1, 
										pos = (-0.6,dropAmount[0]/20-0.5), 
										color = 'white')
	text_rightS = visual.TextStim(win1, text = '', 
										height = 0.1, 
										pos = (0.4,dropAmount[1]/20-0.5),
										color = 'white')
	text_leftM = visual.TextStim(win1, text = '', 
										height = 0.1, 
										pos = (-0.4,dropAmount[0]/20-0.5), 
										color = 'white')
	text_rightM = visual.TextStim(win1, text = '', 
										height = 0.1, 
										pos = (0.6,dropAmount[1]/20-0.5), 
										color = 'white')
	text_leftS.text = str(dropAmount[0])
	text_rightS.text = str(dropAmount[1])
	text_leftM.text = '$'+ str(moneyAmount[0])
	text_rightM.text = '$'+ str(moneyAmount[1])
	arrow_1.draw()
	arrow_2.draw()
	dropMark_left.draw()
	dropMark_right.draw()
	text_leftS.draw()
	text_rightS.draw()
	text_leftM.draw()
	text_rightM.draw()
	win1.flip()
	timer_1 = core.Clock()
	choiceKey = event.waitKeys(maxWait = 5, keyList = ['left','right'])
	if not choiceKey:
		Warn = visual.TextStim(win1, text = 'Please respond faster', height = 0.3)
		Warn.draw()
		win1.flip()
		core.wait(3)
		trial_order.append(ij)
		RT = 'overtime'
		choiceKey = ['none']
	elif 'left' in choiceKey:
		RT = str(timer_1.getTime())
		frame = visual.ImageStim(win1, 'frame.PNG',
										pos = (-0.493, -0.80),
										size = 0.15)
		arrow_1.draw()
		arrow_2.draw()
		dropMark_left.draw()
		dropMark_right.draw()
		text_leftS.draw()
		text_rightS.draw()
		text_leftM.draw()
		text_rightM.draw()
		frame.draw()
		win1.flip()
		core.wait(2)
	elif 'right' in choiceKey:
		RT = str(timer_1.getTime())
		frame = visual.ImageStim(win1, 'frame.PNG',
										pos = (0.51, -0.80),
										size = 0.15)
		arrow_1.draw()
		arrow_2.draw()
		dropMark_left.draw()
		dropMark_right.draw()
		text_leftS.draw()
		text_rightS.draw()
		text_leftM.draw()
		text_rightM.draw()
		frame.draw()
		win1.flip()
		core.wait(2)
	timer_1.reset()
	key_escape = event.waitKeys(maxWait = 2, keyList = ['escape'])
	if not key_escape:
		key_escape = ['Not_quit']
	else:
		win1.close()
		core.quit()	
	dataFile.write(str(ijk+1)+','+str(ij+1)+','
					+str(dropAmount[0])+','+str(moneyAmount[0])+','
					+str(dropAmount[1])+','+str(moneyAmount[1])+','
					+choiceKey[0]+','+RT+','+dropsfor+','
					+str(Fixtime)+'\n')

#FINISHING UP
ending = visual.TextStim(win1, text = 'Thanks for participating. Press SPACE to quit.')
ending.draw()
win1.flip()
event.waitKeys(maxWait=np.inf, keyList=['space'])

win1.close()
core.quit()