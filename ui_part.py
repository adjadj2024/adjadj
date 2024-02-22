import datetime
import time
import tkinter as tk
from random import choice
from tkinter import ttk

from multiprocessing import Process, get_context
from threading import Thread
import asyncio

from request_functionality import Requests
from auth_page import Authorization
from database import Database
from email_part import Email
from logger import Logger


class MyApp:
    def __init__(self, master):
        self.tracking_process = None
        self.periodical_proc = None
        self.fast_requests = None
        self.fast_slot_requests = None
        self.fast_requests_pyramid = None
        self.start_process = None
        self.standard_proc = None
        self.rows = []

        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.section1 = tk.Frame(self.frame, height=100, borderwidth=1, relief=tk.SUNKEN)

        self.section1.pack(fill=tk.BOTH, expand=True)
        self.create_section_1()

    def create_section_1(self):
        self.insert_user_section = tk.Frame(self.section1, bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.insert_user_section.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        self.username_label = tk.Label(self.insert_user_section, text="Username", fg="black")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_field = tk.Entry(self.insert_user_section)
        self.username_field.grid(row=1, column=0, padx=10, pady=10)
        self.password_label = tk.Label(self.insert_user_section, text="Password", fg="black")
        self.password_label.grid(row=0, column=1, padx=10, pady=10)
        self.password_field = tk.Entry(self.insert_user_section)
        self.password_field.grid(row=1, column=1, padx=10, pady=10)


        self.submit_button = tk.Button(self.insert_user_section, text='Submit',
                                       command=self.submit_button_functionality)
        self.submit_button.grid(row=1, column=2, padx=10, pady=10)


        self.fast_request_section = tk.Frame(self.section1, bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.fast_request_section.grid(row=0, column=1, padx=10, pady=10, sticky="nw")
        self.fast_requests_count_label = tk.Label(self.fast_request_section, text="Fast Wheel Requests Count",
                                                  fg="black")
        self.fast_requests_count_label.grid(row=6, column=0, padx=10, pady=10)

        self.fast_requests_count_field = tk.Entry(self.fast_request_section)
        self.fast_requests_count_field.grid(row=7, column=0, padx=10, pady=10)

        self.fast_requests_start_button = tk.Button(self.fast_request_section, text='Start',
                                                    command=lambda: self.fast_req_start())
        self.fast_requests_start_button.grid(row=7, column=1, padx=10, pady=10)

        self.fast_requests_stop_button = tk.Button(self.fast_request_section, text='Stop',
                                                   command=lambda: self.fast_req_stop())
        self.fast_requests_stop_button.grid(row=7, column=2, padx=10, pady=10)

        self.fast_pyramid_request_section = tk.Frame(self.section1, bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.fast_pyramid_request_section.grid(row=1, column=1, padx=10, pady=10, sticky="nw")
        self.fast_pyramid_requests_count_label = tk.Label(self.fast_pyramid_request_section, text="Fast Pyramid Requests Count",
                                                  fg="black")
        self.fast_pyramid_requests_count_label.grid(row=0, column=0, padx=10, pady=10)

        self.fast_pyramid_requests_count_field = tk.Entry(self.fast_pyramid_request_section)
        self.fast_pyramid_requests_count_field.grid(row=1, column=0, padx=10, pady=10)

        self.fast_pyramid_requests_start_button = tk.Button(self.fast_pyramid_request_section, text='Start',
                                                    command=lambda: self.fast_req_pyramid_start())
        self.fast_pyramid_requests_start_button.grid(row=1, column=1, padx=10, pady=10)

        self.fast_pyramid_requests_stop_button = tk.Button(self.fast_pyramid_request_section, text='Stop',
                                                   command=lambda: self.fast_req_pyramid_stop())
        self.fast_pyramid_requests_stop_button.grid(row=1, column=2, padx=10, pady=10)

        self.fast_slot_request_section = tk.Frame(self.section1, bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.fast_slot_request_section.grid(row=2, column=1, padx=10, pady=10, sticky="nw")
        self.fast_slot_requests_count_label = tk.Label(self.fast_slot_request_section,
                                                          text="Fast Slot Requests Count",
                                                          fg="black")
        self.fast_slot_requests_count_label.grid(row=0, column=0, padx=10, pady=10)

        self.fast_slot_requests_count_field = tk.Entry(self.fast_slot_request_section)
        self.fast_slot_requests_count_field.grid(row=1, column=0, padx=10, pady=10)

        self.fast_slot_requests_start_button = tk.Button(self.fast_slot_request_section, text='Start',
                                                            command=lambda: self.fast_req_slot_start())
        self.fast_slot_requests_start_button.grid(row=1, column=1, padx=10, pady=10)

        self.fast_slot_requests_stop_button = tk.Button(self.fast_slot_request_section, text='Stop',
                                                           command=lambda: self.fast_req_slot_stop())
        self.fast_slot_requests_stop_button.grid(row=1, column=2, padx=10, pady=10)




        self.log_window_section = tk.Frame(self.section1, bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.log_window_section.grid(row=0, column=3, columnspan=5, rowspan=10, padx=20, pady=1, sticky="nw")
        self.log_window = tk.Text(self.log_window_section, width=40, height=30)
        self.log_window.grid(row=0, column=0)
        # self.set_free_rows()
        self.user_table_section = tk.Frame(self.section1, bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.user_table_section.grid(row=1, column=0, rowspan=20, padx=10, pady=10, sticky="nw")
        self.canvas = tk.Canvas(self.user_table_section)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar = tk.Scrollbar(self.user_table_section, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.user_table_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.user_table_frame, anchor="nw")
        self.user_table_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.config(width=450, height=400)

        self.create_by_users()
        self.sync_db_button = tk.Button(self.section1, text='Sync User Chances',
                                        command=self.sync_db_functionality)
        self.sync_db_button.grid(row=3, column=1, padx=10, pady=10, sticky="nw")





    def create_by_users(self):
        db = Database()
        user_list = db.get_all_users_from_db()
        start_row = 0
        self.create_table(start_row, user_list)


    def fast_req_pyramid_start(self):
        if not self.fast_requests_pyramid:
            self.fast_requests_pyramid = Process(target=self.fast_requests_pyramid_start_functionality)
            self.fast_requests_pyramid.start()
            self.log_window.insert(tk.END, f'Fast requests  started !...\n')
        else:
            self.log_window.insert(tk.END, f'Fast requests already started push Stop after Start!...\n')

    def fast_req_pyramid_stop(self):
        if self.fast_requests_pyramid:
            self.fast_requests_pyramid.terminate()
            self.log_window.insert(tk.END, f'Fast requests  stoped !...\n')
            self.fast_requests_pyramid = None

    def fast_req_start(self):
        if not self.fast_requests:
            self.fast_requests = Process(target=self.fast_requests_start_functionality)
            self.fast_requests.start()
            self.log_window.insert(tk.END, f'Fast requests  started !...\n')
        else:
            self.log_window.insert(tk.END, f'Fast requests already started push Stop after Start!...\n')

    def fast_req_stop(self):
        if self.fast_requests:
            self.fast_requests.terminate()
            self.log_window.insert(tk.END, f'Fast requests  stoped !...\n')
            self.fast_requests = None

    def fast_requests_start_functionality(self):
        start = datetime.datetime.now()
        user_list = self.get_checkbox_values()
        user = choice(user_list)
        count = self.fast_requests_count_field.get()
        if count.isdigit():
            rec = Requests()
            rec.request_wheel_for_all(count=int(count), user_list=user_list)
        end = datetime.datetime.now()
        delta = end - start
        Logger.info(f'{delta}')
        self.log_window.insert(tk.END, f'Fast requests  duration is {delta}...\n')


    def fast_requests_slot_start_functionality(self):
        start = datetime.datetime.now()
        user_list = self.get_checkbox_values()
        user = choice(user_list)
        count = self.fast_slot_requests_count_field.get()
        if count.isdigit():
            rec = Requests()
            rec.request_slot_for_all(count=int(count), user_list=user_list)
        end = datetime.datetime.now()
        delta = end - start
        Logger.info(f'{delta}')
        self.log_window.insert(tk.END, f'Fast requests  duration is {delta}...\n')

    def fast_req_slot_start(self):
        if not self.fast_slot_requests:
            self.fast_slot_requests = Process(target=self.fast_requests_slot_start_functionality)
            self.fast_slot_requests.start()
            self.log_window.insert(tk.END, f'Fast requests  started !...\n')
        else:
            self.log_window.insert(tk.END, f'Fast requests already started push Stop after Start!...\n')

    def fast_req_slot_stop(self):
        if self.fast_slot_requests:
            self.fast_slot_requests.terminate()
            self.log_window.insert(tk.END, f'Fast requests  stoped !...\n')
            self.fast_slot_requests = None

    def fast_requests_pyramid_start_functionality(self):
        start = datetime.datetime.now()
        user_list = self.get_checkbox_values()
        user = choice(user_list)
        count = self.fast_pyramid_requests_count_field.get()
        if count.isdigit():
            rec = Requests()
            asyncio.run(rec.pyramid_fast(count=int(count), user=user, user_list=user_list))
        end = datetime.datetime.now()
        delta = end - start
        Logger.info(f'{delta}')
        self.log_window.insert(tk.END, f'Fast requests  duration is {delta}...\n')

    def sync_db_functionality(self):
        req = Requests()
        db = Database()
        for var, checkbox, user_id_header, chance_count_header, delete_button in self.rows:
            id, user_id, user_hash, chance = db.get_one_user(user_id_header.cget('text'))
            data = req.get_prize_chance_count(user_id=user_id,user_hash=user_hash)
            spinids = data.get("SpinIds")
            if spinids:
                chance_count = spinids.get('avialable_try')
                db.update_value_in_table(chance_count=chance_count,
                                         user_id=user_id_header.cget('text'))
                chance_count_header.config(text=chance_count)
        self.log_window.insert(tk.END, 'Users chances is synced!...\n')

    def submit_button_functionality(self):
        self.submit_proc = Thread(target=self.submit)
        self.submit_proc.start()

    def submit(self):
        start_column = 0
        chance_count = 0
        auth = Authorization()
        username = self.username_field.get()

        password = self.password_field.get()
        self.log_window.insert(tk.END, f'Authorization is started for {username} please wait several seconds....\n')
        auth.authorization(username=username, password=password)
        message, user_id, user_hash = auth.write_user_in_db()
        self.log_window.insert(tk.END, f'Status of adding user {username} is done....\n')
        if user_id:
            # db = Database()
            # db.insert_user(user_id=user_id)
            row = len(self.rows)
            var, checkbox, user_id_header, chance_count_header, delete_button = self.create_row(row,user_id,chance_count,start_column)
            self.rows.append([var, checkbox, user_id_header, chance_count_header, delete_button])

    def get_checkbox_values(self):
        self.true_row_list = []
        for row in self.rows:
            if row[0].get():
                self.true_row_list.append(row)
        return self.true_row_list

    def create_table(self, start_column, user_list):
        self.rows = []
        row = 0
        for id, user_id,user_hash, chance_count in user_list:
            var, checkbox, user_id_header, chance_count_header, delete_button = self.create_row(row,user_id,chance_count,start_column)
            self.rows.append([var, checkbox, user_id_header, chance_count_header, delete_button])
            row += 1

    def create_row(self, row, user_id, chance_count, start_column):
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(self.user_table_frame, text='', variable=var)
        checkbox.grid(row=row, column=start_column, padx=10, pady=10)
        user_id_header = tk.Label(self.user_table_frame, text=f"{user_id}", fg="black")
        user_id_header.grid(row=row, column=start_column + 1, padx=10, pady=10)
        chance_count_header = tk.Label(self.user_table_frame, text=f"{chance_count}", fg="black")
        chance_count_header.grid(row=row, column=start_column + 3, padx=10, pady=10)

        delete_button = tk.Button(self.user_table_frame, text='Delete',
                                  command=lambda row=row: self.delete_functionality(row))
        delete_button.grid(row=row, column=start_column + 4, padx=10, pady=10)
        return var, checkbox, user_id_header, chance_count_header, delete_button

    def add_functionality(self):
        pass

    def delete_functionality(self, row):
        db = Database()
        db.delete_user_from_table(id=self.rows[row][2].cget('text'))

        for widget in self.rows[row][1:]:
            widget.grid_remove()





if __name__ == '__main__':
    try:
        root = tk.Tk()
        app = MyApp(root)
        root.mainloop()
    except Exception as e:
        print(e)
