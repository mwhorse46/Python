from cx_Freeze import setup, Executable

setup(name='Menu',
      version='0.1',
      description='Faltu',
      executables = [Executable("tkinter_exe.py")])
