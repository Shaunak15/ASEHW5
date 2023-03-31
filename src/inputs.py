the = {"seed": 937162211, "dump": False, "halves":"", "reuse":True , "go": "data", "help": False, "file": "/etc/data/repgrid3.csv","min": 0.5, "rest":4}

help_string = """
        script.lua : an example script with help text and a test suite
        (c)2022, Tim Menzies <timm@ieee.org>, BSD-2
        USAGE:   script.lua  [OPTIONS] [-g ACTION]
        OPTIONS:
        -d  --dump    on crash, dump stack   = false
        -f  --file    name of file           = ../etc/data/repgrid3.csv
        -g  --go      start-up action        = data
        -h  --help    show help              = false
        -p  --p       distance coefficient   = 2
        -s  --seed    random number seed     = 937162211
        ACTIONS:
        -g  the	show settings
        -g  rand	generate, reset, regenerate same
        -g  sym	check syms
        -g  num	check nums
        """