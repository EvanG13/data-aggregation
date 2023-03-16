

def process_data():
    # set of all valid commands
    # inside sets for future expansion to valid actions and records
    valid_action = {"ADD", "DELETE"}
    valid_record = {"PATIENT", "EXAM"}

    # list of commands
    commands_list = []

    # open file then read line by line
    file = open("data1")
    for command in file:
        command_seg = command.split()
        # check if the action and record are valid
        # if not valid, then start processing the next line of the file
        if command_seg[0] not in valid_action or command_seg[1] not in valid_record:
            continue
        # action and record are valid
        commands_list.append(command)

    # print list of valid commands
    print(commands_list)

    # cleanup
    file.close()


def main():
    process_data()


if __name__ == "__main__":
    main()
