import tkinter as tk
from tkinter import messagebox


def check_login(name = "", phone = ""):
    if name == "" or phone == "":
        name = entry_name.get()
        phone = entry_phone.get()

    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Ошибка", "Имя должно содержать только буквы!")
        return False

    if not name or not phone:
        messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля!")
        return False

    messagebox.showinfo("Успех", f"Добро пожаловать, {name}!")

    return True

root = tk.Tk()
root.title("Форма входа")
root.geometry("500x350")
root.configure(bg="#f0f0f0")

label_title = tk.Label(root, text="Форма входа", font=("Arial", 14, "bold"), bg="#f0f0f0")
label_title.pack(pady=10)

label_name = tk.Label(root, text="Имя", bg="#f0f0f0", anchor="w")
label_name.pack(fill="x", padx=20)
entry_name = tk.Entry(root)
entry_name.pack(fill="x", padx=20, pady=5)

label_phone = tk.Label(root, text="Номер телефона", bg="#f0f0f0", anchor="w")
label_phone.pack(fill="x", padx=20)
entry_phone = tk.Entry(root)
entry_phone.pack(fill="x", padx=20, pady=5)

btn_login = tk.Button(root, text="Вход", bg="#7c4dff", fg="white", font=("Arial", 10, "bold"), command=check_login)
btn_login.pack(pady=20, fill="x", padx=20)

# if __name__ == "__main__":
#     root.mainloop()

