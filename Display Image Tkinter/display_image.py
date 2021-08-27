def DisplayImage(image_src, title):
    from tkinter import Tk, Label
    from tkinter.constants import TOP
    from PIL import Image, ImageTk
    from os import path

    BASE_DIR = path.abspath(path.dirname(__file__))
    root = Tk()

    window_height = root.winfo_screenheight()
    window_width = root.winfo_screenwidth()
    root_height = 580
    root_width = 580
   
    x_cord = int((window_width / 2) - (root_width / 2))
    y_cord = int((window_height / 2) - (root_height / 2)) - 15
   
    root.title("Thumbnail")
   
    root.geometry('{}x{}+{}+{}'.format(root_width, root_height, x_cord, y_cord))
    root.maxsize(root_width, root_height)
    root.minsize(root_width, root_height)
    root.resizable(False, False)

    root.iconbitmap(path.join(BASE_DIR, 'icon.ico'))
    root.configure(background='#333')

    image = Image.open(image_src)

    image_width = image.width
    image_height = image.height

    if image_height > 540:
        image_height = 540
    if image_width > 540:
        image_width = 540
    resized_image = image.resize((image_width, image_height), Image.ANTIALIAS)
    disp_image = ImageTk.PhotoImage(resized_image)
 
    label = Label(root, text="Thumbnail Image for {}".format(title), image=disp_image,font=('Halvatica', 10), fg='#000', bg='#fff', compound=TOP)
    label.configure(border=0)
    label.pack(padx=10, pady=10)

    root.mainloop()
DisplayImage("image.jpg", "Falling by Harry Styles")