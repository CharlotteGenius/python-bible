`# pig latin is a word game
# get sentence from user

original = input("Please enter a sentence:").strip().lower()

# split the sentence into words

words = original.split()

# loop thru words and convert to pig latin

new_words = []


# if starts with vowel, just add "yay"
# otherwise, move the first consonant cluser to end, and add "ay"

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"

    else:
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else:
                break
        consonant = word[:vowel_position]       # all the consonants,
                                                # from the first letter
                                                # to the one before vowel
        the_rest = word[vowel_position:]        # the rest is from the vowel
        new_word = the_rest + consonant + "ay"  # stick words back together
                                                # move the consonants to the end
                                                # string can be added using "+"
            
    new_words.append(new_word)

# output the final string

output = " ".join(new_words)
print(output)
