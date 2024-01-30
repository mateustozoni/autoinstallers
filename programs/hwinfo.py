import os
import PySimpleGUI as sg
from urllib.request import urlretrieve
from time import sleep

def download():
    url = "https://www.sac.sk/download/utildiag/hwi_768.exe"
    filename = "hwinfo_installer.exe"

    urlretrieve(url, filename)


def install():
    os.system("hwinfo_installer.exe /q")


def download_and_install():
    layout = [
        [sg.Text("Baixando e instalando o HWiNFO, aguarde")],
        [sg.Text("Status atual:"), sg.Text("Iniciando", key="status")],
        [sg.ProgressBar(max_value=4, key="loading")]
    ]

    loading_window = sg.Window('Baixando e instalando o HWiNFO', layout, finalize=True)

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
