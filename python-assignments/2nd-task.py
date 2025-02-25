user_input = input("Enter your sentence:") 
Break_words =user_input.split()
Count_Words =len(Break_words)
print(f"{user_input}\n Words in Sentence are : {Count_Words}") 

#Bouns Challenge

words = user_input.split()
reverse_text = words.reverse()
reverse_text = ' '.join(words)
print(f"Reverse Text Is : {reverse_text}","\n")