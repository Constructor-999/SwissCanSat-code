import cv2
from serial import Serial
from PIL import Image

ser = Serial("/dev/ttyS0", 2000000, timeout=0.0001)
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
frame = cv2.resize(frame, (640, 360))
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
frame = Image.fromarray(frame)

ser.write("IMG".encode())
for i in range(len(frame.getdata())):
        tupleColors = frame.getdata()[i]
        res = int.from_bytes(tupleColors, byteorder ='big')
        ser.write(f"img{res}".encode())
        ser.close()
        ser.open()
ser.write("endIMG".encode())

