from imageai.Detection import ObjectDetection
import cv2

def ball_detection():
    detector = ObjectDetection()

    video = cv2.VideoCapture(0)

    # insert path to pretrained model
    path_model = ""

    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(path_model)
    detector.loadModel()

    while True:
        ret, img = video.read()
        custom = detector.CustomObjects(sports_ball=True)

        annotated_image, detection = detector.detectObjectsFromImage(custom_objects=custom,
                                                                     input_image=img,
                                                                     input_type="array",
                                                                     output_type="array",
                                                                     minimum_percentage_probability=20,
                                                                     display_object_name=True)

        text = "No ball detected"

        for eachObject in detection:
            ball_x_position = (eachObject["box_points"][0] + eachObject["box_points"][2]) // 2

            if len(detection) > 1:
                text = "Multiple balls detected"
            elif ball_x_position > 800:
                text = "Ball is on the right"
            elif ball_x_position < 600:
                text = "Ball is on the left"
            else:
                text = "Ball is in the middle"

        font = cv2.FONT_HERSHEY_DUPLEX
        pos = (50, 80)
        fontscale = 1.5
        color = (255, 255, 255)  # BGR
        thickness = 2

        text_size, _ = cv2.getTextSize(text, font, fontscale, thickness)
        text_w, text_h = text_size
        cv2.rectangle(annotated_image, (40, 35), (60 + text_w, 65 + text_h), (0, 0, 255), -1)

        annotated_image = cv2.putText(annotated_image, text, pos, font,
                                      fontscale, color, thickness, cv2.LINE_AA)


        cv2.resizeWindow("Ping Pong Detection", 800, 1400)
        cv2.imshow("Ping Pong Detection", annotated_image)

        if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1) == 27):
            break

    video.release()
    cv2.destroyAllWindows()


def main():
    ball_detection()


main()
