# import subprocess
# import os

# def run_terminal_command():
#     command = "python --version"
#     ommand = "python --version"
#     subprocess.run(command, shell=True)
#     subprocess.run(ommand, shell=True)


# run_terminal_command()

# /home/tspl/Desktop/image

# def createEnvAuto(path,name="mortal"):
#     cmd1=path
#     cmd2=["pip3","install","virtualenv"]
#     cmd3 = ["python3", "-m", "venv", name]
#     cmd4=name+"/"
#     cmd5=["source","bin/activate"]
#     cmd6=".."
#     os.chdir(cmd1)
    # print("11111111111")
    # subprocess.run(cmd2)
    # subprocess.run(cmd3)
    # print("222211111111111")
    
    # os.chdir(cmd4)
    # subprocess.run(cmd5)
    # os.chdir(cmd6)

# /home/tspl/Documents/shellScripting

# give_the_path_where_You_want_to_create=input("hey mortal please give me a path")
# give_the_path_where_You_want_to_create="/home/tspl/Documents/shellScripting"
# name_of_virtual_env=input("mortalBro give me the name of virtualenv")
# createEnvAuto(give_the_path_where_You_want_to_create)





# import subprocess
# import os

# def ch(path):
#     # subprocess.run("cd ..",shell=True)
#     os.chdir(path)
# ch("/home/tspl/Documents/")


# import os

# def go_one_step_back():
#     current_directory = os.getcwd()
#     parent_directory = os.path.dirname(current_directory)
    
#     # Change to the parent directory
#     os.chdir(parent_directory)

# # Call the function to go one step back
# go_one_step_back()

# Verify the change by printing the current directory
# print("Current Directory:", os.getcwd())



























