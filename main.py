from watchdog.observers import Observer
import os
import time
# FileSystemEventHandler - класс по отслеживанию изменений
from watchdog.events import FileSystemEventHandler
# from tkinter import *
# from tkinter import filedialog as fd

# window = Tk()
# window.title("WatchDog by syjoosy")
# window.geometry('800x800')
# lbl = Label(window, text="Список всех фильтруемых расширений:", font=("Arial Bold", 16))
# lbl.grid(column=0, row=0)

# def extractText():
#     file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
# 												("HTML files", "*.html;*.htm"),
#                                                 ("All files", "*.*") ))
#     f = open(file_name, 'w')
#     s = text.get(1.0, END)
#     f.write(s)
#     f.close()

# def append():
# 	arr.append(txt.get())
# 	lbox.insert(END, txt.get())
# 	txt.delete(0, END)

arr = ["jpg", "png", "svg", "jpeg", "mp4", "mkv", "zip", "rar", "deb", "doc", "docx", "pdf", "odt", "txt", "py"]
# lbox = Listbox()
# for i in arr:
# 	lbox.insert(END,i)
# lbox.place(x=10, y=40)

# lbl = Label(window, text="Название:", font=("Arial Bold", 16))
# lbl.place(x=10, y=240)

# txt1 = Entry(window, width=10)
# txt1.place(x=280, y=245)

# lbl = Label(window, text="Добавить расширение:", font=("Arial Bold", 16))
# lbl.place(x=10, y=280)

# txt = Entry(window, width=10)
# txt.place(x=280, y=285)

# lbl = Label(window, text="Куда сортировать:", font=("Arial Bold", 16))
# lbl.place(x=10, y=320)

# text = Entry(window, width=10)
# text.place(x=280, y=325)

# btn = Button(window, text="Добавить", command=append)
# btn.place(x=380, y=320)

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

def read():
	# with open('settings.txt') as f:
	# 	lines = f.readlines()
	# 	 print(lines[0:-2])
	# 	print(lines[:-2])
	# определим имя файла, который читаем
	filename = "settings.txt"

	# открываем файл для чтения
	filehandle = open(filename, 'r')
	while True:
		# читаем одну строку
		line = filehandle.readline()
		if not line:
			break
		print(line[:-1])

	# закрываем указатель на этот файл
	filehandle.close()


def write():
	with open(r"settings.txt", "w") as file:
		for line in arr:
			file.write(line + '\n')



read()
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
# window.mainloop()
# Программа будет срабатывать каждые 10 милисекунд
try:
	while(True):
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()

observer.join()