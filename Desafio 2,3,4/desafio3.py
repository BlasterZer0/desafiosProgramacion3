import rsa
 
publicKey, privateKey = rsa.newkeys(512)

message = input("Ingresar mensaje\n")
 
encMessage = rsa.encrypt(message.encode(), publicKey)
 
print("Mensaje original: ", message)
print("Mensaje encriptado: ", encMessage)
 
decMessage = rsa.decrypt(encMessage, privateKey).decode()
 
print("Mensaje desencriptado: ", decMessage)