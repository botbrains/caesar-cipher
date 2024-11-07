message = input("Please enter a message: ")
shift = 5
cipher = ""
#Iterate each letter in the message
for char in message.upper():
    if char.isalpha():
      char_code = ord(char)
      new_char_code = char_code + shift
      if new_char_code > 90:
         new_char_code -= 26
      new_char = chr(new_char_code)
      cipher += new_char
    else:
      cipher = cipher + char
print("Your encrypted message is: ", cipher.lower())

