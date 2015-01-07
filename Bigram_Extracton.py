import re
import sys
import nltk
import random
import itertools
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
#from featx import bag_of_words

pos = open('/media/Gizmos/Random Works/Dev/Review/posr.txt', 'r')
posread = pos.readlines()
#print posread

neg = open('/media/Gizmos/Random Works/Dev/Review/negr.txt', 'r')
negread = neg.readlines()

sto=open('/media/Gizmos/Random Works/Dev/stw.txt', 'r')
stopw=sto.read()

#print stopw
#print posread
#print negread


onlyNegative=[]
onlyPositive=[]

for i in range(0,len(posread)):
	onlyPositive.append('positive')

for i in range(0,len(negread)):
	onlyNegative.append('negative')

###Tuples with sentiment tagged
postagged = zip(posread, onlyPositive)
negtagged = zip(negread, onlyNegative)

###Combining both the tagged reviews
taggedReview = postagged + negtagged
#print taggedReview
'''
print 'Printing tagged Reviews........'
for i in taggedReview:
	print i
'''

reviews=[]

#Create a list of words in the review, within a tuple.
for (word, sentiment) in taggedReview:
	word_filter = [i.lower() for i in word.split()]
	reviews.append((word_filter, sentiment))

#print reviews

'''
print '\n\n###############################\nPrinting List of words\n#################################\n\n'
for line in reviews:
	print line
'''

selected_bgram=[]
cnt=0
print cnt
for(tk,sentiment)in reviews:
	#print cnt,'==>',tk
	bgram_words=nltk.bigrams(tk)
	#print bgram_words
	i=0
	bgram_ptag=nltk.bigrams(nltk.pos_tag(tk))
	#print bgram_ptag
	rr=[]
	for kk in bgram_ptag:
		#print kk
		#Check For Negation i.e not Support , not satisfied
		if ((kk[0][1]=='RB' or kk[0][1]=='RBR' or kk[0][1]=='RBS') and (kk[1][1]=='VB' or kk[1][1]=='VBD' or kk[1][1]=='VBG' or kk[1][1]=='VBN')):
			#print cnt,'==>',tk,'\n','Rule1 >',kk
			#print bgram_words[i]
			rr.append((bgram_words[i][0],bgram_words[i][1]))

		#check for Adjective and noun i.e horrible battery low voice
		if kk[0][1]=='JJ' and kk[1][1]=='NN':
			#print cnt,'==>',tk,'\n','Rule2 >',kk
			#print bgram_words[i]
			rr.append((bgram_words[i][0],bgram_words[i][1]))


		#check for adverd folowed by adjective i.e not worthy,not Good, very Bad
		if (kk[0][1]=='RB' or kk[0][1]=='RBR' or kk[0][1]=='RBS') and kk[1][1]=='JJ':
			#print cnt,'==>',tk,'\n','Rule3 >',kk
			rr.append((bgram_words[i][0],bgram_words[i][1]))

		#check for noun followed by adjective i.e waste of
		if (kk[0][1]=='NN' or kk[0][1]=='NNS') and kk[1][1]=='JJ':
			#print cnt,'==>',tk,'\n','Rule4 >',kk
			rr.append((bgram_words[i][0],bgram_words[i][1]))

		if kk[0][1]=='DT' and ( kk[1][1]=='NS' or kk[1][1]=='NNS'):
			#print cnt,'==>',tk,'\n','Rule4 >',kk
			rr.append((bgram_words[i][0],bgram_words[i][1]))

		i+=1
	if rr:
		print cnt,'==>',rr
		selected_bgram.append(rr)
	else:
		print cnt,'==> Empty'
	cnt+=1
'''		
counter=0
for tom in selected_bgram:
	print counter,'>> ',tom
	counter+=1
'''