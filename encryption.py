from PIL import Image

def encrypt(path):
        key = int(input('Enter Key for encryption of Image : '))
        print('The path of file : ', path)
        print('Key for encryption : ', key)

        fin = open(path, 'rb')
        image = fin.read()
        fin.close()

        image = bytearray(image)
        for index, values in enumerate(image):
                image[index] = values ^ key

        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Encryption Completed Successfully')
        

def decrypt(path):
        try:
                key = int(input('Enter Key for dencryption of Image : '))
                print('The path of file : ', path)
                print('Key for Decryption : ', key)

                fin = open(path, 'rb')
                image = fin.read()
                fin.close()
                
                image = bytearray(image)
                for index, values in enumerate(image):
                	image[index] = values ^ key
                fin = open(path, 'wb')
                fin.write(image)
                fin.close()
                display = Image.open(path)
                display.show()
                print('Decryption Done...')

        except Exception:
                print('Error caught : ', Exception.__name__)

#______Main_______

p=input("Enter the image location:")

n=int(input("Press 1 for encryption and 2 for decryption:"))
if(n==1):
        encrypt(p)
elif(n==2):
        decrypt(p)
else:
        print("Invalid Choice")

