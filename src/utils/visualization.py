import cv2

def draw_defects(original_img, contours):
    result = original_img.copy()
    for cnt in contours:
        if cv2.contourArea(cnt) > 30:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(result, (x,y), (x+w, y+h), (0,255,0), 1)
    return result
