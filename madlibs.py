#Program to make a simple MADLIBS game.

adjective1 = input("Enter an adjective to describe the zoo : ")
noun = input("Enter a name of an animal : ")
adjective2 = input(f"Enter an adjective to describe the {noun} : ")
verb_past1 = input(f"Enter a verb for the {noun} in continuous tense : ")
adverb = input("Enter an adverb to describe the verb : ")
adjective3 = input(f"Enter an adjective to describe the action the {noun} was doing : ")
verb_past2 = input("Enter a verb to show your actions : ")

print(f"\nToday I went to the {adjective1} zoo.")
print(f"I saw a {adjective2} {noun} jumping up and down in its tree.")
print(f"It was {verb_past1} {adverb} through the large tunnel.")
print(f"I was so {adjective3} that I {verb_past2} home.")