import cv2
import os
from flask import Flask, request, render_template
from datetime import date, datetime
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import joblib

# ---------------- FLASK APP ----------------
app = Flask(__name__)

# ---------------- CONFIG ----------------
nimgs = 10
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")

# ---------------- FACE DETECTOR ----------------
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# ---------------- FOLDERS SETUP ----------------
os.makedirs('Attendance', exist_ok=True)
os.makedirs('static/faces', exist_ok=True)

attendance_file = f'Attendance/Attendance-{datetoday}.csv'

if not os.path.exists(attendance_file):
    with open(attendance_file, 'w') as f:
        f.write('Name,Roll,Time\n')

# ---------------- UTILITIES ----------------

def total_registered_users():
    return len(os.listdir('static/faces'))


def extract_faces(img):
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.2, 5, minSize=(20, 20))
        return faces
    except:
        return []


def identify_face(face_array):
    if not os.path.exists('static/face_recognition_model.pkl'):
        return ["Unknown"]
    model = joblib.load('static/face_recognition_model.pkl')
    return model.predict(face_array)


def train_model():
    faces = []
    labels = []

    user_list = os.listdir('static/faces')

    for user in user_list:
        user_path = f'static/faces/{user}'
        for img_name in os.listdir(user_path):
            img = cv2.imread(f'{user_path}/{img_name}')
            resized = cv2.resize(img, (50, 50))
            faces.append(resized.ravel())
            labels.append(user)

    faces = np.array(faces)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(faces, labels)

    joblib.dump(model, 'static/face_recognition_model.pkl')


def extract_attendance():
    df = pd.read_csv(attendance_file)
    return df['Name'], df['Roll'], df['Time'], len(df)


def add_attendance(name):
    username, userid = name.split('_')
    current_time = datetime.now().strftime("%H:%M:%S")

    df = pd.read_csv(attendance_file)

    if df.empty or int(userid) not in df['Roll'].values:
        with open(attendance_file, 'a') as f:
            f.write(f'\n{username},{userid},{current_time}')


def get_all_users():
    user_list = os.listdir('static/faces')

    names = []
    rolls = []

    for user in user_list:
        name, roll = user.split('_')
        names.append(name)
        rolls.append(roll)

    return user_list, names, rolls, len(user_list)


def delete_user_folder(path):
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))
    os.rmdir(path)

# ---------------- ROUTES ----------------

@app.route('/')
def home():
    names, rolls, times, l = extract_attendance()
    return render_template(
        'home.html',
        names=names,
        rolls=rolls,
        times=times,
        l=l,
        totalreg=total_registered_users(),
        datetoday2=datetoday2
    )


@app.route('/listusers')
def listusers():
    userlist, names, rolls, l = get_all_users()
    return render_template(
        'listusers.html',
        userlist=userlist,
        names=names,
        rolls=rolls,
        l=l,
        totalreg=total_registered_users(),
        datetoday2=datetoday2
    )


@app.route('/deleteuser')
def deleteuser():
    user = request.args.get('user')
    delete_user_folder(f'static/faces/{user}')

    if len(os.listdir('static/faces')) == 0:
        if os.path.exists('static/face_recognition_model.pkl'):
            os.remove('static/face_recognition_model.pkl')

    try:
        train_model()
    except:
        pass

    return listusers()


# ---------------- START ATTENDANCE ----------------

@app.route('/start')
def start():
    names, rolls, times, l = extract_attendance()

    if not os.path.exists('static/face_recognition_model.pkl'):
        return render_template(
            'home.html',
            names=names,
            rolls=rolls,
            times=times,
            l=l,
            totalreg=total_registered_users(),
            datetoday2=datetoday2,
            mess="Model not trained. Add users first."
        )

    cap = cv2.VideoCapture(0)

    try:
        while True:
            ret, frame = cap.read()

            faces = extract_faces(frame)

            for (x, y, w, h) in faces:
                face = frame[y:y+h, x:x+w]
                face_resized = cv2.resize(face, (50, 50))

                prediction = identify_face(face_resized.reshape(1, -1))[0]

                add_attendance(prediction)

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, prediction, (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            cv2.imshow("Attendance System", frame)

            if cv2.waitKey(1) == 27:  # ESC key
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

    return home()


# ---------------- ADD NEW USER ----------------

@app.route('/add', methods=['POST'])
def add():
    username = request.form['newusername']
    userid = request.form['newuserid']

    folder = f'static/faces/{username}_{userid}'
    os.makedirs(folder, exist_ok=True)

    cap = cv2.VideoCapture(0)

    i = 0
    j = 0

    try:
        while True:
            ret, frame = cap.read()

            faces = extract_faces(frame)

            for (x, y, w, h) in faces:
                if j % 5 == 0 and i < nimgs:
                    face_img = frame[y:y+h, x:x+w]
                    cv2.imwrite(f'{folder}/{username}_{i}.jpg', face_img)
                    i += 1

                j += 1

                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.imshow("Register User", frame)

            if i >= nimgs:
                break

            if cv2.waitKey(1) == 27:
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

    train_model()

    return home()


# ---------------- RUN APP ----------------

if __name__ == '__main__':
    app.run(debug=True)