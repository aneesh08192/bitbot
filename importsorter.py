import os

cwd = os.getcwd() +"/Actress/"

dirs = os.listdir(cwd)
cmds = []
for import_index in dirs:
    if import_index != "__pycache__":
       name = import_index.split(".")[0]
       print("from Actress."+name+" import "+name)
       cmds.append(name)

print("\n")

for import_indexs in dirs:
    if import_indexs != "__pycache__":
       names = import_indexs.split(".")[0]
       print("updater.dispatcher.add_handler(CommandHandler('"+names+"'," +names+",run_async=True))")

print("\n")

for cmd in cmds:
    print(cmd +" - [seconds] [No. of images]" )
