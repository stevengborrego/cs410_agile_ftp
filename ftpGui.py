import ftp
from ftplib import FTP
import tkinter
import psutil

class Ftp_Gui():

    def __init__(self):
        self.gui_window = tkinter.Tk()


    def login(self,host='ftp.epizy.com', user='epiz_32073599', password='UMDmFiWWBp'):
        with FTP(host) as ftp:
                ftp.login(user=user,passwd=password)

    def get_available_memory(self, text_gui_msg):
        self.login()
        print("CPU utilised ", psutil.cpu_percent(2))
        available = round((psutil.virtual_memory()[1] / (1024.0 ** 3)), 2)
        Used = round((psutil.virtual_memory()[3] / (1024.0 ** 3)), 2)
        text_gui_msg.insert(tkinter.END, "Available Memory : ")
        text_gui_msg.insert(tkinter.END, available)
        text_gui_msg.insert(tkinter.END," GB \n")
        text_gui_msg.insert(tkinter.END, "Used Memory : ")
        text_gui_msg.insert(tkinter.END, Used)
        text_gui_msg.insert(tkinter.END, " GB \n")

if __name__ == '__main__':
    gui = Ftp_Gui()
    gui.gui_window.title("FTP_Client_410")
    gui.gui_window.wm_iconbitmap("favicon.ico")
    gui.gui_window.geometry("1000x600")
    text_gui_msg = tkinter.Text(gui.gui_window, height = 10, width = 36, bg= "light cyan")

    ftp_mem = tkinter.Label(gui.gui_window, command=gui.get_available_memory(text_gui_msg))
    text_gui_msg.pack()
    gui.gui_window.mainloop()

