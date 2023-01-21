import sys
import getopt
import os

def main(argv):

    data_file = ""
    dir_path = ""
    opts,args = getopt.getopt(argv[1:],"hf:p:",["help","data_file=","dir_path"])

    for opt,arg in opts:
        if opt in ("-h", "--help"):
            print(" [Usage]: python3 summary.py -f <data_file> -p <dir_path> \n \
path&file: python3 summary.py -f instrace.ls.log -p ./output_data/ \n \
path_only: python3 summary.py -p ./output_data/")
            sys.exit()
        elif opt in ("-f", "--data_file"):
            data_file = arg
        elif opt in ("-p", "--dir_path"):
            dir_path = arg

    if data_file != "":
        summary(dir_path,data_file)
        exit()

    if data_file == "" and dir_path != "":
        for file in os.listdir(dir_path):
            summary(dir_path,file)
        exit()

        

def summary(dir_path, data_file):
    file = open(dir_path+data_file,"r")
    lines = file.readlines()
    inst_list = []
    inst_count = 0
    for line in lines:
        inst = line.split(",")[1].split("\n")[0]
        inst_list.append(inst)
        inst_count = inst_count + 1

    test_and_j_count = test_and_j(inst_list)
    cmp_and_j_count = cmp_and_j(inst_list)
    nop_and_any_count = nop_and_any(inst_list)

    print("inst_count in " + data_file + " is " + str(inst_count))
    print("test_and_j_count in " + data_file + " is " + str(test_and_j_count))
    print("cmp_and_j_count in " + data_file + " is " + str(cmp_and_j_count))
    print("nop_and_any_count in " + data_file + " is " + str(nop_and_any_count))
    print("proportion is " + str( float(test_and_j_count + cmp_and_j_count + nop_and_any_count) * 2.0 / float(inst_count) ))


def test_and_j(inst_list):
    test_and_j_count = 0
    last_inst = "*"
    for inst in inst_list:
        if last_inst == "test" and inst[0] == "j":
            test_and_j_count = test_and_j_count + 1
        last_inst = inst
    return test_and_j_count

def cmp_and_j(inst_list):
    cmp_and_j_count = 0
    last_inst = "*"
    for inst in inst_list:
        if last_inst == "cmp" and inst[0] == "j":
            cmp_and_j_count = cmp_and_j_count + 1
        last_inst = inst
    return cmp_and_j_count

def nop_and_any(inst_list):
    nop_and_any_count = 0
    last_inst = "*"
    for inst in inst_list:
        if last_inst == "nop":
            nop_and_any_count = nop_and_any_count + 1
        last_inst = inst
    return nop_and_any_count


if __name__ == "__main__":
    main(sys.argv)

    