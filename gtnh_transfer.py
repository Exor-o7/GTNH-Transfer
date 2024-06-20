# Created by Exor_o7 (Discord)
# Version: 1.3
# Changelogs:
# 1.0 - Initial release
# 1.1 - Added this info lines and in the script as well. Reworded destination instance to put in if different path otherwise just press Enter. Added time module.
# 1.2 - Added shaderpacks folder
# 1.3 - Prepared for public release

import os
import shutil
import time

def select_instance(instance_dir):
    instances = os.listdir(instance_dir)
    clear_screen()
    print("Available Instances:")
    for i, instance in enumerate(instances):
        print(f"{i+1}. {instance}")
    print("")
    choice = input("Enter the number of the instance you want to transfer from: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(instances):
            return instances[choice - 1]
        else:
            print("Invalid choice. Please enter a valid number.")
            return select_instance(instance_dir)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return select_instance(instance_dir)

def select_destination_instance(destination_path):
    instances = os.listdir(destination_path)
    clear_screen()
    print("Available Instances for Destination:")
    for i, instance in enumerate(instances):
        print(f"{i+1}. {instance}")
    print("")
    choice = input("Enter the number of the destination instance you want to transfer to: ").strip()
    if choice == "":
        return None
    try:
        choice = int(choice)
        if 1 <= choice <= len(instances):
            return instances[choice - 1]
        else:
            print("Invalid choice. Please enter a valid number.")
            return select_destination_instance(destination_path)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return select_destination_instance(destination_path)

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def main():
    # Select source MultiMC instances path
    source_path = input("Enter the path to the MultiMC instances directory (Example: C:\Games\MultiMC\instances): ").strip()
    if not os.path.exists(source_path):
        print("Instances path does not exist.")
        return

    # Select instance to transfer
    instance_name = select_instance(source_path)

    # Select destination MultiMC instance path
    clear_screen()
    print("")
    destination_path = input(f"Enter the path to the destination MultiMC instances if differ, otherwise just press Enter [{source_path}]: ").strip()
    if destination_path == "":
        destination_path = source_path

    destination_instance_name = select_destination_instance(destination_path)
    if destination_instance_name:
        destination_instance_path = os.path.join(destination_path, destination_instance_name)
    else:
        destination_instance_path = destination_path

    # Transfer instance
    source_instance_path = os.path.join(source_path, instance_name)
    try:
        # List of directories to copy
        directories_to_copy = ['saves', 'journeymap', 'visualprospecting', 'TCNOdeTracker', 'serverutilities', 'schematics', 'resourcepacks', 'screenshots', 'shaderpacks']

        # List of files to copy
        files_to_copy = ['localconfig.cfg', 'options.txt', 'BotaniaVars.dat']

        # Create destination directory if it doesn't exist
        if not os.path.exists(destination_instance_path + "\.minecraft"):
            os.makedirs(destination_instance_path + "\.minecraft")

        # Copy directories
        for directory in directories_to_copy:
            source_dir = os.path.join(source_instance_path + "\.minecraft", directory)
            if os.path.exists(source_dir):
                shutil.copytree(source_dir, os.path.join(destination_instance_path + "\.minecraft", directory))
                print("copying " + directory)
                time.sleep(1)

        # Copy files
        for file in files_to_copy:
            source_file = os.path.join(source_instance_path + "\.minecraft", file)
            if os.path.exists(source_file):
                shutil.copy2(source_file, os.path.join(destination_instance_path + "\.minecraft", file))
                print("copying " + file)
                time.sleep(1)
        
        print("")
        print(f"Instance '{instance_name}' transferred successfully to '{destination_instance_path}'.")

        time.sleep(5)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()