import tkinter as tk

from main import call_api

window = tk.Tk()


def _update_data():
    global total_infections, total_recovered, total_death, last_updated
    data = call_api()
    if data:
        total_infections.config(text=f"Total Infections: {data.get('total_infections')}")
        total_recovered.config(text=f"Total Recovered: {data.get('total_recovered')}")
        total_death.config(text=f"Total Deaths: {data.get('total_deaths')}")
        last_updated.config(text=f"Last Updated: {data.get('last_updated')}")


window.geometry("400x250")
greeting = tk.Label(text="Covid Report")
total_infections = tk.Label(text="Total Infections: 0")
total_recovered = tk.Label(text=f"Total Recovered: 0")
total_death = tk.Label(text="Total Deaths: 0")
last_updated = tk.Label(text="Last Updated: N/A")
data_courtesy = tk.Label(text='Data Courtesy: COVID-19 statistics api by Axisbits')

greeting.pack()
total_infections.pack()
total_recovered.pack()
total_death.pack()
last_updated.pack()

button = tk.Button(
    text="Update Data",
    width=10,
    height=1,
    bg="blue",
    fg="yellow",
    command=_update_data
)
button.pack()
data_courtesy.pack()
window.mainloop()
