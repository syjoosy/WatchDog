from watchdog.observers import Observer
import os
import time
# FileSystemEventHandler - класс по отслеживанию изменений
from watchdog.events import FileSystemEventHandler
from tkinter import *
# from tkinter import filedialog as fd


window = Tk()
window.title("WatchDog by syjoosy")
window.geometry('800x800')
lbl = Label(window, text="Список всех фильтруемых расширений:", font=("Arial Bold", 16))
lbl.grid(column=0, row=0)



arr = ["jpg", "png", "svg", "jpeg", "mp4", "mkv", "zip", "rar", "deb", "doc", "docx", "pdf", "odt", "txt", "py"]

# def append():
# 	arr.append(txt.get())
# 	lbox.insert(END, txt.get())
# 	txt.delete(0, END)

def read(filename="settings.txt"):
	try:
		# filename = "settings.txt"
		filehandle = open(filename, 'r')
		i = 0
		while True:
			line = filehandle.readline()
			if not line:
				break
			i += 1

		filehandle.close()
		print("Весь файл успешно прочтен, {} расширений".format(i))
	except BaseException:
		print("Ошибка чтения файла")



# def write(filename="settings.txt"):
# 	i = 0
# 	try:
# 		with open(filename, "w") as file:
# 			for line in arr:
# 				file.write(line + '\n')
# 				i += 1
#
# 		print("Запись прошла успешно, добавлено {} расширений".format(i))
# 	except BaseException:
# 		print("Ошибка записи файла")

def new():
	try:
		result = txt1.get()
		txt.config(highlightbackground="black", highlightcolor="black")
		res = txt.get()
		# txt.delete(1.0, END)
		# lbl.configure(text=res)
		# expansion = input("Введите новое расширение: ")
		# arr.append(expansion)
		arr.append(res)
		lbox.insert(END, res)
		with open(result, "a") as myfile:
			myfile.write("\n"+res)
		txt1.config(highlightbackground="lawn green", highlightcolor="lawn green")
		txt.config(highlightbackground="lawn green", highlightcolor="lawn green")
		print("Расширение успешно добавлено")
	except BaseException:
		txt.config(highlightbackground="red", highlightcolor="red")
		print("Ошибка, массив расширений не найден")

# def newtype():
# 	# name = input("Введите название категории: ")
# 	res = txt1.get()
# 	# txt1.delete(1.0, END)
# 	myFile = open(res, "a")
# 	txt1.config(highlightbackground="lawn green", highlightcolor="lawn green")
# 	write(res)
# 	read(res)
# 	myFile.close()

def extension():
	global kolvo
	for filename in os.listdir(folder_track):
		# Проверяем расширенеи файла
		extension = filename.split(".")
	# Если это фото,
	try:
		if len(extension) > 1 and (extension[1].lower() == arr[4] or extension[1].lower() == arr[5]):
			file = folder_track + "/" + filename
			folder_dest = '/home/syjoosy/Видео/'
			new_path = folder_dest + filename
			os.rename(file, new_path)
			kolvo = kolvo + 1

	except BaseException:
		pass




lbox = Listbox()
for i in arr:
	lbox.insert(END,i)
lbox.place(x=10, y=40)

lbl = Label(window, text="Название:", font=("Arial Bold", 16))
lbl.place(x=10, y=240)

txt1 = Entry(window, width=10)
txt1.place(x=280, y=245)

# btn = Button(window, text="Добавить", command=newtype)
# btn.place(x=380, y=240)

lbl = Label(window, text="Добавить расширение:", font=("Arial Bold", 16))
lbl.place(x=10, y=280)

txt = Entry(window, width=10)
txt.place(x=280, y=285)

# txt.pack()

btn = Button(window, text="Добавить", command=new)
btn.place(x=380, y=280)

lbl = Label(window, text="Куда сортировать:", font=("Arial Bold", 16))
lbl.place(x=10, y=320)

text = Entry(window, width=10)
text.place(x=280, y=325)

btn = Button(window, text="Добавить", command=new)
btn.place(x=380, y=320)

# Создаем класс наследник, через него может отслеживать изменения в папках



kolvo = 0
class Handler(FileSystemEventHandler):
	# При любых изменениях в папке, мы перемещаем файлы в ней
	def on_modified(self, event):
		# Перебираем все файлы в папке folder_track
		global kolvo
		for filename in os.listdir(folder_track):
			# Проверяем расширенеи файла
			extension = filename.split(".")
			# Если это фото,
			if len(extension) > 1 and (extension[1].lower() == arr[0] or extension[1].lower() == arr[1] or extension[1].lower() == arr[2] or extension[1].lower() == arr[3]):
				# то перемещаем файл в папку с фото
				file = folder_track + "/" + filename
				folder_dest = '/home/syjoosy/Изображения/'
				new_path = folder_dest + filename
				os.rename(file, new_path)
				kolvo = kolvo + 1
			# Если файл видео, то в папку с видео
			# Такое же можно прописать и для других расширений файлов
			if len(extension) > 1 and (extension[1].lower() == arr[4] or extension[1].lower() == arr[5]):
				file = folder_track + "/" + filename
				folder_dest = '/home/syjoosy/Видео/'
				new_path = folder_dest + filename
				os.rename(file, new_path)
				kolvo = kolvo + 1
			if len(extension) > 1 and (extension[1].lower() == arr[6] or extension[1].lower() == arr[7]):
				file = folder_track + "/" + filename
				folder_dest = '/home/syjoosy/Загрузки'
				new_path = folder_dest + "/Zip_Rar/" + filename
				os.rename(file, new_path)
				kolvo = kolvo + 1
			if len(extension) > 1 and extension[1].lower() == arr[8]:
				file = folder_track + "/" + filename
				folder_dest = '/home/syjoosy/Загрузки'
				new_path = folder_dest + "/Deb/" + filename
				os.rename(file, new_path)
				kolvo = kolvo + 1
			if len(extension) > 1 and (extension[1].lower() == arr[9] or extension[1].lower() == arr[10] or extension[1].lower() == arr[11] or extension[1].lower() == arr[12] or extension[1].lower() == arr[13]):
				file = folder_track + "/" + filename
				folder_dest = '/home/syjoosy/Документы/'
				new_path = folder_dest + filename
				os.rename(file, new_path)
				kolvo = kolvo + 1
			elif len(extension) > 1 and extension[1].lower() == arr[14]:
				file = folder_track + "/" + filename
				folder_dest = '/home/syjoosy/Загрузки'
				new_path = folder_dest + "/PyDoc/" + filename
				os.rename(file, new_path)
				kolvo = kolvo + 1
		print("Перемещенно объектов: ", kolvo)
	# def read(self):
	# 	print("FUNCTION")
	# 	f = open('settings.txt')
	# 	print(f.read())
	# 	f.close()


# new()
# read()
# write()
# newtype()
# Папка что отслеживается
folder_track = '/home/syjoosy/Загрузки'
# Папка куда перемещать будем
folder_dest = '/home/syjoosy/Загрузки'
# Handler.read(1)
# Запуск всего на отслеживание
handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()
# print("\n")
print("Старт...")
window.mainloop()
# Программа 	будет срабатывать каждые 10 милисекунд
try:
	while(True):
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()

observer.join()