def Caesar_cipher_encrypt(strr):
    x=""
    for i in range(0,len(strr)):
        if ord(strr[i])==32:
            x+=" "
        else:
            x+=chr((ord(strr[i])+3))
    return x
    
def Caesar_cipher_decrypt(strr):
    x=""
    for i in range(0,len(strr)):
        if ord(strr[i])==32:
            x+=" "
        else:
            x+=chr((ord(strr[i])-3))
    return x

def Pinpen_cipher_encrypt(strr):
    dictt={"a":chr(5287),"b":chr(8852),"c":chr(5290),"d":chr(8848),"e":chr(9633),
       "f":chr(8847),"g":chr(5283),"h":chr(8851),"i":chr(5285),
       "j":chr(5287)+"x","k":chr(8852)+"x","l":chr(5290)+"x","m":chr(8848)+"x",
       "n":chr(9633)+"x","o":chr(8847)+"x","p":chr(5283)+"x","q":chr(8851)+"x",
       "r":chr(5285)+"x",
       "s":chr(5287)+"o","t":chr(8852)+"o","u":chr(5290)+"o","v":chr(8848)+"o",
       "w":chr(9633)+"o","x":chr(8847)+"o","y":chr(5283)+"o","z":chr(8851)+"o"}
    x=""
    for i in range(0,len(strr)):
        if strr[i] in dictt and strr[i]!=" ":
            y=dictt[strr[i]]
            x+=y[0:2]
        else:
            x+=" "        
    return x

def Pinpen_cipher_decrypt(strr):
    dictt={chr(5287):"a",chr(8852):"b",chr(5290):"c",chr(8848):"d",chr(9633):"e",
       chr(8847):"f",chr(5283):"g",chr(8851):"h",chr(5285):"i",
       chr(5287)+"x":"j",chr(8852)+"x":"K",chr(5290)+"x":"l",
       chr(8848)+"x":"m",chr(9633)+"x":"n",chr(8847)+"x":"o",chr(5283)+"x":"p",chr(8851)+"x":"q",
       chr(5285)+"x":"r",
       chr(5287)+"o":"s",chr(8852)+"o":"t",chr(5290)+"o":"u",chr(8848)+"o":"v",
       chr(9633)+"o":"w",chr(8847):"x"+"o",chr(5283)+"o":"y",chr(8851)+"o":"z"}
       
    x=""
    z=""
    for i in range(0,len(strr)):
        if strr[i]==" ":
            x+=" "
        elif i!=len(strr)-1 and (strr[i+1]=="x" or strr[i+1]=="o"):
            z=strr[i]+strr[i+1]
        else:
            z=strr[i]
            
        if z in dictt:
            y=dictt[z]
            x+=y
    return x

n1=int(input("Please select your cypher type(1-Caesar cipher, 2-Pig pen): "))
n2=int(input("Enter your operation(1-encrypt, 2-decrypt): "))
if n1==2 and n2==2:
    print("""you can copy this encrypted pig pen characters
    a( ᒧ ),b( ⊔ ), c( ᒪ ), d( ⊐ ), e( □ ), f( ⊏ ), g( ᒣ ), h( ⊓ ), i( ᒥ ), j( ᒧx ), k( ⊔x ) ,l( ᒪx ), m( ⊐x ),
    n( □x ), o( ⊏x ), p( ᒣx ), q( ⊓x ), r( ᒥx ), s( ᒧo ), t( ⊔o ), u( ᒪo ), v( ⊐o ), w( □o ), x( ⊏o), y( ᒣo ),Z( ⊓o )
    """)
    str1=input("Please enter your text: ")
else:
    str1=input("Please enter your text: ")

strr=str1.lower()

if n1==1 and n2==1:
    print("Encrypted text is: ",Caesar_cipher_encrypt(strr))
elif n1==1 and n2==2:
    print("Decrypted text is: ",Caesar_cipher_decrypt(strr))
elif n1==2 and n2==1:
    print("Eecrypted text is: ",Pinpen_cipher_encrypt(strr))
elif n1==2 and n2==2:
    print("Decrypted text is: ",Pinpen_cipher_decrypt(strr))
