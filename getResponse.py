from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import sys
import spacy
sys.path.append('/Scripts')
nlp = spacy.load("en_core_web_sm")
chatbot = ChatBot('snorg')

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Train the chatbot based on the english corpus
granddat = []
texts = [] #input textfiles here
def boot():
	chatbot.storage.drop()
	for string in texts:
		text = open(string)
		my_text = text.readlines()
		for line in my_text:
			granddat.append(line)
	n = 20
	l = len(granddat)
	i = -n
	while i < l:
		i+=n
		if i+n>=l: trainer.train(granddat[i:])
		else: trainer.train(granddat[i:i+n])
		print(str(i+n) + " out of: " + str(l) + " lines trained")
		print("{:.2f}".format(i/l*100) + "% complete")
		
	print("******* " + str(l) + " lines of text learned from!")
	print("******* " + "{:.2f}".format(l/n) + " conversations had!")

# Get a response to an input statement


def getResponse(msg):
	r = chatbot.get_response(msg)
	return(r)

def autoLearn(text):
	trainer.train(text)
def append(learn):
	ai = open("ai.txt","a")
	for line in learn:
		ai.write("\n")
		ai.write(line)
	ai.close()