#importing cv2 - step 1
import cv2

#read the image using cv2 in img variable (stored in img) - step 2
img = cv2.imread("solar-system.jpg")

#Adding texts to sun and the planets - step 5
cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (120,180),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (185,175),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (280,175),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Moon",
            (320,155),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (380,165),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (580,62),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (770,145),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255)
            ) 

cv2.putText(img,
            "Uranus",
            (960,145),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1110,145),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )  

#diaplay the image - step 3
cv2.imshow("output",img)

#infinite display - step 4
cv2.waitKey(0)

