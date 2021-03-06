import PySimpleGUI as sg

import codewars as cw

sg.theme('BluePurple')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Basic Course Homeworks')],
          [sg.Text('DescOrder'), sg.InputText(key='DescIn'), sg.InputText(readonly=True, key='DescRes'),
           sg.Button('DescOrder')],
          [sg.Text('RomanNum'), sg.InputText(key='RomanIn'), sg.InputText(readonly=True, key='RomanRes'),
           sg.Button('RomanNum')],
          [sg.Text('IfPrime'), sg.InputText(key='IfPrimeIn'), sg.InputText(readonly=True, key='IfPrimeRes'),
           sg.Button('IfPrime')],
          [sg.Text('Vowels'), sg.InputText(key='VowelsIn'), sg.InputText(readonly=True, key='VowelsRes'),
           sg.Button('Vowels')],
          [sg.Text('Bus'), sg.InputText(key='BusIn'), sg.InputText(readonly=True, key='BusRes'), sg.Button('Bus')],
          [sg.Text('PigLatin'), sg.InputText(key='PigLatinIn'), sg.InputText(readonly=True, key='PigLatinRes'),
           sg.Button('PigLatin')],
          [sg.Text('IntFilter'), sg.InputText(key='IntFilterIn'), sg.InputText(readonly=True, key='IntFilterRes'),
           sg.Button('IntFilter')],
          [sg.Text('WordScore'), sg.InputText(key='WordScoreIn'), sg.InputText(readonly=True, key='WordScoreRes'),
           sg.Button('WordScore')],
          [sg.Button('EXIT')]]

# Create the Window
window = sg.Window('Basic Course Homeworks', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':  # if user closes window or clicks cancel
        break
    if event == 'DescOrder':
        window.Element('DescRes').Update(cw.descending_order(values['DescIn']))
    if event == 'RomanNum':
        window.Element('RomanRes').Update(cw.romanNum(values['RomanIn']))
    if event == 'IfPrime':
        window.Element('IfPrimeRes').Update(cw.primeCheck(values['IfPrimeIn']))
    if event == 'Vowels':
        window.Element('VowelsRes').Update(cw.vowelsCount(values['VowelsIn']))
    if event == 'Bus':
        window.Element('BusRes').Update(cw.BusStops(values['BusIn']))
    if event == 'PigLatin':
        window.Element('PigLatinRes').Update(cw.pigLatin(values['PigLatinIn']))
    if event == 'IntFilter':
        window.Element('IntFilterRes').Update(cw.intFilter(values['IntFilterIn']))
    if event == 'WordScore':
        window.Element('WordScoreRes').Update(cw.high(values['WordScoreIn']))
window.close()
