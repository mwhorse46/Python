from cx_Freeze import setup, Executable

setup(name='UrlParse',
      version='0.1',
      description='Parse stuff',
      executables = [Executable("cx_freeze_python_to_exe.py")])
