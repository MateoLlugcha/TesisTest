import cv2
import easyocr

reader = easyocr.Reader(['en'])  # Puedes agregar 'es' si quieres español también
cap = cv2.VideoCapture(0)

print("Presiona ESPACIO para capturar y leer texto. Presiona ESC para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC
        break
    elif key == 32:  # ESPACIO
        print("Reconociendo texto...")
        result = reader.readtext(frame)

        print("Texto detectado:")
        for (bbox, text, prob) in result:
            print(f"{text} (confianza: {prob:.2f})")

cap.release()
cv2.destroyAllWindows()
