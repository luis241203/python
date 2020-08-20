import tkinter, tkinter.filedialog, re, tkinter.messagebox
from PIL import Image
root = tkinter.Tk() 
root.withdraw() 
tkinter.messagebox.showinfo(message='Selecciona tu imagen', title='AVISO')
file_path = tkinter.filedialog.askopenfilename() 
match = re.search(r'/.*\..+', file_path)
file_position = file_path.find(match.group())
Imagen=Image.open(file_path)
new_image=Imagen.resize((132,188))
new_image.show()