import cv2
import time

#image =cv2.imread("../images/pessoas.jpg")
#image =cv2.imread("../images/pessoas_2.jpeg")
#image =cv2.imread("../images/pessoa_3.jpg")
image =cv2.imread("../images/caneca2.jpg")
classificador = cv2.CascadeClassifier("../haar/cascade-caneca3-1800-1200.xml")
imagemCinza = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detectMultiScale(imagemCinza,scaleFactor=1.25,minNeighbors=5)
print(deteccoes)
print(len(deteccoes))

cv2.imshow("Imagens",image)
for (x,y,l,a) in deteccoes:
    cv2.rectangle(image,(x,y),(l+x,a+y),(0,255,0),2)
    cv2.imshow("Imagens",image)
    cv2.waitKey(500)
    

cv2.waitKey(0)
cv2.destroyAllWindows()