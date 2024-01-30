import os
import PySimpleGUI as sg
from urllib.request import urlretrieve
from time import sleep

def download():
    url = "https://drive.usercontent.google.com/download?id=1QKTal-xyDuLzLdsJ7rQMM8eP5fQl3-Lk&export=download&confirm=t&uuid=9111d31a-e291-4657-a885-f7baca7f2343"
    filename = "occt_installer.exe"

    urlretrieve(url, filename)


def install():
    os.system("occt_installer.exe")


def download_and_install():
    layout = [
        [sg.Text("Baixando e instalando o OCCT, aguarde")],
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
