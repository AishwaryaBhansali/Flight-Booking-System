import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from reportlab.pdfgen import canvas 

class Flight:
    def __init__(self,root):
        self.root = root
        self.root.title("Flight Booking System")
        self.root.geometry("700x600")

        #Title
        title1 = tk.Label(root, text="Flight Booking System", font=("Helvetica", 16, "bold"))
        title1.pack(pady=20)

        #frame
        frame = tk.Frame(root)
        frame.pack(pady=10)

        #variables
        self.flight_times = {
            "AirIndia" : {"Mumbai" : 2, "Pune" : 2, "Chennai" : 2},
            "SpiceJet" : {"Mumbai" : 2, "Pune" : 2, "Chennai" : 2},
            "IndiGo" : {"Mumbai" : 2, "Pune" : 2, "Chennai" : 2},
        }

        self.sd = {
            "Mumbai" : ["Bangalore", "Ooty", "Bihar"],
            "Pune" : ["Bangalore", "Ooty", "Bihar"],
            "Chennai" : ["Bangalore", "Ooty", "Bihar"],
        }

        #flight drop down names
        tk.Label(frame, text = "Flight Name : ").grid(row=0, column=0, padx=10, pady=5)
        self.flight_name = ttk.Combobox(frame, value = list(self.flight_times.keys()))
        self.flight_name.grid(row=0, column=1, padx=10, pady=5)
        self.flight_name.set("Select Flight Name ")
        #self.flight_name.bind("<<ComboboxSelected>>", update_dtime)

        #source drop down names
        tk.Label(frame, text = "Source : ").grid(row=1, column=0, padx=10, pady=5)
        self.source = ttk.Combobox(frame, value = ["Mumbai", "Pune", "Chennai"])
        self.source.grid(row=1, column=1, padx=10, pady=5)
        self.source.set("Select Source ")
        #self.flight_name.bind("<<ComboboxSelected>>", update_dtime)

        #dest drop down names
        tk.Label(frame, text = "Destination : ").grid(row=2, column=0, padx=10, pady=5)
        self.dest = ttk.Combobox(frame, value = ["Bangalore", "Ooty", "Bihar"])
        self.dest.grid(row=2, column=1, padx=10, pady=5)

        #departure date
        tk.Label(frame, text = "Departure date : ").grid(row=3, column=0, padx=10, pady=5)
        self.ddate = DateEntry(frame, datepattern='yyyy-mm-dd')
        self.ddate.grid(row=3, column=1, padx=10, pady=5)

        #departure time
        tk.Label(frame, text = "Departure Time : ").grid(row=4, column=0, padx=10, pady=5)
        dtimes = [f"{hour} : 00 AM" if hour < 12 else f"{hour} - 12 : 00 PM" for hour in range(7,20)]
        self.dtime = ttk.Combobox(frame, value = dtimes)
        self.dtime.grid(row=4, column=1, padx=10, pady=5)
        self.dtime.bind("<<ComboboxSelected>>")      

        
        #customer details
        tk.Label(frame, text = "Customer Name : ").grid(row=5, column=0, padx=10, pady=5)
        self.name = tk.Entry(frame)
        self.name.grid(row=5, column=1, padx=10, pady=5)
        
        #age
        tk.Label(frame, text = "Age : ").grid(row=6, column=0, padx=10, pady=5)
        self.age = tk.Entry(frame)
        self.age.grid(row=6, column=1, padx=10, pady=5)

        #age
        tk.Label(frame, text = "Contact No : ").grid(row=7, column=0, padx=10, pady=5)
        self.no = tk.Entry(frame)
        self.no.grid(row=7, column=1, padx=10, pady=5)

        #gender
        tk.Label(frame, text = "Gender : ").grid(row=8, column=0, padx=10, pady=5)
        self.gender = tk.StringVar(value="Male")
        gframe = tk.Frame(frame)
        gframe.grid(row=8, column=1, padx=10, pady=5)
        tk.Radiobutton(gframe, text="Male", variable=self.gender, value="Male").pack(side="left")
        tk.Radiobutton(gframe, text="Female", variable=self.gender, value="Female").pack(side="left")

        #number of seats
        tk.Label(frame, text = "Number of Seats : ").grid(row=9, column=0, padx=10, pady=5)
        self.seats = tk.Entry(frame)
        self.seats.grid(row=9, column=1, padx=10, pady=5)

        #class
        tk.Label(frame, text = "Class : ").grid(row=10, column=0, padx=10, pady=5)
        self.sclass = ttk.Combobox(frame, value = ["First Class", "Business Class", "Economy Class"])
        self.sclass.grid(row=10, column=1, padx=10, pady=5)

        #seat place
        tk.Label(frame, text = "Seat Place(Window/ Aisle) : ").grid(row=11, column=0, padx=10, pady=5)
        self.no = tk.Entry(frame)
        self.no.grid(row=11, column=1, padx=10, pady=5)
        
        #buttons
        buttonf = tk.Frame(root)
        buttonf.pack(pady=10)
        tk.Button(buttonf, text="Calculate Total Cost",command = self.calc, font=("Helvetica",12,"bold")).pack(side="left", padx=10)
        tk.Button(buttonf, text="Download Receipt",command=self.download, font=("Helvetica",12,"bold")).pack(side="left")

        #total
        self.total = tk.Label(root, text = "Total Amount is : 0 INR", font=("Helvetica", 12, "bold"))
        self.total.pack(pady=10)

    def calc(self):
        try:
            no_of_seats = int(self.seats.get())
            cost_per_seat = 5000
            total_cost = no_of_seats * cost_per_seat
            self.total.config(text=f"Total Amount is : {total_cost} INR")
        except ValueError:
            messagebox.showerror("Invalid Input.")

    def download(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", ".*pdf")])
        if not file_path:
            return

        pdf = canvas.Canvas(file_path)
        pdf.setTitle("Flight Booking System")
        pdf.setFont("Helvetica", 16)
        pdf.drawString(100, 750, "Flight Booking Receipt")

        pdf.setFont("Helvetica",12)
        pdf.drawString(100, 720, f"Customer Name  : {self.name.get()}")
        pdf.drawString(100, 700, f"Age  : {self.age.get()}")
        pdf.drawString(100, 680, f"Gender  : {self.gender.get()}")
        pdf.drawString(100, 660, f"Contact No  : {self.no.get()}")
        pdf.drawString(100, 640, f"Flight Name  : {self.flight_name.get()}")
        pdf.drawString(100, 620, f"Source  : {self.source.get()}")
        pdf.drawString(100, 600, f"Destination  : {self.dest.get()}")
        pdf.drawString(100, 580, f"Departure Date  : {self.ddate.get()}")
        pdf.drawString(100, 560, f"Departure Time  : {self.dtime.get()}")
        pdf.drawString(100, 540, f"No of seats  : {self.seats.get()}")
        pdf.drawString(100, 520, self.total.cget("text"))

        pdf.drawString(100, 500, "Thank you for booking with us !")
        pdf.save()

        messagebox.showinfo(value="Success, Receipt has been downloaded successfully.")

if __name__=="__main__":
    root = tk.Tk()
    obj = Flight(root)
    root.mainloop()