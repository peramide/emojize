import emoji

#Ask for word(s) to convert to emoji.
#Strip of white spaces
word_to_emojize = input("").strip()

#Concatenate the word(s) to emojize before and after with : 
emoji_synthax = ":" + word_to_emojize + ":"

#Print Emoji
print(emoji.emojize(emoji_synthax))
