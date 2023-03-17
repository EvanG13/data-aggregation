import sys


def add_patient(patients, patient_id, patient_name):
    if patient_id not in patients:
        patients[patient_id] = patient_name


def process_instruction(patients, instruction):

    # dictionary containing all the current patients
    # Exam patientID examID
    #   key = patient
    #   val = number of exams
    exams = {}

    instr_list = instruction.split()

    command = instr_list[0]
    record = instr_list[1]
    if command == "ADD" and record == "PATIENT":
        patient_id = instr_list[2]
        patient_name = ' '.join(instr_list[3:])
        add_patient(patients, patient_id, patient_name)
    elif command == "ADD" and record == "EXAM":
        print("add exam")


def process_file(file_name):
    # set of all valid command actions and records
    valid_command = {"ADD", "DEL"}
    valid_record = {"PATIENT", "EXAM"}

    # list of commands
    commands_list = []

    # dictionary containing all the current patients
    #   key = id
    #   val = [name, number exams]
    patients = {}

    # parse file
    try:
        file = open(file_name)
        for line in file:
            # line_seg[0] = command
            # line_set[1] = record
            line_seg = line.split()

            # check if line is a valid instruction
            # if not valid, then start processing the next line of the file
            if line_seg[0] not in valid_command or line_seg[1] not in valid_record:
                continue

            # valid instruction
            # therefore, process the instruction
            process_instruction(patients, line)
        print(patients)
    except FileNotFoundError:
        print("File :", file_name + " does not exist")
        sys.exit(-1)

    # cleanup
    file.close()


def main(argv):
    process_file(argv)


if __name__ == "__main__":
    main(sys.argv[1])
