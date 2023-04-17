import VirtualPainter as vp
import os
import PySimpleGUI as sg
from datetime import datetime
from PIL import Image
import home as h
import slide
from session_sent import emailsender

def layout3():
    layout = [[sg.Image("home.png")]]
    window = sg.Window("Home", layout)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event == sg.WIN_CLOSED:
            break
    window.close()

def final_window():
    file_types = [("JPEG (*.jpg)", "*.jpg"),
                  ("All files (*.*)", "*.*")]
    layout2 = [[sg.Text("                                      Thank you using Airoboard ")],

               [sg.Text(
                   "---------------------------------------------------------------------------------------------------------------------------         ")],
               [sg.Text("                                         Send Your Drawing To Your Email")],
               [sg.Text(
                   "---------------------------------------------------------------------------------------------------------------------------         ")],
               [sg.Text("Enter Your Email Address to send Screen time and Drawing")],
               [sg.Text('Email : '), sg.InputText()],
               [sg.Text(size=(40, 1), key='-OUTPUT-')],
               [sg.Text('Choose An Image to insert', size=(40, 1))],
               [sg.Text('Your Folder', size=(15, 1), justification='right'),
                sg.InputText('Default Folder', key="-FILE-"), sg.FileBrowse(file_types=file_types),
                sg.Button("Load Image")],

               [sg.Text(
                   "---------------------------------------------------------------------------------------------------------------------------         ")],
               [sg.Text("                                            Send Your Feedback")],
               [sg.Text(
                   "                                                                                                                                                                        ")],

               [sg.Multiline(size=(30, 5), key='textbox')],
               [sg.Text(
                   "                                                                                                                                                                        ")],
               [sg.Button("Send Email")]
               ]
    window = sg.Window("Feedback", layout2)
    while True:
        event, values = window.read()

        if event == "Send Email":
            print(values)
            if values[0]:
                id_email=values[0]
                send_image=values["Browse"]
                text=values["textbox"]
                emailsender(id_email, send_image, text)
        if event in (None, 'Exit'):
            break
        elif event == sg.WIN_CLOSED:
            break
    window.close()
def middlelayer():
    column1 = []
    file_types = [("JPEG (*.jpg)", "*.jpg"),
                  ("All files (*.*)", "*.*")]
    font = ("Arial", 15)
    font1 = ("Arial", 10)
    layout3 = [[sg.Image("Airo_Board.png")],
               [sg.Text("-----------------------------------------------------------------------------------------",
                        key='-text-',
                        font=font)],
               [sg.Text("                                                 "), sg.Button("HOME", font=("Arial", 10)),
                sg.Button("ABOUT", font=("Arial", 10)), sg.Button("WORKS", font=("Arial", 10))],
               [sg.Text("-----------------------------------------------------------------------------------------",
                        key='-text-',
                        font=font)],
               [sg.Text('User Name', key='-text-', font=font1), sg.InputText()],
               [sg.Text(size=(40, 1), key='-OUTPUT-')],
               [sg.Text('Password', key='-text-', font=font1), sg.InputText("", key='Password', password_char='*')],
               [sg.Text('_' * 80)],
               [sg.Text('Choose An Image to insert', size=(40, 1))],
               [sg.Text('Your Folder', size=(15, 1), justification='right'),
                sg.InputText('Default Folder', key="-FILE-"), sg.FileBrowse(file_types=file_types),
                sg.Button("Load Image")],

               [sg.Text(
                   "----------------------------------------------------------------------------------------------------------------------------")],
               [sg.Frame(layout=[
                   [sg.CBox('Audio Recording', size=(10, 1)),
                    sg.CBox('Video Recording', default=True)]
               ], title='Options For Recording', relief=sg.RELIEF_SUNKEN,
                   tooltip='Use these to set flags'), sg.Col(column1)],
               [sg.Text(
                   "----------------------------------------------------------------------------------------------------------------------------")],
               [sg.Text("                                           "), sg.Button("Virtual Board", font=("Arial", 12)),
                sg.Button("Slide Show", font=("Arial", 12))]
               ]
    window = sg.Window("Home", layout3)
    while True:
        event, values = window.read()
        if event == "HOME":
            print(values)
            layout3()

        elif event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image_load = Image.open(values["-FILE-"])
                image_load.thumbnail((400, 400))
                # bio = io.BytesIO()
                # image.save(bio, format="PNG")
                # window["-IMAGE-"].update(data=bio.getvalue())
        if event == "Virtual Board":
            print(values)
            if values[1]:
                if values["Password"] == "root":
                    name = values[1]
                    now = datetime.now()
                    session_start_time = now.strftime('Date: %d/%Y/%m Time: %I:%M:%S')
                    vp.airoboard(session_start_time, name, image_load)
                    window.close()
                    window = sg.Window("Virtual Board", layout3)
                    window.close()
                    h.final_window()

                else:
                    window['-OUTPUT-'].update("Wrong Password !", text_color='red')
            else:
                window['-OUTPUT-'].update("Please enter the User Name!", text_color='red')
            if values[3]:
                # rec_audios()
                pass
        if event in (None, 'Exit'):
            break
        elif event == sg.WIN_CLOSED:
            break
    window.close()