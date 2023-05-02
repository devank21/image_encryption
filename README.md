# image_encryption
image encryption and decryption in python using simple XOR cipher
The given Code uses simple XOR method to encrypt an image.
The user is asked to input the file path and a KEY for encrypting an image or decrypting an already encrypted image [user's choice].

For Encryption:

     1.) The image file is opened in binary and is saved as an object.
  
     2.) Using the bytearray function an array is generated from the object's bytes.
  
     3.) Each byte is then replaced with the XOR or the respective byte and the entered KEY.
  
     4.) These are then rewritten in the image file and the image is now encrypted.
      
     5.) The encrypted image file is however is not supported by my system, thats why im unable to attach the encrypted image file.
  
  
  
  
  
 For Decryption:
 
     1.) The image file is reopened and the user is asked to input the suitable KEY value required for decryption.
      
     2.) An array of the image's bytes is generated again and the are replaced with XOR of respective bytes and the KEY value.
  
     3.) The bytes are again written back in the image file and the Decrypted image is displayed on the screen using PIL library's Image module.
