# This code is poorly set out.

# ============================================================================
# ============================================================================
# Made by: https://github.com/OzonePrograms/
# Made by: https://github.com/OzonePrograms/
# Made by: https://github.com/OzonePrograms/
# ============================================================================
# ============================================================================


from tkinter import *
import sys
import os
import glob


def exit_view_notes():
    view_notes_screen.destroy()
    notes_app()


def exit_create_notes():
    create_notes_screen.destroy()
    notes_app()


def ok_note_saved_screen():
    note_saved_screen.destroy()
    create_notes_screen.destroy()

    notes_app()


def ok_note_saved_error():
    note_saved_error_screen.destroy()


def note_saved_error():
    global note_saved_error_screen
    note_saved_error_screen = Toplevel(create_notes_screen)
    note_saved_error_screen.title("There was an error.")
    note_saved_error_screen.geometry("450x110")
    note_saved_error_screen.resizable(0, 0)

    Label(note_saved_error_screen, text="There was an error, try again!", bg="grey", width="450", height="2").pack()
    Label(note_saved_error_screen, text="").pack()
    Button(note_saved_error_screen, text="OK", command=ok_note_saved_error).pack()


def note_saved():
    global note_saved_screen
    note_saved_screen = Toplevel(create_notes_screen)
    note_saved_screen.title("Saved!")
    note_saved_screen.geometry("400x100")
    note_saved_screen.resizable(0, 0)

    Label(note_saved_screen, text="Saved!", bg="grey", width="400", height="2").pack()
    Label(note_saved_screen, text="").pack()
    Button(note_saved_screen, text="OK", command=ok_note_saved_screen).pack()


def save_notes():
    filename = raw_filename.get()
    notes = raw_notes.get()

    if filename == "" or notes == "":
        note_saved_error()
    else:
        data = open(filename + ".txt", "w")
        data.write(notes)
        data.close()

        note_saved()

    create_notes_entry1.delete(0, END)
    create_notes_entry2.delete(0, END)


def create_notes():
    notes_program.destroy()

    global create_notes_screen
    create_notes_screen = Tk()
    create_notes_screen.title("Create Notes")
    create_notes_screen.geometry("500x500")
    create_notes_screen.resizable(False, False)

    global create_notes_entry1
    global create_notes_entry2
    global raw_filename
    global raw_notes
    raw_filename = StringVar()
    raw_notes = StringVar()

    Label(create_notes_screen, text="Enter a filename for your note:", bg="grey", width="500", height="2").pack()
    Label(create_notes_screen, text="").pack()
    create_notes_entry1 = Entry(create_notes_screen, textvariable=raw_filename)
    create_notes_entry1.pack()
    Label(create_notes_screen, text="").pack()
    Label(create_notes_screen, text="Enter your notes for the file:", bg="grey", width="500", height="2").pack()
    Label(create_notes_screen, text="").pack()
    create_notes_entry2 = Entry(create_notes_screen, textvariable=raw_notes, width="75")
    create_notes_entry2.pack()
    Label(create_notes_screen, text="").pack()
    Button(create_notes_screen, text="Save", command=save_notes).pack()

    Button(create_notes_screen, text=">> Back <<", command=exit_create_notes).place(x=420, y=470)


def ok_show_notes_error():
    show_notes_error.destroy()


def view_notes_error():
    global show_notes_error
    show_notes_error = Tk()
    show_notes_error.title("There was an error.")
    show_notes_error.geometry("450x110")
    show_notes_error.resizable(0, 0)

    Label(show_notes_error, text="File not found, try again! (Make sure your include (.txt) in the filename!)", bg="grey", width="450", height="2").pack()
    Label(show_notes_error, text="").pack()
    Button(show_notes_error, text="OK", command=ok_show_notes_error).pack()


def exit_show_notes():
    show_notes.destroy()
    notes_app()


def view_notes_cmd():
    filename1 = raw_filename1.get()

    view_entry.delete(0, END)

    if filename1 in list_of_notes:
        data1 = open(filename1, "r")
        data1 = data1.read()

        view_notes_screen.destroy()

        global show_notes
        show_notes = Tk()
        show_notes.title("Viewing " + filename1)
        show_notes.geometry("500x300")
        show_notes.resizable(0, 0)

        Label(show_notes, text=data1, bg="grey", width="500", height="2").pack()
        Label(show_notes, text="").pack()
        Label(show_notes, text=list_of_notes, bg="SpringGreen2", width="500", height="1").pack()

        Button(show_notes, text=">> Back <<", command=exit_show_notes).place(x=420, y=270)
    else:
        view_notes_error()


def view_notes():
    notes_program.destroy()

    global view_notes_screen
    view_notes_screen = Tk()
    view_notes_screen.title("View Notes")
    view_notes_screen.geometry("500x500")
    view_notes_screen.resizable(0, 0)

    global list_of_notes
    list_of_notes = []
    os.listdir()
    for file in glob.glob("*.txt"):
        list_of_notes.append(file)

    Label(view_notes_screen, text="Please use one of the filenames below:", bg="grey", width="500", height="2").pack()
    Label(view_notes_screen, text="").pack()
    if len(list_of_notes) >= 1:
        Label(view_notes_screen, text=list_of_notes, bg="green2", width="500", height="1").pack()
    else:
        Label(view_notes_screen, text="Nothing to View", bg="red2", width="500", height="1").pack()
    Label(view_notes_screen, text="").pack()

    global raw_filename1
    global view_entry
    raw_filename1 = StringVar()

    view_entry = Entry(view_notes_screen, textvariable=raw_filename1)
    view_entry.pack()
    Label(view_notes_screen, text="").pack()
    Button(view_notes_screen, text="View", command=view_notes_cmd).pack()
    Label(view_notes_screen, text="").pack()

    Button(view_notes_screen, text=">> Back <<", command=exit_view_notes).place(x=420, y=470)


def exit_delete_notes_screen():
    delete_notes_screen.destroy()
    notes_app()


def ok_del_note_error():
    del_note_error.destroy()


def del_file_error():
    global del_note_error
    del_note_error = Toplevel(delete_notes_screen)
    del_note_error.title("There was an error.")
    del_note_error.geometry("450x110")
    del_note_error.resizable(0, 0)

    Label(del_note_error, text="File not found, try again! (Make sure your include (.txt) in the filename!)", bg="grey", width="450", height="2").pack()
    Label(del_note_error, text="").pack()
    Button(del_note_error, text="OK", command=ok_del_note_error).pack()


def ok_file_deleted():
    file_deleted_box.destroy()
    delete_notes_screen.destroy()
    notes_app()


def file_deleted():
    global file_deleted_box
    file_deleted_box = Toplevel(delete_notes_screen)
    file_deleted_box.title("File " + file_to_del + " deleted!")
    file_deleted_box.geometry("250x110")
    file_deleted_box.resizable(0, 0)

    Label(file_deleted_box, text="File Deleted!", bg="grey", width="250", height="2").pack()
    Label(file_deleted_box, text="").pack()
    Button(file_deleted_box, text="OK", command=ok_file_deleted).pack()


def del_file():
    global file_to_del
    file_to_del = filename_del.get()

    delete_entry.delete(0, END)

    if file_to_del in list_of_notes:
        os.remove(file_to_del)
        file_deleted()
    else:
        del_file_error()


def delete_notes():
    notes_program.destroy()

    global delete_notes_screen
    delete_notes_screen = Tk()
    delete_notes_screen.title("Delete Notes")
    delete_notes_screen.geometry("500x500")
    delete_notes_screen.resizable(0, 0)

    global filename_del
    global delete_entry
    filename_del = StringVar()

    global list_of_notes
    list_of_notes = []
    os.listdir()
    for file in glob.glob("*.txt"):
        list_of_notes.append(file)

    Label(delete_notes_screen, text="Enter filename to delete:", bg="grey", width="500", height="2").pack()
    Label(delete_notes_screen, text="").pack()
    if len(list_of_notes) >= 1:
        Label(delete_notes_screen, text=list_of_notes, bg="green2", width="500", height="1").pack()
    else:
        Label(delete_notes_screen, text="Nothing to Delete!", bg="red2", width="500", height="1").pack()
    Label(delete_notes_screen, text="").pack()
    delete_entry = Entry(delete_notes_screen, textvariable=filename_del)
    delete_entry.pack()
    Label(delete_notes_screen, text="").pack()
    Button(delete_notes_screen, text="Delete", command=del_file).pack()

    Button(delete_notes_screen, text=">> Back <<", command=exit_delete_notes_screen).place(x=420, y=470)


def notes_app():
    global notes_program
    notes_program = Tk()
    notes_program.title("Notes 2.0")
    notes_program.geometry("500x500")
    notes_program.resizable(0, 0)

    Label(notes_program, text="Welcome to Notes 2.0!", bg="grey", width="500", height="2").pack()
    Label(notes_program, text="").pack()
    Button(notes_program, text="Create Notes", command=create_notes, width="65").pack()
    Label(notes_program, text="").pack()
    Button(notes_program, text="View Notes", command=view_notes, width="65").pack()
    Label(notes_program, text="").pack()
    Button(notes_program, text="Delete Notes", command=delete_notes, width="65").pack()

    Button(notes_program, text=">> Exit <<", command=exit_notes).place(x=430, y=470)


def exit_notes():
    notes_program.destroy()
    sys.exit()


def exit_main():
    main.destroy()
    sys.exit()


def exit_register():
    register_screen.destroy()
    main_screen()


def exit_login():
    login_screen.destroy()
    main_screen()


def ok_register_success():
    register_success_box.destroy()
    exit_register()


def ok_user_not_found_box():
    user_not_found_box.destroy()


def ok_password_not_recognised_box():
    password_not_recognised_box.destroy()


def ok_login_success_box():
    login_success_box.destroy()
    login_screen.destroy()
    notes_app()


def ok_register_error_box():
    register_error_box.destroy()


def register_error():
    register_entry1.delete(0, END)
    register_entry2.delete(0, END)

    global register_error_box
    register_error_box = Toplevel(register_screen)
    register_error_box.title("Error has occurred.")
    register_error_box.geometry("450x150")
    register_error_box.resizable(0, 0)

    Label(register_error_box, text="There was an error, try again!", bg="grey", width="450", height="2").pack()
    Label(register_error_box, text="").pack()
    Button(register_error_box, text="OK", command=ok_register_error_box).pack()


def login_success():
    global login_success_box
    login_success_box = Toplevel(login_screen)
    login_success_box.title("Success")
    login_success_box.geometry("400x100")
    login_success_box.resizable(0, 0)

    Label(login_success_box, text="Login Successful.", bg="grey", width="400", height="2").pack()
    Label(login_success_box, text="").pack()
    Button(login_success_box, text="OK", command=ok_login_success_box).pack()


def password_not_recognised():
    global password_not_recognised_box
    password_not_recognised_box = Toplevel(login_screen)
    password_not_recognised_box.title("Password not Recognised.")
    password_not_recognised_box.geometry("400x100")
    password_not_recognised_box.resizable(0, 0)

    Label(password_not_recognised_box, text="Password Error.", bg="grey", width="400", height="2").pack()
    Label(password_not_recognised_box, text="").pack()
    Button(password_not_recognised_box, text="OK", command=ok_password_not_recognised_box).pack()


def user_not_found():
    global user_not_found_box
    user_not_found_box = Toplevel(login_screen)
    user_not_found_box.title("Username not found.")
    user_not_found_box.geometry("400x100")
    user_not_found_box.resizable(False, False)

    Label(user_not_found_box, text="Username not found.", bg="grey", width="400", height="2").pack()
    Label(user_not_found_box, text="").pack()
    Button(user_not_found_box, text="OK", command=ok_user_not_found_box).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    login_entry1.delete(0, END)
    login_entry2.delete(0, END)

    global loginfile
    loginfile = username1 + ".login"

    global list_of_logins
    list_of_logins = os.listdir()
    if loginfile in list_of_logins:
        file1 = open(loginfile, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()


def login():
    main.destroy()

    global login_screen
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.resizable(False, False)

    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global login_entry1
    global login_entry2

    Label(login_screen, text="Username:", bg="grey", width="300", height="1").pack()
    Label(login_screen, text="").pack()
    login_entry1 = Entry(login_screen, textvariable=username_verify)
    login_entry1.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password:", bg="grey", width="300", height="1").pack()
    Label(login_screen, text="").pack()
    login_entry2 = Entry(login_screen, textvariable=password_verify)
    login_entry2.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width="10", height="1", command=login_verify).pack()

    Button(login_screen, text=">> Back <<", command=exit_login).place(x=220, y=220)


def register_user():
    username_info = username.get()
    password_info = password.get()

    if username_info == "" or password_info == "":
        register_error()
    else:
        login_file = open(username_info + ".login", "w")
        login_file.write(username_info + "\n")
        login_file.write(password_info)
        login_file.close()

        register_entry1.delete(0, END)
        register_entry2.delete(0, END)

        global register_success_box
        register_success_box = Toplevel(register_screen)
        register_success_box.title("Registration Success")
        register_success_box.geometry("200x150")
        register_success_box.resizable(False, False)

        Label(register_success_box, text="Registration Successful!", bg="grey", width="200", height="2").pack()
        Label(register_success_box, text="").pack()
        Button(register_success_box, text="OK", command=ok_register_success).pack()


def register():
    main.destroy()

    global register_screen
    register_screen = Tk()
    register_screen.title("Register")
    register_screen.geometry("300x275")
    register_screen.resizable(False, False)

    global register_entry1
    global register_entry2
    global username
    global password
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Enter a Username:", bg="grey", width="300").pack()
    Label(register_screen, text="").pack()
    register_entry1 = Entry(register_screen, textvariable=username)
    register_entry1.pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="Enter a Password:", bg="grey", width="300").pack()
    Label(register_screen, text="").pack()
    register_entry2 = Entry(register_screen, textvariable=password)
    register_entry2.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width="10", height="1", command=register_user).pack()

    Button(register_screen, text=">> Back <<", command=exit_register).place(x=220, y=245)


def main_screen():
    global main
    main = Tk()
    main.title("Notes")
    main.geometry("275x250")
    main.resizable(False, False)

    Label(main, text="Notes 2.0", bg="grey", width="275", height="2").pack()
    Label(main, text="").pack()
    Button(main, text="Login", command=login, width="25").pack()
    Label(main, text="").pack()
    Button(main, text="Register", command=register, width="25").pack()

    Button(main, text=">> Exit <<", command=exit_main).place(x=200, y=215)

    main.mainloop()


main_screen()

# ============================================================================
# ============================================================================
# Made by: https://github.com/OzonePrograms/
# Made by: https://github.com/OzonePrograms/
# Made by: https://github.com/OzonePrograms/
# ============================================================================
# ============================================================================

# Thanks for using!
