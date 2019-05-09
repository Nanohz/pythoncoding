# Will encypt a passcode inputed by user 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ''
#character = input('Please enter a character: ')
message = input( 'Please enter a message: ')

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
  #print(position)
  
  newPosition = (position + key) % 27
  #print(newPosition)
  
  newCharacter = alphabet[newPosition]
  #print('This is now the new character :'+ newCharacter)
  newMessage += newCharacter 
  print('You new message is :' + newMessage)
  