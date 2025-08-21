import cv2
import numpy as np

# --- Configuración del color a seguir (en espacio HSV) ---
# Puedes cambiar estos valores para rastrear otro color.
# Ejemplo: Para seguir un objeto azul, ajusta los valores de abajo.
LOWER_COLOR = np.array([100, 150, 70])   # Mínimo (HSV)
UPPER_COLOR = np.array([140, 255, 255]) # Máximo (HSV)

# --- Inicializa la cámara ---
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo acceder a la cámara.")
    exit()

print("Presiona 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo leer el frame.")
        break

    # Convertir imagen de BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crear una máscara para el color seleccionado
    mask = cv2.inRange(hsv, LOWER_COLOR, UPPER_COLOR)

    # Procesar la máscara para reducir ruido
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Encontrar contornos del objeto
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    center = None

    if contours:
        # Selecciona el contorno más grande
        largest_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest_contour) > 400:  # Ignora objetos muy pequeños
            # Encuentra el círculo mínimo que rodea el contorno
            ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)
            M = cv2.moments(largest_contour)
            if M["m00"] != 0:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                # Dibuja un círculo y el centro en el objeto
                cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,0), 2)
                cv2.circle(frame, center, 5, (0,0,255), -1)
                cv2.putText(frame, f"Pos: {center}", (center[0]+10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    # Mostrar resultados
    cv2.imshow('Color Tracking', frame)
    cv2.imshow('Mask', mask)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- Libera recursos ---
cap.release()
cv2.destroyAllWindows()
