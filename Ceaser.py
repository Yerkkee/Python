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
text = "cryptography"
s = 22

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + caesar(text,s))


# Function to find inverse permutations
def inversePermutation(arr, size):
 
    # Loop to select Elements one by one
    for i in range(0, size):
 
        # Loop to print position of element
        # where we find an element
        for j in range(0, size):
 
        # checking the element in increasing order
            if (arr[j] == i + 1):
 
                # print position of element where
                # element is in inverse permutation
                print(j + 1, end = " ")
                break
 
# Driver Code
arr = [6, 2, 4, 5, 7, 1, 8, 3]
arr2 = ['b', 'h', 'd', 'f', 'a', 'c', 'g', 'e']
size = len(arr)
size2 = len(arr2)

print(inversePermutation(arr2, size2))
 
#This code is contributed by Smitha Dinesh Semwal