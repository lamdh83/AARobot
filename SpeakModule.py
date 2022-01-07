#install pyaudio
# pip install pipwin
# pipwin install pyaudio
import pyttsx3

class Speak():
    def __init__(self):
        self.robot_mouth = pyttsx3.init('dummy')
        self.voices = self.robot_mouth.getProperty("voices")
        self.robot_mouth.setProperty("voice", self.voices[1].id)

    def noi(self, s='xin chào cả nhà'):
        self.robot_mouth.say(s)
        self.robot_mouth.runAndWait()

def main():
    robot_mouth = pyttsx3.init('dummy')
    s='A Bi xin chào cả nhà'
    # voices = robot_mouth.getProperty("voices")
    # robot_mouth.setProperty("voice", voices[1].id)
    robot_mouth.say("hello")
    robot_mouth.runAndWait()


if __name__ == "__main__":
    main()
