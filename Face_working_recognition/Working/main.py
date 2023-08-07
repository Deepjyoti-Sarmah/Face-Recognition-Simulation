import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import numpy as np

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# from firebase_admin import storage
import os
from twilio.rest import Client


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-june-2023-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recognition-june-2023.appspot.com"
})


# account_sid = os.environ["ACCOUNT_SID"]
# auth_token = os.environ["AUTH_TOKEN"]

account_sid = "AC61072ea617705dad0a5cb2eb94a6fb65"
auth_token = "72d332a1d4cffe0ca834a8b5cd849463"


client = Client(account_sid, auth_token)


# bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Load the encoding file
print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(
                encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(
                encodeListKnown, encodeFace)
            # print("matches", matches)
            # print("faceDis", faceDis)

            matchIndex = np.argmin(faceDis)
            # print("Match Index", matchIndex)

            if matches[matchIndex]:
                print("Known Face Detected")
                print(studentIds[matchIndex])

                id = studentIds[matchIndex]

                if counter == 0:
                    #                 cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    #                 cv2.imshow("Face Attendance", imgBackground)
                    #                 cv2.waitKey(1)
                    counter = 1

            if counter != 0:

                if counter == 1:

                    studentInfo = db.reference(f'Students/{id}').get()

                    # name = studentInfo['name']
                    #             # Get the Data
                    # print(studentInfo)
                    try:
                        if studentInfo is not None:
                            print(studentInfo)
                        else:
                            print(f"No data found for student with ID {id}")
                    except Exception as e:
                        print(f"Error accessing the database: {str(e)}")

                #             # Get the Image from the storage
                #             blob = bucket.get_blob(f'Images/{id}.png')
                #             array = np.frombuffer(blob.download_as_string(), np.uint8)
                #             imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
                #             # Update data of attendance
                #             datetimeObject = datetime.strptime(studentInfo['last_attendance_time'], "%Y-%m-%d %H:%M:%S")
                #             secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                #             print(secondsElapsed)
                #             if secondsElapsed > 30:
                        ref = db.reference(f'Students/{id}')
                        studentInfo['detection_no'] += 1
                        try:
                            ref.child('detection_no').set(
                                studentInfo['detection_no'])
                            print("Update successful")
                        except Exception as e:
                            print("Update failed:", str(e))

        #                 ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                # else:

                #     counter = 0

        #             if 10 < counter < 20:

        #             if counter <= 10:

                counter += 1

                if counter >= 20:

                    #     # name = studentInfo['name']

                    message = client.messages.create(
                        body="A face has been detected! The name of the person detected is {} and their ID is {}".format(
                            *studentInfo.values()),
                        from_='+15419858704',
                        to='+916003349334'
                    )

                    print(message.status)

                # counter = 0
                # studentInfo = []
                # imgStudent = []

    else:
        counter = 0
    cv2.imshow("Webcam", img)
    # cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
