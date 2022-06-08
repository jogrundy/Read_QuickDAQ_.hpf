import PySimpleGUI as sg
import os
import read_hpf

working_directory = os.getcwd()

layout = [
        [
            sg.Text('choose a .hpf file')
            ],
        [
            sg.Text()
            ],
        [
            sg.InputText(key='-FILE_PATH-'),
            sg.FileBrowse(initial_folder=working_directory, file_types=[("HPF Files", ".hpf")])
            ],
        [
           sg.Button('submit'), 
           sg.Exit()
            ]
        ]

window = sg.Window('hpf converter', layout)

def doStuff(hpf_address):
    read_hpf.test_method(hpf_address)
    read_hpf.write_info_and_csv_from_hpf(hpf_address)

while True:
    event, value = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event == 'submit':
        hpf_address = value["-FILE_PATH-"]
        doStuff(hpf_address)

window.close()
