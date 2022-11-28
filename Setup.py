import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"
executables=[cx_Freeze.Executable("Snakes N Ladders Game.py")]
cx_Freeze.setup(
    name="Snakes N Ladders Game",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["shortcuticon.ico","Die1.png","Die2.png","Die3.png","Die4.png","Die5.png","Die6.png","redgoti.png","yellowgoti.png","greengoti.png","bluegoti.png","credits.jpg","intropic.png","intropic2.jpg","intropic3.jpg","intropic4.jpg","intropic5.jpg","playbg.jpg","icon.jpg","menu.jpg","Snakes-and-Ladders-Bigger.jpg","ladder.wav","lose.wav","music.wav","Win.wav","snake.wav"]}},
    executables = executables

    )
