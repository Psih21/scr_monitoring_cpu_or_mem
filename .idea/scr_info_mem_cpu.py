import psutil
import sys

# while True:
# value = input("Please, enter mem or cpu: ")


def out_info():
    print("Please, enter mem or cpu:")


def get_info_cpu():
    print("CPU:")
    cpu = psutil.cpu_times(set)

    for i, x in enumerate(cpu):
        print(f"logical CPU: {i+1}")
        arg = x._fields
        value = tuple(psutil.cpu_times())
        liste = zip(arg, value)
        for arg, value in liste:
            print(f"\t|{arg}| = {value}")
        print("-------------------------------")


def get_info_mem():
    print("MEM:")
    mem = psutil.virtual_memory()
    arg = mem._fields
    value = tuple(psutil.virtual_memory())
    liste = zip(arg, value)
    for arg, value in liste:
        print(f"\t|{arg}| = |{value}|")
    print("-------------------------------")


def main():
    for value in sys.argv:
        if value == 'cpu':
            get_info_cpu()
        elif value == 'mem':
            get_info_mem()
        elif value == '':
            out_info()
        else:
            pass


if __name__ == '__main__':
        main()
