# Yerkebulan Zhaiylkan
# This is an application to decrypt text in Caesar encryption.

def caesar(plainText, shift): 
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  print ("Your ciphertext is: ", cipherText)
  return cipherText
#check the above function

text = "cryptography" #Encrypted text
s = 22 #Key of Plain Text

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + caesar(text,s))

 