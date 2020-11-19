from watchdog.observers import Observer
import os
import time
# FileSystemEventHandler - класс по отслеживанию изменений
from watchdog.events import FileSystemEventHandler
from tkinter import *


window = Tk()
window.title("WatchDog by syjoosy")
window.geometry('800x800')


# Папка что отслеживается
folder_track = '/home/syjoosy/Загрузки'
# Папка куда перемещать будем
folder_dest = '/home/syjoosy/Загрузки'


#arr = ["jpg", "png", "svg", "jpeg", "mp4", "mkv", "zip", "rar", "deb", "doc", "docx", "pdf", "odt", "txt", "py"]
settings_line = []
arr = []

lbox1 = Listbox()
lbox = Listbox()


def new():
	try:
		result = txt1.get()
		txt.config(highlightbackground="black", highlightcolor="black")
		res = txt.get()
		arr.append(res)
		lbox.insert(END, res)
		with open(result, "a") as myfile:
			myfile.write("\n"+res)

		settings_file = open("settings.txt", 'r')
		find = 0
		for line in settings_file:
			if line == result + "\n":
				find = 1
				pass
		if find == 0:
			settings_file = open("settings.txt", 'a')
			settings_file.write(result)
			settings_line.append(result)

		lbox.delete(0, 'end')
		lbox1.delete(0, 'end')

		for i in arr:
			lbox.insert(END, i)
		lbox.place(x=10, y=40)

		for i in settings_line:
			lbox1.insert(END, i)
		lbox1.place(x=200, y=40)

		txt1.config(highlightbackground="lawn green", highlightcolor="lawn green")
		txt.config(highlightbackground="lawn green", highlightcolor="lawn green")
		print("Расширение успешно добавлено")
	except BaseException:
		txt.config(highlightbackground="red", highlightcolor="red")
		print("Ошибка, массив расширений не найден")

def remove():
	name = txt1.get()
	extension = txt.get()
	file = open(name)
	for line in file:
		if line == extension:
			pass
	file.close()

def remove_all():
	name = txt1.get()
	file = open(name, 'w')
	txt1.config(highlightbackground="lawn green", highlightcolor="lawn green")
	lbox.update()
	lbox1.update()
	file.close()


def newtype():
	res = txt1.get()
	myFile = open(res, "a")
	txt1.config(highlightbackground="lawn green", highlightcolor="lawn green")
	myFile.close()

def extension(line):
	global kolvo
	try:
		myFile = open(line, 'r')
		for line_file in myFile:
			line_file = line_file[0:-1]
			arr.append(line_file)
			print("Строка ", line_file, " добавлена")
	except BaseException:
		print("Ошибка чтения файлов расширений")

filename = "settings.txt"
filehandle = open(filename, 'r')

i = 0
kolvo = 0
lbox_restart = 123
while True:
	line = filehandle.readline()
	line = line[0:-1]
	if not line:
		break
	i += 1
	settings_line.append(line)
	extension(line)
filehandle.close()
print("Весь файл успешно прочтен, строк: {}".format(i))


for i in settings_line:
	lbox1.insert(END,i)
lbox1.place(x=200, y=40)

lbl = Label(window, text="Список всех фильтруемых расширений:", font=("Arial Bold", 16))
lbl.grid(column=0, row=0)

for i in arr:
	lbox.insert(END,i)
lbox.place(x=10, y=40)

lbl = Label(window, text="Название:", font=("Arial Bold", 16))
lbl.place(x=10, y=240)

txt1 = Entry(window, width=10)
txt1.place(x=280, y=245)

btn = Button(window, text="Удалить все расширения", command=remove_all)
btn.place(x=380, y=240)

lbl = Label(window, text="Добавить расширение:", font=("Arial Bold", 16))
lbl.place(x=10, y=280)

txt = Entry(window, width=10)
txt.place(x=280, y=285)

btn = Button(window, text="Добавить", command=new)
btn.place(x=380, y=280)

btn = Button(window, text="Удалить", command=remove)
btn.place(x=490, y=280)

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



# Папка что отслеживается
folder_track = '/home/syjoosy/Загрузки'
# Папка куда перемещать будем
folder_dest = '/home/syjoosy/Загрузки'



# Запуск всего на отслеживание
handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()
print("Старт...")
window.mainloop()

# Программа 	будет срабатывать каждые 10 милисекунд
lbox_restart = "lbox_restart"

try:
	print("Запуск try")
	while(True):
		print("Выполнилось")
		lbox1.insert(END, lbox_restart)
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()

observer.join()