import PySimpleGUI as sg

sg.theme('DarkAmber')


def oktextui(message, title):
    layout = [[sg.Text(message)],
              [sg.Button("OK")]]
    window = sg.Window(title, layout, finalize=True)
    window.Maximize()
    while True:
        event = window.read()
        if event == sg.WIN_CLOSED or event == "OK":
            break
        break
    window.close()


def twobuttonui(button1, button2, message, title):
    layout = [[sg.Text(message)],
              [sg.Button(button1)],
              [sg.Button(button2)]]
    window = sg.Window(title, layout, finalize=True)
    window.Maximize()
    while True:
        event = window.read()
        if event == sg.WIN_CLOSED or event == "OK":
            break
        break
    window.close()
    return event


def threebuttonui(button1, button2, button3, message, title):
    layout = [[sg.Text(message)],
              [sg.Button(button1)],
              [sg.Button(button2)],
              [sg.Button(button3)]]
    window = sg.Window(title, layout, finalize=True)
    window.Maximize()
    while True:
        event = window.read()
        if event == sg.WIN_CLOSED or event == "OK":
            break
        break
    window.close()
    return event


def listbuttonui(buttonlist, message, title):
    layout = [[sg.Text(message)]]
    for i in buttonlist:
        layout.append(f"[sg.Button({buttonlist[i]})")
    window = sg.Window(title, layout, finalize=True)
    window.Maximize()
    while True:
        event = window.read()
        if event == sg.WIN_CLOSED or not event == "":
            break
        break
    window.close()
    return event
