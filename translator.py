import ui
import re
from WordTranslate import WordTranslate


def click_button(sender):
	label = sender.superview['label1']
	textbox = sender.superview['textfield1']

	#assign variables from UI values
	translateControl = sender.superview['segmentedcontrol1']
	label.alignment = ui.ALIGN_CENTER
	translateWord = textbox.text

	#set language based on segmented control
	if translateControl.selected_index == 0:
		language = 'EN'
	else:
		language = 'TR'

	#create new WordTranslate object and translate word
	word = WordTranslate(translateWord, language)
	label.text = word.translate()


#setup view for UI		
v = ui.load_view()
v.present('sheet')
