import customtkinter
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x500")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="Crop your image", font=("Roboto", 20, "underline"))
label.pack(pady=20)


def choose_file():
    global filename
    filename = askopenfilename()
    img = ImageTk.Image.open(filename)
    img = customtkinter.CTkImage(dark_image=img, size=(img.width // 2, img.height // 2))
    panel = customtkinter.CTkLabel(root, image=img, text="")
    panel.pack(side="bottom", fill="both", expand="yes")



image_choose = customtkinter.CTkButton(master=frame, text="Choose File", command=choose_file)
image_choose.pack(pady=20, padx=15)

entry_frame = customtkinter.CTkFrame(master=frame)
entry_frame.pack(pady=20, padx=15, fill="x")

width_config = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Width")
width_config.pack(side="left", padx=(65, 0))
x = customtkinter.CTkLabel(master=entry_frame, text="x", font=("Roboto", 15))
x.pack(side="left", padx=10)
height_config = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Height")
height_config.pack(side="left", fill="both", padx=0)


def crop_image():
    image_path = filename
    image = Image.open(image_path)
    new_size = (int(width_config.get()), int(height_config.get()))
    resized_image = image.resize(new_size, Image.LANCZOS)

    resized_image_path = askopenfilename()
    resized_image.save(resized_image_path)


run_button = customtkinter.CTkButton(master=frame, text="Crop", command=crop_image)
run_button.pack(pady=10, padx=20)


root.mainloop()
