import tkinter as tk
import requests

class View:
    def __init__(self, root=tk.Tk()):
        self.root = root
        self.bc_image = tk.PhotoImage(file='./background.png')
        self.start_parameters()
        self.background()
        self.background_image()
        self.upper_frame()
        self.lower_frame()
        self.label1()
        self.label2()
        self.entry1()
        self.button1()
        root.mainloop()

    def get_api(self, city):
    #api_key = '2dfea41a0246fba09ccff01cd611e07a'
        try:
            url = 'https://api.openweathermap.org/data/2.5/weather'
            response = requests.get(url,
                params={
                    "q": city,
                    "appid": '2dfea41a0246fba09ccff01cd611e07a',
                    "units": "metric"
                    }).json()
            temperature = response['main']['temp']
            description = response['weather'][0]['description']
            name_city = response['name']
            pressure = response['main']['pressure']
            humidity = response['main']['humidity']
            speed = response['wind']['speed']
            country = response['sys']['country']

            self.label_1['text'] = f'City: {name_city}, {country}\n\n Temperature: {temperature} \u00B0C\n\nWeather conditions: {description}\n\nPressure: {pressure} hPa\n\nHumidity: {humidity} %\n\nSpeed of wind: {speed} m/s'
        except:
            self.label_1['text'] = 'Sorry, given place is not correct!'

    def start_parameters(self):
        self.root.geometry('650x500')
        self.root.resizable(False, False)

    def background_image(self):
        self.bc_label = tk.Label(self.root, image=self.bc_image)
        self.bc_label.place(x=0, y=0, relwidth=1, relheight=1)
        return self.bc_label

    @staticmethod
    def background():
        canvas = tk.Canvas(height=650, width=500)
        canvas.pack()

    def entry1(self):
        self.entry_1 = tk.Entry(self.frame_up, bg='white', justify='center')
        self.entry_1.place(relx=0.05, rely=0.1, relheight=0.8, relwidth=0.65)

    def button1(self):
        button_1 = tk.Button(self.frame_up, text="Check", font=('Segoe UI',10), command=lambda: self.get_api(self.entry_1.get()))
        button_1.place(relx=0.75, rely=0.1, relheight=0.8, relwidth=0.2)

    def label1(self):
        self.label_1 = tk.Label(self.frame_low, bg='#80bfff', font=('Segoe UI',10))
        self.label_1.place(relx=0.05, rely=0.075, relheight=0.85, relwidth=0.9)

    def label2(self):
        self.label_2 = tk.Label(self.frame_low, bg='#ffff66', text='Weather data provided by: OpenWeather.org', font=('Segoe UI',10), anchor='w')
        self.label_2.place(relx=0.45, rely=0.95, relheight=0.05, relwidth=0.9)

    def upper_frame(self):
        self.frame_up = tk.Frame(self.root, bg='#ffff66')
        self.frame_up.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    def lower_frame(self):
        self.frame_low = tk.Frame(self.root, bg='#ffff66')
        self.frame_low.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.75)

if __name__ == '__main__':
    view = View()


    # def get_api(city):
    #     #api_key = '2dfea41a0246fba09ccff01cd611e07a'
    #     url = 'https://api.openweathermap.org/data/2.5/weather'temperature = response['main']['temp']
    #     # description = response['weather'][0]['description']
    #     # name_city = response['name']
    #     response = requests.get(url,
    #         params={
    #             "q": city,
    #             "appid": '2dfea41a0246fba09ccff01cd611e07a',
    #             "units": "metric",
    #         }).json()
    #     #
    #     # print(f'{temperature}\u00B0C')
    #     print()
    #
    # get_api('boston')