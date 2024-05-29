# USAGE
# python classify.py --model pokedex.model --labelbin lb.pickle --image examples/00000012.jpg

# import the necessary packages
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

# construct the argument parse and parse the arguments
'''ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-l", "--labelbin", required=True,
	help="path to label binarizer")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())'''


# load the image
def detect_emotio(score):
    camera = cv2.VideoCapture(0)
    import surprise
    import sad
    import happy
    import angry
    import fear
    import neutral
    import surprise
    while (True):

        i = 0
        while (True):
            ret, frame = camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite(str(i) + '.png', frame)
                path = str(i) + '.png'
                image = cv2.imread(path)
                # image = cv2.imread(path)

                output = image.copy()

                # pre-process the image for classification
                image = cv2.resize(image, (96, 96))
                image = image.astype("float") / 255.0
                image = img_to_array(image)
                image = np.expand_dims(image, axis=0)

                # load the trained convolutional neural network and the label
                # binarizer
                print("[INFO] loading network...")
                model = load_model("pokedex.model")
                lb = pickle.loads(open("lb.pickle", "rb").read())

                # classify the input image
                print("[INFO] classifying image...")
                proba = model.predict(image)[0]
                idx = np.argmax(proba)
                emo_index = idx + 1
                print(emo_index)
                label = lb.classes_[idx]
                proceed = label

                # we'll mark our prediction as "correct" of the input image filename
                # contains the predicted label text (obviously this makes the
                # assumption that you have named your testing image files this way)
                filename = path[path.rfind(os.path.sep) + 1:]
                correct = "correct" if filename.rfind(label) != -1 else ""

                # build the label and draw the label on the image
                label = "{}: {:.2f}% ({})".format(label, proba[idx] * 100, correct)
                output = imutils.resize(output, width=400)
                cv2.putText(output, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0, 255, 0), 2)
                print("[INFO] {}".format(label))
                cv2.imshow("Output", output)
                cv2.waitKey(1)
                import matplotlib.pyplot as plt
                x = [0, score]
                y = [emo_index, 0]
                plt.plot(x, y)
                plt.xlabel('Score')
                plt.ylabel('Emotion')
                plt.title('Emotion Vs Score Graph')
                plt.show()
                if proceed == "sad":
                    sad.sad()
                elif proceed == "happy":
                    happy.happy()
                elif proceed == "angry":
                    angry.angry()
                elif proceed == "fear":
                    fear.fear()
                elif proceed == "neutral":
                    neutral.neutral()
                else:
                    surprise.surprise()
                break
        # path= "C:/Users/Dell/Desktop/cnn-keras/examples/00000002.jpg"

        # return_value, frame = camera.read()
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        # cv2.imshow('frame',gray)

        # cv2.imwrite(str(i)+'.png', frame)

        camera.release()
        cv2.destroyAllWindows()
