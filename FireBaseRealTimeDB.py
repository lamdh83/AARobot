import pyrebase

class FireBase:
    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyBvP5tmbxKk0OF1IIAu7FhPmpz7UV2A79k",
            "authDomain": "compuspeech.firebaseapp.com",
            "databaseURL": "https://compuspeech-default-rtdb.firebaseio.com",
            "projectId": "compuspeech",
            "storageBucket": "compuspeech.appspot.com",
            "messagingSenderId": "317903435823",
            "appId": "1:317903435823:web:b3fdd50b36f07d4981aeda",
            "measurementId": "G-P5BJ2H5TB4"
        }
        self.firebase = pyrebase.initialize_app(self.config)
        self.datebase = self.firebase.database()


    def getData(self):
        try:
            data = self.datebase.child("Order").get()
            dt = data.val()
            dateTime = dt["dateTime"]
            message = dt["message"]
        except:
            dateTime = ""
            message = ""
        return dateTime, message

    def delete(self):
        try:
            self.datebase.child("Order").remove()
        except:
            pass

    def upImage(self):
        storage = self.firebase.storage()
        storage.child("screencapture.png").put("screencapture/screencapture.png")

def main():
    fire = FireBase()
    # dateTime, message = fire.getData()
    # print(f'{dateTime}/ {message}')
    # fire.delete()
    fire.upImage()

if __name__ == "__main__":
    main()






