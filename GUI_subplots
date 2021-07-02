import tkinter as tk
from tkinter.filedialog import askdirectory
from plotter import *
from animate import animate
import os

def choose_folder():
    folder = askdirectory()
    chosen_folder_label.config(text = folder)

def show():
    data = load_openpose(chosen_folder_label.cget("text"))
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("") # Title?
    if chosen_joint1.get() != "Select a Joint": plot_joint_over_time(list(JOINTS.keys())[list(JOINTS.values()).index(chosen_joint1.get())], data, axis=ax1)
    if chosen_joint2.get() != "Select a Joint": plot_joint_over_time(list(JOINTS.keys())[list(JOINTS.values()).index(chosen_joint2.get())], data, axis=ax2)
    if chosen_model3.get() != "Select a Model": animate(data, chosen_model3.get(), subplots=(fig, ax3))
    plt.show()

def save(): # Saves each plot individually
    if chosen_joint1.get() != "Select a Joint":
        plot_joint_over_time(
            list(JOINTS.keys())[list(JOINTS.values()).index(chosen_joint1.get())],
            load_openpose(chosen_folder_label.cget("text")),
            show=False,
            save=True,
            save_dir=os.path.join(os.path.split(chosen_folder_label.cget("text"))[0], os.path.split(os.path.split(
                chosen_folder_label.cget("text"))[0])[1] + "_" + chosen_joint1.get().lower().replace(" ", "_") + "_plot.png")
        )
    if chosen_joint2.get() != "Select a Joint":
        plot_joint_over_time(
            list(JOINTS.keys())[list(JOINTS.values()).index(chosen_joint2.get())],
            load_openpose(chosen_folder_label.cget("text")),
            show=False,
            save=True,
            save_dir=os.path.join(os.path.split(chosen_folder_label.cget("text"))[0], os.path.split(os.path.split(
                chosen_folder_label.cget("text"))[0])[1] + "_" + chosen_joint2.get().lower().replace(" ", "_") + "_plot.png")
        )
    if chosen_model3.get() != "Select a Model":
        animate(load_openpose(chosen_folder_label.cget("text")), chosen_model3.get(),
                save_path=os.path.join(os.path.split(chosen_folder_label.cget("text"))[0], os.path.split(os.path.split(chosen_folder_label.cget("text"))[0])[1] + "_animation.gif"))

def show_save():
    show()
    save()

# def save(): # Saves entire figure
#     data = load_openpose(chosen_folder_label.cget("text"))
#     fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
#     fig.suptitle("") # Title?
#     plot_joint_over_time(list(JOINTS.keys())[list(JOINTS.values()).index(chosen_joint1.get())], data, axis=ax1)
#     plot_joint_over_time(list(JOINTS.keys())[list(JOINTS.values()).index(chosen_joint2.get())], data, axis=ax2)
#     animate(data, chosen_model3.get(), subplots=(fig, ax3))
#     fig.savefig(os.path.join(os.path.split(chosen_folder_label.cget("text"))[0], os.path.split(os.path.split(chosen_folder_label.cget("text"))[0])[1] + "_plot.png"))

def set_joint_options1(model):
    if model == "Body":
        choose_joint_menu1['menu'].delete(0, 'end')
        for j in JOINTS.values():
            choose_joint_menu1['menu'].add_command(label=j, command=tk._setit(chosen_joint1, j))
    if model == "Hand":
        choose_joint_menu1['menu'].delete(0, 'end')
        choose_joint_menu1['menu'].add_command(label="Hand Joints Not Implemented Yet", command=tk._setit(chosen_joint1, "Hand Joints Not Implemented Yet"))
    chosen_joint1.set("Select a Joint")
def set_joint_options2(model):
    if model == "Body":
        choose_joint_menu2['menu'].delete(0, 'end')
        for j in JOINTS.values():
            choose_joint_menu2['menu'].add_command(label=j, command=tk._setit(chosen_joint2, j))
    if model == "Hand":
        choose_joint_menu2['menu'].delete(0, 'end')
        choose_joint_menu2['menu'].add_command(label="Hand Joints Not Implemented Yet", command=tk._setit(chosen_joint2, "Hand Joints Not Implemented Yet"))
    chosen_joint2.set("Select a Joint")

window = tk.Tk()
window.title("Openpose Plot Creator")
window.minsize(800, 600)

chosen_model1 = tk.StringVar()
chosen_model1.set("Select a Model")
chosen_model2 = tk.StringVar()
chosen_model2.set("Select a Model")
chosen_model3 = tk.StringVar()
chosen_model3.set("Select a Model")
chosen_joint1 = tk.StringVar()
chosen_joint1.set("Select a Joint")
chosen_joint2 = tk.StringVar()
chosen_joint2.set("Select a Joint")

choose_folder_frame = tk.Frame(borderwidth=2, relief="solid")
choose_folder_label = tk.Label(master=choose_folder_frame, text="Select the folder containing the JSON files", height = 3, padx=10)
choose_folder_button = tk.Button(master=choose_folder_frame, text="Choose", command=choose_folder)
chosen_folder_label = tk.Label(master=choose_folder_frame)
choose_folder_frame.pack(pady=10)
choose_folder_label.pack()
choose_folder_button.pack()
chosen_folder_label.pack()

# choose_joint_frame = tk.Frame(borderwidth=2, relief="solid")
# choose_joint_label = tk.Label(master=choose_joint_frame, text="Select the Model and Joint to Graph")
# choose_model_menu = tk.OptionMenu(choose_joint_frame, chosen_model, *["Body", "Hand"], command=set_joint_options)
# choose_joint_menu = tk.OptionMenu(choose_joint_frame, chosen_joint, "Choose a Model First")
# choose_joint_frame.pack(pady=10)
# choose_joint_label.pack(padx=5, pady=5)
# choose_model_menu.pack(padx=5, pady=5)
# choose_joint_menu.pack(padx=5, pady=5)

choose_joint_frame = tk.Frame(borderwidth=2, relief="solid")
choose_joint_frame.pack(pady=10)

choose_joint_frame1 = tk.Frame(master=choose_joint_frame, borderwidth=1, relief="solid")
choose_joint_label1 = tk.Label(master=choose_joint_frame1, text="Select the Model and Joint to Graph")
choose_model_menu1 = tk.OptionMenu(choose_joint_frame1, chosen_model1, *["Body", "Hand"], command=set_joint_options1)
choose_joint_menu1 = tk.OptionMenu(choose_joint_frame1, chosen_joint1, "Choose a Model First")
choose_joint_frame1.pack(padx=5, pady=10, side="left")
choose_joint_label1.pack(padx=5, pady=5, side="top")
choose_model_menu1.pack(padx=5, pady=5, side="top")
choose_joint_menu1.pack(padx=5, pady=5, side="top")

choose_joint_frame2 =tk.Frame(master=choose_joint_frame, borderwidth=1, relief="solid")
choose_joint_label2 = tk.Label(master=choose_joint_frame2, text="Select the Model and Joint to Graph")
choose_model_menu2 = tk.OptionMenu(choose_joint_frame2, chosen_model2, *["Body", "Hand"], command=set_joint_options2)
choose_joint_menu2 = tk.OptionMenu(choose_joint_frame2, chosen_joint2, "Choose a Model First")
choose_joint_frame2.pack(padx=5, pady=10, side="left")
choose_joint_label2.pack(padx=5, pady=5, side="top")
choose_model_menu2.pack(padx=5, pady=5, side="top")
choose_joint_menu2.pack(padx=5, pady=5, side="top")

choose_joint_frame3 =tk.Frame(master=choose_joint_frame, borderwidth=1, relief="solid")
choose_joint_label3 = tk.Label(master=choose_joint_frame3, text="Select the Model to Animate")
choose_model_menu3 = tk.OptionMenu(choose_joint_frame3, chosen_model3, *["Body", "Hand"])
choose_joint_frame3.pack(padx=5, pady=10, side="left")
choose_joint_label3.pack(padx=5, pady=5, side="top")
choose_model_menu3.pack(padx=5, pady=5, side="top")

plot_frame = tk.Frame(borderwidth=2, relief="solid")
plot_label = tk.Label(master=plot_frame, text="Plot options")
show_save_button = tk.Button(master=plot_frame, text="Show and Save", command=show_save)
save_button = tk.Button(master=plot_frame, text="Save", command=save)
show_button = tk.Button(master=plot_frame, text="Show", command=show)
plot_frame.pack(padx=5, pady=10)
plot_label.pack()
show_save_button.pack(padx=5, pady=5)
save_button.pack(padx=5, pady=5)
show_button.pack(padx=5, pady=5)

window.mainloop()
