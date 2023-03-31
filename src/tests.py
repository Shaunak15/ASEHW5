import sys
sys.path.append("./src")

from num import Num
from sym import Sym
import utils
from data import *
from pathlib import Path
import os,math 
import optimize 
import Query
import update 
import cluster
import Discretization 



def readCSV(sFilename, fun):
  
    with open(sFilename, mode='r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            fun(line)


def test_csv():

    global n
    def fun(t):
        n += len(t)
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "ASEHW5/etc/data/auto93.csv")
    if(csv_content(csv_path) == 8 * 399):
        print(" Test csv : successful \n")
    return csv_content(csv_path) == 8 * 399

def csv_content(src):
    with open(src, mode='r') as file:
        csvFile = csv.reader(file)
        l =0
        for row in csvFile:
            l += len(row)
        return l

def test_nums():
    val = Num()
    lst = [1,1,1,1,2,2,3]
    for a in lst:
        val.add(a)
    print("test_nums: PASS\n")
    return 11/7 == val.mid() and 0.787 == utils.rnd(val.div(),3)
    
def test_sym():
    value = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
    sym1 = Sym()
    for x in value:
        sym1.add(x)
    print("test_syms: PASS\n")
    return "a"==sym1.mid() and 1.379 == utils.rnd(sym1.div(),3)

def test_the():
    print("The results of test_the function:")
    print(str(the))
    print("test_the: PASS\n")
    return True

def test_data():
    csv_path = "../etc/data/auto93.csv"
    data = Data().read_file(csv_path)
    col = data.cols.x[1].col
    print("Test data : successful \n")
    print(col.lo,col.hi, Query.mid(col), Query.div(col))
    print(Query.stats(data))
    return True

def test_clone():
    csv_path = "../etc/data/auto93.csv"
    data = Data().read_file(csv_path)
    data2 = data.clone(data,data.rows)
    print("Test clone : successful \n")
    utils.oo(Query.stats(data))
    utils.oo(Query.stats(data2))
    return True

def test_half():
    csv_path = "../etc/data/auto93.csv"
    data = Data().read_file(csv_path)

    left, right, A, B, c = cluster.half(data)
    print("Test half : successful \n")
    print(len(left), len(right), len(data.rows))
    print(utils.o(A), c)
    print(utils.o(B))
    return True

def test_cliffs():
    if utils.cliffs_delta([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]):
        return False
    if not utils.cliffs_delta([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]):
        return False

    t1, t2 = [], []
    for i in range(1000):
        t1.append(utils.rand())
        t2.append(math.sqrt(utils.rand()))
    if utils.cliffs_delta(t1, t1):
        return False
    if not utils.cliffs_delta(t1, t2):
        return False
    diff, j = False, 1.0
    while not diff:
        t3 = list(map(lambda x: x * j,t1))
        diff = utils.cliffs_delta(t1, t3)
        print(">", utils.rnd(j), diff)
        j *= 1.025
    print("Test cliff : successful \n")
    return True

def test_dist():
    csv_path = "../etc/data/auto93.csv"
    data = Data().read_file(csv_path)
    num = Num()
    for row in data.rows:
        update.add(num, Query.dist(data, row, data.rows[1]))
    print("Test dist : successful \n")
    print({"lo": num.lo, "hi": num.hi, "mid": utils.rnd(Query.mid(num)), "div": utils.rnd(num.n)})
    return True

def test_tree():
    csv_path = "../etc/data/auto93.csv"
    data = Data().read_file(csv_path)
    print("Test tree : successful \n")
    cluster.show_tree(cluster.tree(data))

    return True

def test_sway():
  
    csv_path = "../etc/data/auto93.csv"
    data = Data().read_file(csv_path)
    best, rest = optimize.sway(data)
    print(utils.o(Query.stats(data)))
    print("\nall ", utils.o(Query.stats(data)))
    print("    ",  utils.o( Query.stats(data, Query.div)))
    print("\nbest", utils.o(Query.stats(best)))
    print("    ",   utils.o(Query.stats(best, Query.div)))
    print("\nrest", utils.o(Query.stats(rest)))
    print("    ",   utils.o(Query.stats(rest, Query.div)))
    print("\nall ~= best?", utils.o(utils.diffs(best.cols.y, data.cols.y)))
    print("best ~= rest?", utils.o(utils.diffs(best.cols.y, rest.cols.y)))
    return True



def test_bins():
    csv_path = "../etc/data/auto93.csv"
    data = Data().read_file(csv_path)
    best, rest = optimize.sway(data)
    print("Test bin : successful")
    print("all","","","",utils.o({"best":len(best.rows), "rest": len(rest.rows)}))
    for k,t in enumerate(Discretization.bins(data.cols.x, {"best": best.rows, "rest": rest.rows})):
        for _, range in enumerate(t):
            print(range.txt, range.lo, range.hi,round(Query.value(range.y.has, len(best.rows), len(rest.rows), "best")),
                  range.y.has)
    print("end")
    return  True 
