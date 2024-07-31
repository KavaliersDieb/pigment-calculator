# I coded this for my bachelor thesis
# First "real" application

import tkinter as tk
from tkinter import ttk

# GUI specs
window = tk.Tk()
#window.geometry("1000x500")
window.title('Pigment Calculator')
#window.resizable(0, 0)

# Fuctions
def calculate():
    values = read_input()
    normalized_values = normalize(values)
    chla = calc_chla(normalized_values)
    caro = calc_caro(normalized_values, chla)

    chla_norm = chla_normalisation(normalized_values, chla)
    caro_norm = caro_normalisation(normalized_values, caro)

    #changing values in gui (insert results)
    Chla_amount.config(text=round(chla,6))
    Carotenoid_amount.config(text=round(caro,6))
    Chla_amount_normalised.config(text=round(chla_norm,6))
    Carotenoid_amount_normalised.config(text=round(caro_norm,6))

def read_input():
    try:     
        values = {
            "470":float(Extinction_470.get()),
            "665":float(Extinction_665.get()),
            "720":float(Extinction_720.get()),
            "750":float(Extinction_750.get()),
            "Harvest":float(Harvest_volume.get()),
            "Dilution":float(Dilution_factor.get())
        }
        return values
    except:
        print("------------------------------------")
        print("Error occured while reading the data")
        print("Use dots as comma!")
        print("Enter data in every field!")
        print("------------------------------------")

def normalize(dictonary):
    try:
        for wavelength in [470, 665, 720]:
            dictonary[str(wavelength)] = dictonary[str(wavelength)] * (1/dictonary["Harvest"]) * dictonary["Dilution"] # Check for harvest volume
        return dictonary
    except:
        print("-------------------------------")
        print("Error with normalizing the data")
        print("-------------------------------")
        values = {"470":0, "665":0, "720":0, "750":0, "Harvest":0, "Dilution":0}
        return values

def calc_chla(data) -> float: # Chla [μg/ml] = 12.9447 (A665 − A720) (Ritchie, 2006)
    try:
        return 12.9447 * (data["665"] - data["720"])
    except:
        print("-------------------------------------------------------")
        print("Error occured while calculating the Chlorophyll contend")
        print("-------------------------------------------------------")

def calc_caro(data, chlorophyll) -> float: # Carotenoids [μg/ml] = [1,000 (A470 − A720) − 2.86 (Chla [μg/ml])] / 221 (Wellburn, 1994).
    try:
        return (1000*(data["470"] - data["720"]) - (2.86 * chlorophyll) )/221
    except:
        print("--------------------------------------------------")
        print("Error occured while calculating Carotenoid contend")
        print("--------------------------------------------------")

def chla_normalisation(data, chlorophyll):
    try:
        return chlorophyll/data["750"]
    except:
        print("---------------------------------------------------")
        print("Error occured while normalizing Chlorophyll contend")
        print("---------------------------------------------------")

def caro_normalisation(data, carotenoid):
    try:
        return carotenoid/data["750"]
    except:
        print("--------------------------------------------------")
        print("Error occured while normalizing Carotenoid contend")
        print("--------------------------------------------------")

# 470 nm, 665 nm and 720 nm
Label_explanation = ttk.Label(window, text="Insert measured values:")
Label_nm1 = ttk.Label(window, text="470 nm (measured)")
Label_nm2 = ttk.Label(window, text="665 nm (measured)")
Label_nm3 = ttk.Label(window, text="720 nm (measured)")
Label_nm4 = ttk.Label(window, text="750 nm (calculated)")
Label_explanation.grid(column=0, row=0, padx=5, pady=5)
Label_nm1.grid(column=0, row=3, padx=5, pady=5)
Label_nm2.grid(column=1, row=3, padx=5, pady=5)
Label_nm3.grid(column=2, row=3, padx=5, pady=5)
Label_nm4.grid(column=3, row=3, padx=5, pady=5)

Extinction_470 = ttk.Entry(window)
Extinction_665 = ttk.Entry(window)
Extinction_720 = ttk.Entry(window)
Extinction_750 = ttk.Entry(window)
Extinction_470.grid(column=0, row=4, padx=5, pady=5)
Extinction_665.grid(column=1, row=4, padx=5, pady=5)
Extinction_720.grid(column=2, row=4, padx=5, pady=5)
Extinction_750.grid(column=3, row=4, padx=5, pady=5)
Extinction_750.insert(0, "1")


# Parameters
Label_harvest = ttk.Label(window, text="Amount of cells \nharvested [ml]:")
Label_harvest.grid(column=0, row=1, padx=5, pady=5)
Harvest_volume = ttk.Entry(window)
Harvest_volume.grid(column=1, row=1, padx=5, pady=5)

Dilution_label = ttk.Label(window, text="Dilution factor \nof supernant:")
Dilution_label.grid(column=0, row=2, padx=5, pady=5)
Dilution_factor = ttk.Entry(window)
Dilution_factor.grid(column=1, row=2, padx=5, pady=5)
Harvest_example = ttk.Label(window, text="Example: Dilution 1:10")
Harvest_example.grid(column=2, row=2, padx=5, pady=5)
Harvest_example_2 = ttk.Label(window, text="-> Insert: 10")
Harvest_example_2.grid(column=3, row=2, padx=5, pady=5, sticky=tk.W)

# Button
Calc_button = ttk.Button(window, text="Do the magic", command=calculate)
Calc_button.grid(column=0, row=5, padx=5, pady=5)

# 750 explanation label
info_750 = ttk.Label(window, text="For OD-Normalisation")
info_750.grid(column=3, row=5, padx=5, pady=5)

# Outputs
Chla_Label = ttk.Label(window, text="Chlorophyll [μg/ml]:")
Carotenoid_Label = ttk.Label(window, text="Carotenoid [μg/ml]:")
Chla_normalised = ttk.Label(window, text="Chl a [μg/ml/OD]:")
Carotenoid_normalised = ttk.Label(window, text="Carotenoid \n[μg/ml/OD]:")
Chla_Label.grid(column=0, row=6, padx=5, pady=5)
Carotenoid_Label.grid(column=0, row=7, padx=5, pady=5)
Chla_normalised.grid(column=0, row=8, padx=5, pady=5)
Carotenoid_normalised.grid(column=0, row=9, padx=5, pady=5)

Chla_amount = ttk.Label(window, text="0")
Carotenoid_amount = ttk.Label(window, text="0")
Chla_amount_normalised = ttk.Label(window, text="0")
Carotenoid_amount_normalised = ttk.Label(window, text="0")
Chla_amount.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)
Carotenoid_amount.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)
Chla_amount_normalised.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5)
Carotenoid_amount_normalised.grid(column=1, row=9, sticky=tk.W, padx=5, pady=5)


#mainloop
window.mainloop()