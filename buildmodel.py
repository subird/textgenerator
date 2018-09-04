import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--input', help='Text input file', required=True)
parser.add_argument('-o','--output', help='Output file for model', required=True)
args = vars(parser.parse_args())

file = open(args['input'], "r")
words = " ".join([i.rstrip() for i in file.readlines()]).replace('<p>', "").replace('</p>', '<br>').lower().split()
dic = dict()

for i in range(1, len(words)):
	word1 = words[i - 1]
	word2 = words[i]
	dic[word1] = dic.get(word1, dict())
	dic[word1][word2] = dic[word1].get(word2, 0) + 1

dic[words[-1]] = dic.get(words[-1], dict())
print(dic, file=open(args['output'], "w"))