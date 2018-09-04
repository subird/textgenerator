import random
import argparse

def next(word):
	ptr = random.randint(0, sum(model[word].values()) - 1)
	for key in model[word].keys():
		if ptr < model[word][key]:
			return key
		else:
			ptr -= model[word][key]

parser = argparse.ArgumentParser()
parser.add_argument('-i','--input', help='Model input file', required=True)
parser.add_argument('-o','--output', help='Output file', required=True)
parser.add_argument('-l','--length', help='Number of words in text', required=True)
args = vars(parser.parse_args())

global model
exec("model=" + open(args['input'], "r").readline().rstrip())

word = random.choice(list(model.keys()))
text = word
for i in range(int(args['length']) - 1):
	word = next(word)
	text += " " + word

print(text.replace("<br>", '\n'), file=open(args['output'], "w"))