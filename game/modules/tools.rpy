init python:
    import os

    class Tools:
        def __init__(self):
            pass

        def dir_walker(self, path:str = os.path.join(renpy.config.gamedir,"images/background")):# C:\Users\water\Desktop\renpy\Ushio_Noa\game
            dir_names=[]
            file_names=[]
            with os.scandir(path) as it:
                for entry in it:
                    if entry.is_file():
                        if entry.name == "desktop.ini":
                            pass
                        else:
                            file_names.append(entry.name)
                    elif entry.is_dir():
                        dir_names.append(entry.name)
            return dir_names+file_names

        def get_dirs(self,path:str=os.path.join(renpy.config.gamedir,"images/background")):
            dir_names=[]
            with os.scandir(path) as it:
                for entry in it:
                    if entry.is_dir():
                        dir_names.append(entry.name)
            return dir_names

        def control_character(self,position,emotion,emoji:str="",action=blank,effect=blank,scaleup=blank):
            if emoji:
                renpy.show_screen(emoji,position=position,emotion=emotion,action=action,effect=effect,scaleup=scaleup)
            else:
                renpy.show_screen("noa_base",position=position,emotion=emotion,action=action,effect=effect,scaleup=scaleup)

    tools = Tools()