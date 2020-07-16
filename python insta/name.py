from textblob import TextBlob
a="whate was youre namey?"
print("original text: "+str(a))
b=TextBlob(a)
print("corrected text: "+str(b.correct()))