from playsound import playsound
morsecode= input("ingresa la palabra a convertir: ")
diccionariodecodigo={'a':'.-',
         'b':'-...',
         'c':'-.-.',
         'd':'-..',
         'e':'.',
         'f':'..-.',
         'g':'--.',
         'h':'....',
         'i':'..',
         'j':'.---',
         'k':'-.-',
         'l':'.-..',
         'm':'--',
         'n':'-.',
         'o':'---',
         'p':'.--.',
         'q':'--.-',
         'r':'.-.',
         's':'...',
         't':'-',
         'u':'..-',
         'v':'...-',
         'w':'.--',
         'x':'-..-',
         'y':'-.--',
         'z':'--..',
         '1':'.----',
         '2':'..---',
         '3':'...--',
         '4':'....-',
         '5':'.....',
         '6':'-....',
         '7':'--...',
         '8':'---..',
         '9':'----.',
         '0':'-----',
         '.':'.-.-.-',
         ',':'--..--',
         '?':'..--..',
         " ":"  "                  
      }
morse_code=' ' 
correct=True
for x in morsecode:
      	try:
      		morse_code+=diccionariodecodigo[x]
      	except:
      		print("introduce caracteres validos")
      		correct=False
      		break
print ("el codigo es:"+morse_code)
for factor in morse_code:
      if factor== ".":
            playsound('C:\\Users\\Miri\\Desktop\\Gael\\Python\\python_projects\\beep-07.wav')
#beep largo
      else:
	      playsound('C:\\Users\\Miri\\Desktop\\Gael\\Python\\python_projects\\beep-01a.wav')
#beep corto     		