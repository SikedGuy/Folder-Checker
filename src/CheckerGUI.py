from CheckerNoGUI import Checker
import customtkinter as ctk
import subprocess

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_widget_scaling(1.5)


class OpenFolderButton(ctk.CTkButton):
    def __init__(self, master, pathTofolder, width = 140, height = 28, text = "CTkButton", **kwargs):
        super().__init__(master, width, height, text=text, command=self.Click, **kwargs)
        self.pathTofolder = pathTofolder

    def Click(self):
        # open target folder
        print(self.pathTofolder)
        subprocess.Popen(f"explorer /enter, {self.pathTofolder}")
        pass

class CheckerWithGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.checker = Checker()

        self.displayedFolders: list[ctk.CTkFrame] = []

        # create window
        self.title("Folder Checker")
        self.geometry(f"{1560}x{840}")

        # start frames
        self.rightFrame = ctk.CTkFrame(self, 300) # dont know what to use for yet. maybe logging
        self.rightFrame.pack(padx = 10, pady = 10, fill = "y", side = "right")

        self.problemsDetectedFrame = ctk.CTkFrame(self, height = 40)
        self.problemsDetectedFrame.pack(padx = 10, pady = 10, fill = "x", side = "top")

        self.usernameFrame = ctk.CTkFrame(self, height = 40)
        self.usernameFrame.pack(padx = 10, pady = 10, fill = "x", side = "bottom")

        self.mainFrame = ctk.CTkScrollableFrame(self)
        self.mainFrame.pack(padx = 10, pady = 10, fill = "both", expand = True)

        # create data things
        self.problemsDetectedText = ctk.CTkLabel(self.problemsDetectedFrame, text="Hello world")
        self.problemsDetectedText.pack(padx = 5, pady = 5, fill = "both", expand = True)

        self.usernameInput = ctk.CTkEntry(self.usernameFrame, placeholder_text="system username:")
        self.usernameInput.pack(padx = 5, pady = 5, fill = "both", expand = True)

        self.startCheckingButton = ctk.CTkButton(self.rightFrame, text="Start Checking", command=self.OnStartChecking)
        self.startCheckingButton.pack(padx = 5, pady = 5, fill = "x", side = "bottom")

    def OnStartChecking(self) -> None:
        if (Checker.ValidUsername(self.usernameInput.get())):
            (fullpath, folders) = self.checker.StartSearch(self.usernameInput.get())
            if (folders.__len__() > 0):
                self.problemsDetectedText.configure(text="bad folders detected")

                self.DisplayFolders(fullpath, folders)

            else:
                self.problemsDetectedText.configure(text="no bad folders detected")
        else:
            self.problemsDetectedText.configure(text="bad username input")

    def DisplayFolders(self, fullpath: str, folders: list[str]) -> None:
        self.DestroyShownFolders()

        for folder in folders:
            f = ctk.CTkFrame(self.mainFrame, height=38)
            t = ctk.CTkLabel(f, text=folder)
            b = OpenFolderButton(f, f"{fullpath}\\{folder}", text="show in file explorer")
            f.pack(padx = 5, pady = 5, fill = "x")
            b.pack(padx = 5, pady = 5, side = "right")
            t.pack(padx = 5, pady = 5, fill = "both")

            self.displayedFolders.append(f)

    def DestroyShownFolders(self) -> None:
        for folder in self.displayedFolders:
            folder.destroy()
        
        self.displayedFolders.clear()

    #def PackShownFolders(self) -> None:
    #    for frame in self.displayedFolders:
    #        frame.pack(padx = 5, pady = 5, fill = "both")


    def Run(self) -> None:
        self.mainloop()
