the = {"seed": 937162211, "dump": False, "halves":"", "reuse":True , "go": "data", "help": False, "file": "/etc/data/auto93.csv","min": 0.5, "rest":4}

help_string = """cluster.lua : an example csv reader script
    (c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
    USAGE: cluster.lua  [OPTIONS] [-g ACTION]
    OPTIONS:
    -d  --dump    on crash, dump stack   = false
    -f  --file    name of file           = ../etc/data/auto93.csv
    -F  --Far     distance to "faraway"  = .95
    -g  --go      start-up action        = data
    -h  --help    show help              = false
    -m  --min     stop clusters at N^min = .5
    -p  --p       distance coefficient   = 2
    -s  --seed    random number seed     = 937162211
    -S  --Sample  sampling data size     = 512
    ]]"""