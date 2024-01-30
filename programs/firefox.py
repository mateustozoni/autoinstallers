import os
import PySimpleGUI as sg
from urllib.request import urlretrieve
from time import sleep

def download():
    url = "https://download.mozilla.org/?product=firefox-msi-latest-ssl&os=win64&lang=pt-BR"
    filename = "firefox_installer.msi"

    urlretrieve(url, filename)


def install():
    os.system("firefox_installer.msi /quiet /norestart")


def download_and_install():
    layout = [
        [sg.Text("Baixando e instalando o Firefox, aguarde")],
        [sg.Text("Status atual:"), sg.Text("Iniciando", key="status")],
        [sg.ProgressBar(max_value=4, key="loading")]
    ]

    loading_window = sg.Window('Baixando e instalando o Firefox', layout, finalize=True)

    loading_window["loading"].update_bar(1)
    loading_window["status"].update("Iniciando Download")
    download()
    loading_window["loading"].update_bar(2)

    loading_window["status"].update("iniciando Instalação")
    loading_window["loading"].update_bar(3)
    install()
    loading_window["loading"].update_bar(4)
    loading_window["status"].update("Instalação finalizada")

    sleep(2)

    loading_window.close()

    return
