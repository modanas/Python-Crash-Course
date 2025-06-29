import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created By Anas")
    while True:
        x = input("Enter what you want me to speak : ")
        if x == "q" :
            break
        command = f'powershell -Command "(New-Object -ComObject SAPI.SpVoice).Speak(\\"{x}\\")"'
        os.system(command)
