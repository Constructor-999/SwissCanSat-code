from serial import Serial
from PIL import Image
from time import sleep

ser = Serial("COM6", 2000000)

imgData = []

while True:
    data = ser.readline().decode()
    print(data)
    if(data == "IMG\r\n"):
        while True:
            res = ser.readline().decode()
            print(res)
            if (res == "endIMG\r\n"):
                resultImg = Image.new("RGB", (640, 360))
                resultImg.putdata(imgData)
                resultImg.save("./test.png")
                print("finished")
                imgData = []
                break
            res = str(res)
            res = res.replace("i", "")
            res = res.replace("m", "")
            res = res.replace("g", "")
            res = res.replace("\r\n", "")
            if ("\r" in res):
                resArr = res.split("\r")
                for r in range(len(resArr)):
                    resArr = resArr[r].replace("\r", "")
                    res = int(resArr)
                    resTuple = tuple(res.to_bytes(3, byteorder='big'))
                    imgData.append(resTuple)
            else:
                res = int(res)
                resTuple = tuple(res.to_bytes(3, byteorder='big'))
                imgData.append(resTuple)