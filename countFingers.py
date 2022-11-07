import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

hands = mp.solutions.hands
Hands = hands.Hands(max_num_hands=2)
mpDwaw = mp.solutions.drawing_utils

while True:
    success, img = video.read()
    frameRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(frameRGB)
    handPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []
    if handPoints:
        for points in handPoints:
            mpDwaw.draw_landmarks(img, points, hands.HAND_CONNECTIONS)
            # podemos enumerar esses pontos da seguinte forma
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                cv2.putText(img, str(id), (cx, cy + 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 0, 100), 2)
                pontos.append((cx, cy))

            dedos = [8, 12, 16, 20]
            dedos2 = [29, 33, 37, 41]
            dedos3 = [50, 54, 58, 62]
            dedos4 = [71, 75, 79, 83]
            
            contador = 0
            contador2 = 0
            contador3 = 0
            contador4 = 0
            if pontos:
                # fazendo verificação se a mão esta para cima
                if pontos[0][1] > pontos[5][1] and pontos[0][1] > pontos[9][1] and pontos[0][1] > pontos[13][1] and pontos[0][1] > pontos[17][1]:
                    if pontos[4][0] > pontos[17][0]:
                        if pontos[5][0] < pontos[4][0]:
                            contador += 1
                    else:
                        if pontos[4][0] < pontos[2][0] or pontos[4][0] < pontos[3][0]:
                            contador += 1

                    for x in dedos:
                        if pontos[x][1] < pontos[x-2][1]:
                            contador += 1
                # verificação se a mão esta para baixo
                elif pontos[0][1] < pontos[5][1] and pontos[0][1] < pontos[9][1] and pontos[0][1] < pontos[13][1] and pontos[0][1] < pontos[17][1]:
                    if pontos[4][0] > pontos[17][0]:
                        if pontos[5][0] < pontos[4][0]:
                            contador += 1
                    else:
                        if pontos[4][0] < pontos[2][0] or pontos[4][0] < pontos[3][0]:
                            contador += 1

                    for x in dedos:
                        if pontos[x][1] > pontos[x-2][1]:
                            contador += 1

                # verificação para o lado direito
                elif pontos[0][0] < pontos[5][0] and pontos[0][0] < pontos[9][0] and pontos[0][0] < pontos[13][0] and pontos[0][0] < pontos[17][0]:
                    if pontos[4][1] > pontos[17][1]:
                        if pontos[5][1] < pontos[4][1]:
                            contador += 1
                    else:
                        if pontos[4][1] < pontos[2][1] or pontos[4][1] < pontos[3][1]:
                            contador += 1

                    for x in dedos:
                        if pontos[x][0] > pontos[x-2][0]:
                            contador += 1
                  # verificação para o lado esquerdo
                elif pontos[0][0] > pontos[5][0] and pontos[0][0] > pontos[9][0] and pontos[0][0] > pontos[13][0] and pontos[0][0] > pontos[17][0]:
                    if pontos[4][1] > pontos[17][1]:
                        if pontos[5][1] < pontos[4][1]:
                            contador += 1
                    else:
                        if pontos[4][1] < pontos[2][1] or pontos[4][1] < pontos[3][1]:
                            contador += 1

                    for x in dedos:
                        if pontos[x][0] < pontos[x-2][0]:
                            contador += 1
                if len(pontos) > 21:
                    count = 2
                    if pontos[1 * count][1] > pontos[5 * count][1] and pontos[1 * count][1] > pontos[9 * count][1] and pontos[1 * count][1] > pontos[13 * count][1] and pontos[1 * count][1] > pontos[17 * count][1]:
                        if pontos[4 * count][0] > pontos[17 * count][0]:
                            if pontos[5 * count][0] < pontos[4 * count][0]:
                                contador2 += 1
                        else:
                            if pontos[4 * count][0] < pontos[2 * count][0] or pontos[4 * count][0] < pontos[3 * count][0]:
                                contador2 += 1

                        for x in dedos2:
                            if pontos[x][1] < pontos[x-2][1]:
                                contador2 += 1
                    # verificação se a mão esta para baixo
                    elif pontos[1 * count][1] < pontos[5 * count][1] and pontos[1 * count][1] < pontos[9 * count][1] and pontos[1 * count][1] < pontos[13 * count][1] and pontos[1 * count][1] < pontos[17 * count][1]:
                        if pontos[4 * count][0] > pontos[17 * count][0]:
                            if pontos[5 * count][0] < pontos[4 * count][0]:
                                contador2 += 1
                        else:
                            if pontos[4 * count][0] < pontos[2 * count][0] or pontos[4 * count][0] < pontos[3 * count][0]:
                                contador2 += 1

                        for x in dedos2:
                            if pontos[x][1] > pontos[x-2][1]:
                                contador2 += 1

                    # verificação para o lado direito
                    elif pontos[1 * count][0] < pontos[5 * count][0] and pontos[1 * count][0] < pontos[9 * count][0] and pontos[1 * count][0] < pontos[13 * count][0] and pontos[1 * count][0] < pontos[17 * count][0]:
                        if pontos[4 * count][1] > pontos[17 * count][1]:
                            if pontos[5 * count][1] < pontos[4 * count][1]:
                                contador2 += 1
                        else:
                            if pontos[4 * count][1] < pontos[2 * count][1] or pontos[4 * count][1] < pontos[3 * count][1]:
                                contador2 += 1

                        for x in dedos2:
                            if pontos[x][0] > pontos[x-2][0]:
                                contador2 += 1
                      # verificação para o lado esquerdo
                    elif pontos[1 * count][0] > pontos[5 * count][0] and pontos[1 * count][0] > pontos[9 * count][0] and pontos[1 * count][0] > pontos[13 * count][0] and pontos[1 * count][0] > pontos[17][0]:
                        if pontos[4 * count][1] > pontos[17 * count][1]:
                            if pontos[5 * count][1] < pontos[4 * count][1]:
                                contador2 += 1
                        else:
                            if pontos[4 * count][1] < pontos[2 * count][1] or pontos[4 * count][1] < pontos[3 * count][1]:
                                contador2 += 1

                        for x in dedos2:
                            if pontos[x][0] < pontos[x-2][0]:
                                contador2 += 1
                if len(pontos) > 42:
                    count = 3
                    if pontos[1 * count][1] > pontos[5 * count][1] and pontos[1 * count][1] > pontos[9 * count][1] and pontos[1 * count][1] > pontos[13 * count][1] and pontos[1 * count][1] > pontos[17 * count][1]:
                        if pontos[4 * count][0] > pontos[17 * count][0]:
                            if pontos[5 * count][0] < pontos[4 * count][0]:
                                contador3 += 1
                        else:
                            if pontos[4 * count][0] < pontos[2 * count][0] or pontos[4 * count][0] < pontos[3 * count][0]:
                                contador3 += 1

                        for x in dedos3:
                            if pontos[x][1] < pontos[x-2][1]:
                                contador3 += 1
                    # verificação se a mão esta para baixo
                    elif pontos[1 * count][1] < pontos[5 * count][1] and pontos[1 * count][1] < pontos[9 * count][1] and pontos[1 * count][1] < pontos[13 * count][1] and pontos[1 * count][1] < pontos[17 * count][1]:
                        if pontos[4 * count][0] > pontos[17 * count][0]:
                            if pontos[5 * count][0] < pontos[4 * count][0]:
                                contador3 += 1
                        else:
                            if pontos[4 * count][0] < pontos[2 * count][0] or pontos[4 * count][0] < pontos[3 * count][0]:
                                contador3 += 1

                        for x in dedos3:
                            if pontos[x][1] > pontos[x-2][1]:
                                contador3 += 1

                    # verificação para o lado direito
                    elif pontos[1 * count][0] < pontos[5 * count][0] and pontos[1 * count][0] < pontos[9 * count][0] and pontos[1 * count][0] < pontos[13 * count][0] and pontos[1 * count][0] < pontos[17 * count][0]:
                        if pontos[4 * count][1] > pontos[17 * count][1]:
                            if pontos[5 * count][1] < pontos[4 * count][1]:
                                contador3 += 1
                        else:
                            if pontos[4 * count][1] < pontos[2 * count][1] or pontos[4 * count][1] < pontos[3 * count][1]:
                                contador3 += 1

                        for x in dedos3:
                            if pontos[x][0] > pontos[x-2][0]:
                                contador3 += 1
                      # verificação para o lado esquerdo
                    elif pontos[1 * count][0] > pontos[5 * count][0] and pontos[1 * count][0] > pontos[9 * count][0] and pontos[1 * count][0] > pontos[13 * count][0] and pontos[1 * count][0] > pontos[17][0]:
                        if pontos[4 * count][1] > pontos[17 * count][1]:
                            if pontos[5 * count][1] < pontos[4 * count][1]:
                                contador3 += 1
                        else:
                            if pontos[4 * count][1] < pontos[2 * count][1] or pontos[4 * count][1] < pontos[3 * count][1]:
                                contador3 += 1

                        for x in dedos3:
                            if pontos[x][0] < pontos[x-2][0]:
                                contador3 += 1
                if len(pontos) > 63:
                    count = 4
                    if pontos[1 * count][1] > pontos[5 * count][1] and pontos[1 * count][1] > pontos[9 * count][1] and pontos[1 * count][1] > pontos[13 * count][1] and pontos[1 * count][1] > pontos[17 * count][1]:
                        if pontos[4 * count][0] > pontos[17 * count][0]:
                            if pontos[5 * count][0] < pontos[4 * count][0]:
                                contador4 += 1
                        else:
                            if pontos[4 * count][0] < pontos[2 * count][0] or pontos[4 * count][0] < pontos[3 * count][0]:
                                contador4 += 1

                        for x in dedos4:
                            if pontos[x][1] < pontos[x-2][1]:
                                contador4 += 1
                    # verificação se a mão esta para baixo
                    elif pontos[1 * count][1] < pontos[5 * count][1] and pontos[1 * count][1] < pontos[9 * count][1] and pontos[1 * count][1] < pontos[13 * count][1] and pontos[1 * count][1] < pontos[17 * count][1]:
                        if pontos[4 * count][0] > pontos[17 * count][0]:
                            if pontos[5 * count][0] < pontos[4 * count][0]:
                                contador4 += 1
                        else:
                            if pontos[4 * count][0] < pontos[2 * count][0] or pontos[4 * count][0] < pontos[3 * count][0]:
                                contador4 += 1

                        for x in dedos4:
                            if pontos[x][1] > pontos[x-2][1]:
                                contador4 += 1

                    # verificação para o lado direito
                    elif pontos[1 * count][0] < pontos[5 * count][0] and pontos[1 * count][0] < pontos[9 * count][0] and pontos[1 * count][0] < pontos[13 * count][0] and pontos[1 * count][0] < pontos[17 * count][0]:
                        if pontos[4 * count][1] > pontos[17 * count][1]:
                            if pontos[5 * count][1] < pontos[4 * count][1]:
                                contador4 += 1
                        else:
                            if pontos[4 * count][1] < pontos[2 * count][1] or pontos[4 * count][1] < pontos[3 * count][1]:
                                contador4 += 1

                        for x in dedos4:
                            if pontos[x][0] > pontos[x-2][0]:
                                contador4 += 1
                      # verificação para o lado esquerdo
                    elif pontos[1 * count][0] > pontos[5 * count][0] and pontos[1 * count][0] > pontos[9 * count][0] and pontos[1 * count][0] > pontos[13 * count][0] and pontos[1 * count][0] > pontos[17][0]:
                        if pontos[4 * count][1] > pontos[17 * count][1]:
                            if pontos[5 * count][1] < pontos[4 * count][1]:
                                contador4 += 1
                        else:
                            if pontos[4 * count][1] < pontos[2 * count][1] or pontos[4 * count][1] < pontos[3 * count][1]:
                                contador4 += 1

                    for x in dedos4:
                        if pontos[x][0] < pontos[x-2][0]:
                            contador4 += 1                
            # mostrar o quadrado
            cv2.rectangle(img, (80, 10), (570, 110), (255, 0, 255), 1)
            cv2.rectangle(img, (80, 10), (570, 110), (255, 0, 255), 1)
            # mostrar o contador
            cv2.putText(img, str(contador), (100, 100),cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)
            cv2.putText(img, str(contador2), (220, 100),cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)
            cv2.putText(img, str(contador3), (340,  100),cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)
            cv2.putText(img, str(contador4), (460, 100),cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5)
            

    cv2.imshow('Imagem', img)
    cv2.imshow('Imagem', alo)
    cv2.waitKey(1)
