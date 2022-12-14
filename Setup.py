import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"
executables=[cx_Freeze.Executable("Snakes N Ladders Game.py")]
cx_Freeze.setup(
    name="Snakes N Ladders Game",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["Die1.png","Die2.png","Die3.png","Die4.png","Die5.png","Die6.png","redgoti.png","yellowgoti.png","greengoti.png","bluegoti.png","credits.jpg","intropic.png","intropic1.jpg","intropic2.jpg","intropic3.jpg","intropic4.jpg","playbg.jpg","menu.jpg","Trouble-Bigger.jpg","lose.wav","music.wav","Win.wav"]}},
    executables = executables

    )
