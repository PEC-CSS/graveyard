import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--add', type=str, help='Adds task')
parser.add_argument('--done', type=str, help='Task completed')
parser.add_argument('--task', type=str, help='Show remaining task')
parser.add_argument('--exit', type=str, help='Exit the Program')
args=parser.parse_args()
if(args.add):
    result=open("data_store.txt", "a")
    result.write(" "+str(args.add))
    result.close()
    print(f"Task Added:{args.add}")
if(args.done):
    result = open("data_store.txt", "r").readlines()[0].split()
    result.remove(args.done)
    length = len(result)
    string = str()
    for i in range(length):
        string = string + " " + str(result[i])
    x = open("data_store.txt", "w")
    x.write(string)
    x.close()
    print(f"Task Completed:{args.done}")
if(args.task):
    print("Remaining Tasks are:")
    result = open("data_store.txt", "r").readlines()[0].split()
    for i in range(len(result)):
        print(result[i])
if(args.exit):
    result = open("data_store.txt", "w")
    result.write(str())
    result.close()
    print("ThankYou for Using this TODO list app.")