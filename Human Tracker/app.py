import cv2
import sqlite3
import hashlib
import getpass

class PeopleTracker:
    def __init__(self, video_path):
        self.video_path = video_path
        self.video_capture = cv2.VideoCapture(video_path)

    def track(self):
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        while True:
            ret, frame = self.video_capture.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            (regions, _) = hog.detectMultiScale(gray, winStride=(5, 5), padding=(3, 3), scale=1.21)

            for (x, y, w, h) in regions:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imshow('People Tracking', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.video_capture.release()
        cv2.destroyAllWindows()

class LoginSystem:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
        self.conn.commit()

    def login(self):
        username = input('Enter your username: ')
        password = getpass.getpass('Enter your password: ')
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
        if self.cursor.fetchone():
            return True
        else:
            print('Incorrect username or password')
            return False

    def register(self):
        username = input('Enter a new username: ')
        password = getpass.getpass('Enter a new password: ')
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        if self.cursor.fetchone():
            print('Username is already taken')
        else:
            self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            self.conn.commit()
            print('Registration successful')

def main():
    login_system = LoginSystem()
    while True:
        print('1. Login')
        print('2. Register')
        choice = input('Enter your choice: ')
        if choice == '1':
            if login_system.login():
                tracker = PeopleTracker('camera2.mp4')
                tracker.track()
                break
        elif choice == '2':
            login_system.register()
        else:
            print('Invalid choice')

if __name__ == "__main__":
    main()