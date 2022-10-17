from fileinput import filename
import tkinter
from tkinter import *
from tkinter import filedialog , messagebox, font
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import cv2
import dlib
import numpy as np

window = tkinter.Tk()
lebar=500
tinggi=300
x = 500
y = 100

label1 = tkinter.Label(window, text = "APLIKASI PENGHITUNG WAJAH", font=("Futura Md BT Bold",16))
label2 = tkinter.Label(window, text = "Menggunakan Foto", font=("Arial Bold Italic",10))
label4 = tkinter.Label(window, text = "Menggunakan kamera", font=("Arial Bold Italic",10))

label1.place(x=85, y=10)
label2.place(x=150, y=65)
label4.place(x=180, y=165)

window.title("Aplikasi Penghitung Wajah")
window.resizable(0,0)
window.minsize(lebar,tinggi)
window.maxsize(lebar,tinggi)
screenwidh = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

newx = int((screenwidh/2) - (lebar/2))
newy = int((screenheight/2) - (tinggi/2)-50)

window.geometry(f"{lebar}x{tinggi}+{newx}+{newy}")

def camera():
	# connect kamera webcam
	webcam = cv2.VideoCapture(0)

	# Deteksi koordinat wajah
	detector = dlib.get_frontal_face_detector()

	# Capture frames continuously
	while True:

		# Capture frame-by-frame
		ret, frame = webcam.read()
		frame = cv2.flip(frame, 1)

		# RGB to grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = detector(gray)

		# untuk menghitung wajah
		i = 0
		for face in faces:

			# mendapatkan koordinat wajah
			x, y = face.left(), face.top()
			x1, y1 = face.right(), face.bottom()
			cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

			# Increment iterator for each face in faces
			i = i+1

			# menampilkan kotak dan jumlah wajah
			cv2.putText(frame, 'wajah ke'+str(i), (x-10, y-10),
						cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			print(face, i)
			
		cv2.imshow('output', frame)
		
		# perintah untuk keluar dari aplikasi
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
	# Release the capture and destroy the windows
	webcam.release()
	cv2.destroyAllWindows()

#fungsi upload gambar dan proses gambar
def gambar():
    #pilih image
    path = tkinter.filedialog.askopenfilename()
    # membaca image
    img = cv2.imread(path)
    # load cascade file
    face_cascade = cv2.CascadeClassifier("cascadefile/haarcascade_frontalface_default.xml")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # deteksi wajah
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    print (type(faces))

    if len(faces) == 0:
        print ("No faces found")

    else:
        print (faces)
        print (faces.shape)
        print ("Jumlah Wajah terdeteksi: " + str(faces.shape[0]))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # menampilkan jumlah wajah
        cv2.rectangle(img, ((0,img.shape[0] -25)),(270, img.shape[0]), (255,255,255), -1)
        cv2.putText(img, "Jumlah wajah Terdeteksi: " + str(faces.shape[0]), (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)

        # menampilkan output
        cv2.imshow("Output", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows

def about():
    messagebox.showinfo(title="about",message = str("Aplikasi ini menggunakan bahasa pemrograman python. Aplikasi ini menggunakan metode haascade untuk mengenali dan mendeteksi wajah menggunakan webcam atau Foto. Aplikasi ini menggunakan library opencv, dlib sebagai library untuk mendeteksi wajah,tkinter sebagai gui, dan PIL untuk menampilkan image di aplikasi window. sumber : stackoverflow, youtube, website, github"))

tombol1 = tkinter.Button(window, text ="Buka Kamera", command=camera)
tombol2 = tkinter.Button(window, text ="Pilih Foto", command=gambar)
tombol3 = tkinter.Button(window, text ="About", command=about)

tombol1.place(x=220, y=205, width=100, height=50)
tombol2.place(x=180, y=95, width=100, height=50)
tombol3.place(x=20, y=255, width=50, height=25)

window.mainloop()