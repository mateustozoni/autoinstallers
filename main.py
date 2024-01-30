import PySimpleGUI as sg
import programs.firefox
import programs.occt
import programs.hwinfo

sg.theme('DarkPurple')   # Add a touch of color


def start_gui():
    title = ("Arial", 20)

    layout = [
        [sg.Text("Programinha do Milk", font=title, pad=(sg.DEFAULT_ELEMENT_PADDING, (10, 30)))],
        [sg.Text('Programas para instalar:')],
        [sg.Button('Instalar OCCT')],
        [sg.Button('Instalar HWiNFO')],
        [sg.Button('Instalar Firefox', pad=(sg.DEFAULT_ELEMENT_PADDING, (10, 30)))],
        [sg.Button('Fechar')]
    ]

    window = sg.Window('Programa de cria do Milk', layout, size=(300, 600))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Fechar':
            break

        if event == 'Instalar Firefox':
            programs.firefox.download_and_install()

        if event == 'Instalar OCCT':
            programs.occt.download_and_install()

        if event == 'Instalar HWiNFO':
            programs.hwinfo.download_and_install()

    window.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_gui()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
