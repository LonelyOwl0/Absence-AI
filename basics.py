import cv2
import numpy as np
import face_recognition



# Importation des images et pretraitement :
imgandrew1 = face_recognition.load_image_file('ImagesAttendance/andrewtate.jpg')
imgandrew1 = cv2.cvtColor(imgandrew1, cv2.COLOR_BGR2RGB)
imgandrew2 = face_recognition.load_image_file('ImagesAttendance/fouad mohammed.jpeg')
imgandrew2 = cv2.cvtColor(imgandrew2, cv2.COLOR_BGR2RGB)

# faceloc contient les dimensions du carré qui contient le visage détécté :
faceLoc = face_recognition.face_locations(imgandrew1)[0]
# l"encodage du visage est utilisé pour comparer avec d'autre encodage d'autres visages :
encodeandrew1 = face_recognition.face_encodings(imgandrew1)[0]
#dessiner un rectange sur le visage de l'image cible :
cv2.rectangle(imgandrew1,(faceLoc[3],faceLoc[0]),(faceLoc[1], faceLoc[2]), (255,0, 255), 2)

#La meme chose pour la 2ème image :
faceLoc = face_recognition.face_locations(imgandrew2)[0]
encodeandrew2 = face_recognition.face_encodings(imgandrew2)[0]
cv2.rectangle(imgandrew2,(faceLoc[3],faceLoc[0]),(faceLoc[1], faceLoc[2]), (255,0, 255), 2)

results = face_recognition.compare_faces([encodeandrew1],encodeandrew2)
facedistance = face_recognition.face_distance([encodeandrew1],encodeandrew2)

cv2.putText(imgandrew2,f'{results} {round(facedistance[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

print(results)
print(facedistance)
#Affichage des images avec detection de visage :
cv2.imshow('Andrew 1', imgandrew1)
cv2.imshow('Andrew 2', imgandrew2)


cv2.waitKey(0)