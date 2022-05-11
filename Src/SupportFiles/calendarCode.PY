import tkinter.ttk as ttk
from tkinter import *
from tkcalendar import Calendar
from time import sleep
from datetime import datetime

class calendarCode:

    def __init__(self) -> None:
        
        self.frame_search = ttk.Frame(self.root)
        self.button_start = ttk.Button(self.frame_search,
            text='DE',
            command=lambda: self._open_calendar_start()
        )
        self.str_start = StringVar()
        self.label_start = ttk.Label(self.frame_search,
            textvariable=self.str_start
        )
        self.calendar_start = Calendar(self.frame_search, 
            selectmode='day', 
            locate='pt_BR', 
            firstweekday='sunday',
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day
        )
        self.calendar_start.bind('<<CalendarSelected>>', self._select_date)
        self.button_end = ttk.Button(self.frame_search,
            text='ATÉ',
            command=lambda: self._open_calendar_end()
        )
        self.str_end = StringVar()
        self.label_end = ttk.Label(self.frame_search,
            textvariable=self.str_end
        )
        self.calendar_end = Calendar(self.frame_search, 
            selectmode='day', 
            locate='pt_BR', 
            firstweekday='sunday',
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day
        )
        self.calendar_end.bind('<<CalendarSelected>>', self._select_date)
    
    def _open_calendar_start(self):
        self.calendar_end.grid_forget()
        self.calendar_start.grid(row=2, column=0, columnspan=3)
        #ProfileApp.set_geometry(self.root)
    
    def _open_calendar_end(self):
        self.calendar_start.grid_forget()
        self.calendar_end.grid(row=2, column=0, columnspan=3)
        #ProfileApp.set_geometry(self.root)

    def _select_date(self, evt=None):
        date_start = self.calendar_start.selection_get()
        date_end = self.calendar_end.selection_get()
        date_start = f'{date_start.day}/{date_start.month}/{date_start.year}'
        date_end = f'{date_end.day}/{date_end.month}/{date_end.year}'
        self.str_start.set(date_start)
        self.str_end.set(date_end)
        sleep(0.5)
        self.calendar_start.grid_forget()
        self.calendar_end.grid_forget()
        #ProfileApp.set_geometry(self.root)