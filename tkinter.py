from tkinter import FileDialog
from tkinter import *
root = Tkinter.Tk() #esto se hace solo para eliminar la ventanita de Tkinter 
root.withdraw() #ahora se cierra 
file_path = tkFileDialog.askopenfilename() #abre el explorador de archivos y guarda la seleccion en la variable!
    
    #Ahora para guardar el directorio donde se encontraba el archivo seleccionado:
match = re.search(r'/.*\..+', file_path)#matches name of file
file_position = file_path.find(match.group()) #defines position of filename in file path

save_path = file_path[0: file_position+1] #extracts the saving path.