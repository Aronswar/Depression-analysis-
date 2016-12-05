import sentiment_mod as s



us_in=input("how are feeling now? type and test")

tup1=s.sentiment(us_in)



if tup1[0]=="pos":
	tup2=("happy",tup1[1]
	print tup2
else:
	tup2=("depressed/sad", tup1[2])
	print tup2
	
	

