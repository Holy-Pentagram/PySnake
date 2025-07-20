import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QGuiApplication
from PyQt5.QtCore import QTimer, Qt
speed = None
ascii_art_default = '''
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠟⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠈⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣦⡀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⡇⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠾⠋⠁⢸⣿⡇⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⡇⠀⠀⠀⠀⠀⠀⠀⠙⢷⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡾⠛⠁⠀⠀⠀⣿⣼⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡏⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡾⠛⠁⠀⠀⠀⠀⠀⣸⡿⣿⠂⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⣿⠀⠀⠀⠀⠀⠶⠶⠶⠶⠶⠶⠿⠷⠶⠶⠤⣤⣤⣀⣀⡀⢀⣤⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⢠⣿⢣⡟⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣽⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡷⣸⠇⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢣⡿⠁⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣼⠃⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡏⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣿⣿⡾⠛⠉⣉⣽⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠶⠛⢛⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⢸⣿⡀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⢰⣾⠛⢉⣵⡟⣃⣤⣶⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⣠⣾⠏⣡⣴⣾⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⢈⡹⣇⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠙⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣰⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠶⠖⠲⠾⣿⣿⣦⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⣠⣴⡾⠋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠈⠙⢿⣄⠀⠀⠀⠀
                    ⠀⠀⣿⡛⠉⠁⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀
                    ⠀⠀⣾⣷⣦⣀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⠀
                    ⠀⡀⠈⠻⢿⣿⣿⣷⠆⠀⠙⠻⠿⣿⣿⡿⢿⣿⠋⠀⠀⠀⣴⠇⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆
                    ⠀⠻⣟⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣆⣀⣠⣼⢿⣧⠀⠀⠀⢀⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⠿⣛⠹⣮⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷
                    ⠀⠀⠈⠻⢦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢩⠿⠻⣯⢻⣷⣶⣿⡿⠋⠀⠀⠀⠉⠉⠉⠉⠁⠀⣐⣭⣾⡿⠋⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
                    ⠀⠀⠀⢀⣰⣿⣻⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠛⣍⠡⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟
                    ⠀⠀⠀⠛⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁
                    ⠀⠀⠀⢐⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀
                    ⠀⠀⠀⣼⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠃⠀⠀⠀
                    ⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⡟⠀⠀⠀⠀⠀
                    ⠀⠀⣰⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠛⠀⠀⠀⠀⠀⠀
                    ⢠⣾⢿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀
                    ⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠀⠀⠀⠀⠀⠀⠀⠀
                    ⣾⢿⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀
                    ⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀


▗▖ ▗▖▗▄▄▄▖▗▖  ▗▖    ▗▄▄▄▖▗▄▖      ▗▄▄▖▗▄▄▄▖▗▄▄▄▖     ▗▄▖     ▗▄▄▖ ▗▄▄▖ ▗▄▄▄▖ ▗▄▄▖▗▄▄▄▖
▐▌ ▐▌  █  ▐▛▚▖▐▌      █ ▐▌ ▐▌    ▐▌   ▐▌     █      ▐▌ ▐▌    ▐▌ ▐▌▐▌ ▐▌  █  ▐▌   ▐▌   
▐▌ ▐▌  █  ▐▌ ▝▜▌      █ ▐▌ ▐▌    ▐▌▝▜▌▐▛▀▀▘  █      ▐▛▀▜▌    ▐▛▀▘ ▐▛▀▚▖  █  ▐▌   ▐▛▀▀▘
▐▙█▟▌▗▄█▄▖▐▌  ▐▌      █ ▝▚▄▞▘    ▝▚▄▞▘▐▙▄▄▖  █      ▐▌ ▐▌    ▐▌   ▐▌ ▐▌▗▄█▄▖▝▚▄▄▖▐▙▄▄▖
                                                                                                                                                     
▗▄▄▄   ▗▄▖ ▗▄▄▖ ▗▖   ▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖                                                 
▐▌  █ ▐▌ ▐▌▐▌ ▐▌▐▌     █  ▐▛▚▖▐▌▐▌                                                    
▐▌  █ ▐▛▀▜▌▐▛▀▚▖▐▌     █  ▐▌ ▝▜▌▐▌▝▜▌                                                 
▐▙▄▄▀ ▐▌ ▐▌▐▌ ▐▌▐▙▄▄▖▗▄█▄▖▐▌  ▐▌▝▚▄▞▘                                                                                                                 
                                                                                  

⠀⠀⠀⠀⠀⠀⠀⠀
'''
ascii_art_win = '''
⣿⡿⠿⠛⠁⠀⠀⠀⠘⣾⡇⢸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠉⠛⢀⡀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠈⠛⢿⣿⣿⣿⣿⡄⠀⠀⠀⠘⣿⡇⣼⣿⣿⣿⣿
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠙⠇⠀⠉⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⢀⠀⠀⠀⠀⣠⠀⠉⠉⠉⠉⢉⠁⠀⢀⡀⢠⡄⠀⠀⠈⠋⢉⠀⡀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠉⢈⠉⢉⣽⣿⣿
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠰⣦⡤⠐⠀⠀⠀⠀⠀⠈⢢⣤⣴⣆⣐⣀⣀⣀⡀⣀⠠⣤⣼⣤⣧⣬⣤⣤⣾⣧⣤⣤⣶⣄⠀⠀⠨⠄⠃⢴⣤⡆⠀⠀⠀⠀⠀⠀⠀⢠⣴⡤⢛⣿⣿
⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⢰⣼⣟⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣯⣭⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠘⠿⠟⠀⠀⠀⠀⠀⢀⣾⡟⢀⣾⣿⣿
⣤⣴⣦⣄⣀⣀⠻⠶⣤⡄⠘⢻⡆⡀⠀⠀⠀⠀⢠⣿⣿⣶⣿⠿⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣧⣄⣀⠀⠀⢠⣧⡀⠀⠀⠀⠀⠀⠀⢀⣦⠘⣿⠀⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣶⣤⣁⡀⠀⢁⡗⢀⡀⢀⠀⢸⣿⡿⠋⢀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢽⣿⣿⣿⣿⣿⣿⣆⣘⡋⣀⡀⠀⠀⠀⠀⠀⠾⠇⣰⠇⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣈⡛⠻⠄⠀⣿⣇⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢁⣼⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣙⠻⢿⣿⣿⣿⣿⣿⣿⠟⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠿⣿⣿⣿⣿⣿⣿⣿⣭⣍⡻⢿⣤⣉⣛⠻⢿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣈⠹⢿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠇⠀⠀⠀⠀⠀⠂⠀⠺⠿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣙⠻⠿⣿⣿⡛⣿⣿⣿⣌⠻⣿⡻⣷⣦⣘⠻⢿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣇⣰⠃⠀⠀⣴⠟⠀⠀⠀⠀⢰⡀⠸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⢻⣿⣿⣿⣿⣿⣿⣿⣷⡈⢻⡿⣿⣦⣈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⢠⠀⠈⡟⢦⠈⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⣿⣿⣿⣿⡆⢻⣿⠻⣿⣿⣿⣿⣿⣿⣦⣌⠲⣝⡻⠿⣶⣦⣉⡻⠿⣿⣿⣿⣿⡿⠟⣉⣩⣤⣶⣶⣶⣶⣶⣶⣾⣿⣿⣷⠀⠈⠸⣿⡈⢿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠸⣿⣿⣿⣷⠀⣿⣆⢻⣿⣧⣬⡿⣿⣿⣿⣿⣦⡙⢿⣦⣌⠙⠻⠿⠷⢶⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠙⣧⠈⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣇⠸⣿⡄⠹⣿⣿⣿⣷⣙⣻⠿⠿⠿⠦⡈⠿⣿⣿⣿⣶⣶⣤⣄⣉⣳⠾⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠘⠀⠹⣿
⣿⣿⣿⣿⣿⣿⡟⢻⣿⣿⣿⣿⣷⡀⢿⣿⣿⣿⡀⠀⠐⠀⠈⠙⠻⣻⣿⣿⣿⣿⣿⣆⠱⣦⣌⣉⠛⠿⠿⣿⠿⠋⣁⣶⣦⣍⣱⣦⣬⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⢈
⠛⣿⣿⣿⣿⣿⣷⠀⢻⣿⣿⣿⣿⣷⡜⣿⣿⣿⣷⡀⠀⠀⠈⠙⣶⣦⡈⠙⣿⣿⣿⣿⡆⢹⡿⠭⠀⢀⣀⣤⣤⣤⣽⣿⣿⣿⣿⣿⣿⣿⣿⠆⠙⣿⣿⣿⣿⣿⣿⡿⢋⣡⣾⣿
⠀⢿⣿⣿⣿⣿⣿⡄⠈⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣷⠀⢸⣿⣦⡀⠙⠿⣧⠈⢿⣿⣿⣷⡌⢷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣭⣉⣉⣉⣥⣶⣿⣿⣿⣿
⣦⠈⠙⣿⣿⣿⣿⣿⡀⠈⢹⣿⣿⣿⣿⣷⡈⣿⣿⣿⣆⠘⣿⣿⣿⣦⡀⠈⠳⡘⣿⣿⣿⣷⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿
⣿⣆⠀⢻⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣷⡈⣿⣿⣿⡄⣿⣿⣿⣿⣿⣆⠀⠀⠈⢿⣿⣿⣷⡸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⡄⠘⣿⣿⣿⣿⣿⡀⠀⠹⣿⣿⣿⣿⣧⣡⢹⣿⣿⣇⢸⣿⣿⣭⣉⡉⠓⢄⠀⠘⣿⣿⣿⣇⠙⣿⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣷⠀⢹⣿⣿⣿⣿⣧⠀⠀⢻⣿⣿⣿⣿⣿⡀⢻⣿⣿⠘⣿⣿⣿⣿⣿⣶⡀⠀⠀⠈⢿⣿⣿⣧⡈⢻⣯⡙⠍⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠹⣆⠈⠉⣿⣿⣿⣿⡇⠀⠈⢿⣿⣿⣿⣿⣷⠈⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣆⢀⣀⠀⠻⣿⣿⣿⣆⠻⣿⣶⣄⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣆⠘⡆⠈⢿⣿⣿⣿⣿⡀⠀⠘⢿⣿⣿⣿⣿⣆⢿⣿⡇⢸⣿⣿⣿⡿⠋⣽⣿⠀⣿⣷⡄⠸⣟⠻⣿⣦⠘⣿⣿⣧⡀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣆⠀⠀⠀⢻⣿⣿⣿⣷⡀⠀⠸⣿⣿⣿⣿⣿⠈⣿⣧⠘⣿⣿⠟⣡⣾⣿⡟⢠⣿⢿⣿⢄⠙⠲⢿⣿⠇⠻⣿⣿⣿⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣧⠀⠁⠀⢻⣿⣿⣿⣧⠀⠀⠹⣿⣿⣿⣿⡇⠸⣿⡀⠟⢁⣼⣿⣿⠏⣠⣊⠍⠉⠛⢦⣽⣶⣤⣤⣤⣤⠘⣿⣿⣇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣄⠰⠀⢻⣿⣿⣿⣆⠀⠀⢹⣿⣿⣿⣿⡄⢿⠃⣴⣿⣿⠟⢡⣾⠟⠁⠀⣾⡆⠀⠉⠛⠿⣿⣿⣿⣷⠈⢿⣿⡀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⢹⣿⣿⣷⠀⠀⠈⢻⣿⣿⣿⣷⠀⢰⣿⠟⠁⠔⠉⠀⣠⢀⡄⢹⠃⢰⣄⡐⢤⣈⠛⠻⣿⠃⠘⣿⣧⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠉⣻⣿⠃⠀⢀⠀⣿⣿⣿⣿⡆⠘⠁⠀⣠⡴⠀⣼⠏⣸⢇⠈⢸⣿⠙⣿⣆⠹⣿⣦⡈⠑⢀⡙⠻⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢠⣴⣦⡈⠂⠙⢿⣿⣿⡆⠀⢀⣴⡿⠁⣼⠇⣠⡇⠈⠀⠈⠻⣇⢸⣿⡆⣿⣿⣿⡆⠀⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠘⣿⣿⣿⣆⠀⢀⠙⠿⠇⢠⣿⡿⢀⣼⠏⠀⠋⠀⠀⠀⠀⠀⠈⠀⣿⣇⢸⣿⡿⢧⣼⠋⢀⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠘⢿⣿⣿⣷⣦⠙⢶⣤⡿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⢀⣿⠃⣾⠏⢀⣾⣿⣿⡏⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠘⢿⣿⣿⣿⣿⣦⡙⢿⣝⢿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⡾⢁⣼⠟⢀⣾⣿⣿⡿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⢻⣿⣿⣿⣿⣿⣦⡙⢷⣝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠟⢀⣠⡾⠋⣰⣿⣿⣿⡿⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠻⣿⣿⣿⣿⣿⣿⣦⡙⠳⣀⠀⢄⣤⣤⣤⣤⡄⠀⢀⣴⡿⠏⣠⣾⣿⣿⣿⡟⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠘⢿⣿⣿⣿⣿⣿⣿⣦⣈⠑⠺⢿⣿⣿⣋⣠⠴⠟⢉⣠⣾⣿⣿⣿⣿⠋⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙⢿⣿⣿⣿⣿⣿⣷⣌⠷⣦⣤⣤⣤⣤⣶⣿⣿⣿⣿⣿⣿⠟⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙⢿⣿⣿⣿⣿⣿⣿⣶⡀⠙⠃⣀⣴⣾⣿⣿⡿⠟⢁⣴⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⢿⣶⣄⡙⠻⢿⣿⣿⣿⣋⣡⣴⡾⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠉⠛⠿⢷⣶⡾⠿⠟⠉⢁⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠢⡀⠀⣠⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠈⠀⠉⢩⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠗⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠓⢀⣄⣤⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠸⣿⡟⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠹⠃⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
ascii_art_loose = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣤⣶⣦⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⣿⣤⡄⠀⠀⠀⠀⢀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣷⣿⣷⣶⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠈⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⠀⠀⠀⠀⠀⠀
⢰⣿⣿⣿⣿⡟⠉⠘⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
⢘⣿⣿⣿⣿⣿⡄⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠀⠀
⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⢸⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⢀⣀⣀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

'''
qwerty = input("Choose difficulty level:\n1.easy\n2.medium\n3.hard\nChoice: ").lower()
while qwerty in ["easy", "1", "medium", "2", "hard", "3"]:
    if qwerty == "easy" or qwerty == "1":
        speed = 200
        break
    elif qwerty == "medium" or qwerty == "2":
        speed = 150
        break
    elif qwerty == "hard" or qwerty == "3":
        speed = 100
        break
    else:
        qwerty = input("Invalid choice. Please try again.")
    
    
apple_location_x = random.randint(0, 24) * 25
apple_location_y = random.randint(0, 24) * 25
snake = [{"x": 0, "y": 0}]
last_keystroke = Qt.Key_Right  
can_turn = True

class SnakeGame(QMainWindow): 
    def __init__(self):
        super().__init__()
        screen = QGuiApplication.primaryScreen().availableGeometry()
        screen_width = screen.width()
        screen_height = screen.height()
        
        # Make game window smaller to give more space to ASCII art
        game_width = screen_width // 3
        game_height = int(screen_height * 0.7)  # Make game taller
        
        # Position game centered on the right side
        x = int(screen_width - game_width - (screen_width * 0.05))  # Add some padding from right edge
        y = (screen_height - game_height) // 2
        
        self.setGeometry(x, y, game_width, game_height)
        self.setFixedSize(game_width, game_height)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.CustomizeWindowHint)
        self.restart_button = QPushButton("Repeat", self)
        self.restart_button.setParent(self)
        self.restart_button.setGeometry((game_width-200)//2, 10, 200, 50)
        self.restart_button.raise_()
        self.restart_button.clicked.connect(self.repeat_game)
        self.restart_button.hide()
        self.SetUI()

    def keyPressEvent(self, event):
        global last_keystroke, can_turn
        if not can_turn:
            return
        if event.key() in (Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down):
            last_keystroke = event.key()
            can_turn = False
        self.board.update()

    def SetUI(self):
        global speed
        self.setWindowTitle("Snake Game")
        self.setStyleSheet("""
            background-color: #0a0a0a;
            border: 3px solid #444444;
        """)
        self.board = GameBoard()
        self.setCentralWidget(self.board)
        self.game_over_label = QLabel("GAME OVER", self)
        self.game_over_label.setStyleSheet("""
            color: #ff1744;
            font-size: 64px;
            font-weight: 900;
            font-family: 'Arial Black', Arial, sans-serif;
            background-color: rgba(0, 0, 0, 0.95);
            border: 4px solid #ff1744;
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            letter-spacing: 6px;
        """)
        self.restart_button.setStyleSheet("""
            background-color: #222;
            color: #fff;
            font-size: 22px;
            font-weight: bold;
            border: 2px solid #00ff00;
            border-radius: 10px;
            padding: 10px 20px;""")
        self.game_over_label.setAlignment(Qt.AlignCenter)
        self.game_over_label.setGeometry(0, 0, 625, 625)
        self.game_over_label.hide()
        self.restart_button.hide()
        self.timer = QTimer()
        self.timer.timeout.connect(self.board.snake_loop)
        self.timer.start(speed)
        self.board.update()

    def repeat_game(self):
        global snake, last_keystroke, can_turn, apple_location_x, apple_location_y, score, bomboclat
        snake = [{"x": 0, "y": 0}]
        last_keystroke = Qt.Key_Right
        can_turn = True
        apple_location_x = random.randint(0, 24) * 25
        apple_location_y = random.randint(0, 24) * 25
        score = 0
        bomboclat.set_score(score)
        # Reset ASCII art to default
        asciiart.set_ascii(ascii_art_default)
        self.game_over_label.hide()
        self.restart_button.hide()
        self.board.update()
        self.setFocus() 

class GameBoard(QWidget):
    def paintEvent(self, event):
        global apple_location_x, apple_location_y, snake
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor('#1a1a1a'))
        painter.setPen(QColor('#333333'))
        for i in range(0, 625, 25):
            painter.drawLine(i, 0, i, 625)
            painter.drawLine(0, i, 625, i)
        painter.setBrush(QColor('#00aa00'))
        painter.setPen(QColor('#008800'))
        for segment in snake[1:]:
            painter.drawRect(segment["x"], segment["y"], 25, 25)
        painter.setBrush(QColor('#00ff00'))
        painter.setPen(QColor('#00aa00'))
        painter.drawRect(snake[0]["x"], snake[0]["y"], 25, 25)
        painter.setBrush(QColor('#ff4444'))
        painter.setPen(QColor('#aa0000'))
        painter.drawEllipse(apple_location_x + 3, apple_location_y + 3, 19, 19)
        painter.end()
    def snake_loop(self):
        global snake, last_keystroke, can_turn, apple_location_x, apple_location_y, score, bomboclat, selected_art, asciiart
        if last_keystroke is not None:
            head_x = snake[0]["x"]
            head_y = snake[0]["y"]
            if last_keystroke == Qt.Key_Left:
                new_head_x = head_x - 25
                new_head_y = head_y
            elif last_keystroke == Qt.Key_Right:
                new_head_x = head_x + 25
                new_head_y = head_y
            elif last_keystroke == Qt.Key_Up:
                new_head_x = head_x
                new_head_y = head_y - 25
            elif last_keystroke == Qt.Key_Down:
                new_head_x = head_x
                new_head_y = head_y + 25

            if new_head_x < 0 or new_head_x >= 625 or new_head_y < 0 or new_head_y >= 625:
                self.parent().game_over_label.show()
                self.parent().restart_button.setGeometry((625-200)//2, 500, 200, 50)
                self.parent().restart_button.show()
                self.parent().restart_button.raise_()
                asciiart.set_ascii(ascii_art_loose)
                return
            for segment in snake:
                if new_head_x == segment["x"] and new_head_y == segment["y"]:
                    self.parent().game_over_label.show()
                    self.parent().restart_button.setGeometry((625-200)//2, 500, 200, 50)
                    self.parent().restart_button.show()
                    self.parent().restart_button.raise_()
                    asciiart.set_ascii(ascii_art_loose)
                    return
            snake.insert(0, {"x": new_head_x, "y": new_head_y})
            if new_head_x == apple_location_x and new_head_y == apple_location_y:
                score += 1
                bomboclat.set_score(score)
                # Create list of all available positions
                available_positions = []
                for x in range(0, 625, 25):
                    for y in range(0, 625, 25):
                        position_valid = True
                        for segment in snake:
                            if segment["x"] == x and segment["y"] == y:
                                position_valid = False
                                break
                        if position_valid:
                            available_positions.append({"x": x, "y": y})
                
                # If there are available positions, randomly choose one
                if available_positions:
                    new_pos = random.choice(available_positions)
                    apple_location_x = new_pos["x"]
                    apple_location_y = new_pos["y"]

                if len(snake) >= 625: 
                    asciiart.set_ascii(ascii_art_default)
                    return
            else:
                snake.pop()
            self.update()
            can_turn = True

#window score
class SCORE(QMainWindow):
    def __init__(self):
        super().__init__()
        global score
        score = 0
        screen = QGuiApplication.primaryScreen().availableGeometry()
        score_width = screen.width() // 2
        score_height = int(screen.height() * 0.1)
        x = screen.width() // 2
        y = 0
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(x, y, score_width, score_height)
        self.setStyleSheet("background-color: #000;")
        self.label = QLabel("SCORE: 0", self)
        self.label.setGeometry(0, 0, score_width, score_height)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            font-size: 48px;
            color: #00ff00;
            font-weight: bold;
            font-family: 'Arial Black', Arial, sans-serif;
            border-bottom: 2px solid #00ff00;
            background: transparent;
        """)
        self.setFixedSize(score_width, score_height)
    def set_score(self, value):
        self.label.setText(f"SCORE: {value}")
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor('#000000'))




class ASCIIART(QMainWindow):
    def __init__(self):
        super().__init__()
        global pos
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(0, 0, 1000, 1500)
        self.setStyleSheet("background-color: #000;")
        
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 1000, 1500)
        self.label.setStyleSheet("""
            color: #00ff00;
            font-family: monospace;
            font-size: 12px;
            background: transparent;
            padding: 20px;
        """)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText(ascii_art_default)
        
    def set_ascii(self, text):
        self.label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = SnakeGame()
    game.show()
    pos = game.pos()
    bomboclat = SCORE()
    bomboclat.show()
    asciiart = ASCIIART()
    asciiart.show()
    def close_all(event):
        bomboclat.close()
        asciiart.close()
        event.accept()
    game.closeEvent = close_all
    sys.exit(app.exec_())




