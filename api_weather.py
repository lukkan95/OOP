import tkinter as tk


class View:
    def __init__(self, root=tk.Tk()):
        self.root = root
        self.start_parameters()
        self.background()
        self.frame1()
        self.entry1()
        self.button1()
        root.mainloop()

    def start_parameters(self):
        self.root.geometry('650x500')
        self.root.resizable(False, False)

    @staticmethod
    def background():
        canvas = tk.Canvas(height=400, width=400)
        canvas.place(relx=0.3, rely=0.3)

    def entry1(self):
        entry_1 = tk.Entry(self.frame1(), bg='green')
        entry_1.place(relx=0.5, rely=0.2, relheight=0.1, relwidth=0.2)

    def button1(self):
        button_1 = tk.Button(self.frame1(), text="Confirm", font=('Segoe UI',10))
        button_1.place(relx=0.2, rely=0.5, relheight=0.1, relwidth=0.2)

    def frame1(self):
        frame = tk.Frame(self.root, bg='#ffff66')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

if __name__ == '__main__':
    view = View()

# import requests
#
# def get_api():
#     url = 'https://www.olx.pl/api/open/oauth/token'
#     response = requests.get(url,
#         params={
#             "grant_type": "",
#             "client_id": "201764",
#             "client_secret": "xZi5H3rqE22FGidUzPnK52R4lqKdYLYGfRpCKqRwJr3GuubJ",
#             "scope": "v2 read write"
#         }).json()
#     print(response)
#
# get_api()