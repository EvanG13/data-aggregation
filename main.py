import sys


def process_summary(patients):
    """
    process a summary of all the patient records: names, id and exam count
    :param patients: dictionary containing the existing patients
    :return: a string that is a list of all the patient records, returns empty string if empty patients record
    example: Name: PATIENT_NAME, Id: PATIENT_ID, Exam Count: EXAM_COUNT
    """

    return_str = ""
    for patient_id in patients:
        patient_name = patients[patient_id][0]
        exam_count = len(patients[patient_id][1])
        return_str += "Name: " + patient_name + ", Id: " + str(patient_id) + ", Exam Count: " + str(exam_count) + "\n"

    return return_str


def add_patient(patients, patient_id, patient_name):
    """
    add a patient record to patients dict
    used by command : ADD PATIENT
    :param patients: dict of patients
    :param patient_id: patient id
    :param patient_name: patient name
    """

    # check if patient id is not in the patients dict to ensure that
    # only want to add new patients
    # otherwise, do not add and continue processing
    if patient_id not in patients:
        patients[patient_id] = [patient_name, set()]


def add_exam(patients, patient_id, exam_id):
    """
    add a new exam record
    used by command : ADD EXAM
    :param patients: dict of patients
    :param patient_id: patient id
    :param exam_id: exam id
    """

    # check if the patient id is in the patients dict
    # only want to add an exam for patients who exist
    # if patient exists, add the exam id to their exam_id set
    # uses a set to hold exam ids in order to prevent duplicates
    if patient_id in patients:
        patients[patient_id][1].add(exam_id)


def delete_patient(patients, patient_id):
    """
    delete patient from the dict of patients
    used by command : DEL PATIENT
    :param patients: dict of patients
    :param patient_id:  patient id
    """

    # check if the given patient id is in the patients dict
    # need to check in order to ensure that we only attempt to delete a patient that exists
    # if they do exist, delete the patient
    # otherwise, do not delete
    if patient_id in patients:
        patients.pop(patient_id)


def delete_exam(patients, exam_id):
    """
    delete the given exam
    :param patients: dict of patients
    :param exam_id: exam id
    """

    # iterate through the patients dict searching for the patient who owns that exam record
    # if an owner of that exam record is found, delete the exam record
    # otherwise, do not delete
    for patient_id in patients:
        if exam_id in patients[patient_id][1]:
            patients[patient_id][1].remove(exam_id)
            break


def process_instruction(patients, instruction):
    """
    process the passed in valid instruction
    :param patients: dict of patients
    :param instruction: valid instruction
    """

    # split the valid instruction into a list
    instr_list = instruction.split()

    # the command and record are at these two positions for every valid instruction
    command = instr_list[0]
    record = instr_list[1]

    # start processing instructions
    # ADD PATIENT patient_id name
    if command == "ADD" and record == "PATIENT":
        patient_id = instr_list[2]
        patient_name = ' '.join(instr_list[3:])
        add_patient(patients, patient_id, patient_name)
    # ADD EXAM patientID examID
    elif command == "ADD" and record == "EXAM":
        patient_id = instr_list[2]
        exam_id = instr_list[3]
        add_exam(patients, patient_id, exam_id)
    # DEL PATIENT patient_iD
    elif command == "DEL" and record == "PATIENT":
        patient_id = instr_list[2]
        delete_patient(patients, patient_id)
    # DEL EXAM exam_id
    elif command == "DEL" and record == "EXAM":
        exam_id = instr_list[2]
        delete_exam(patients, exam_id)


def process_file(file_name):
    """
    process the given file of Patient and Exam records
    :param file_name: name of input file
    """

    # set of all valid command actions and records
    valid_command = {"ADD", "DEL"}
    valid_record = {"PATIENT", "EXAM"}

    # dictionary containing all the current patients
    #   key = id
    #   val = [name, set() of exam ids]
    patients = {}

    # parse file line by line
    try:
        file = open(file_name)
        for line in file:
            # line_seg[0] = command
            # line_set[1] = record
            line_seg = line.split()

            # check if line is a valid instruction
            # if not valid, then start processing the next line of the file
            if line_seg[0] in valid_command and line_seg[1] in valid_record:
                # valid instruction
                # therefore, process the instruction
                process_instruction(patients, line)
    except FileNotFoundError:
        print("File :", file_name + " does not exist")
        sys.exit(-1)

    # cleanup
    file.close()

    # input file of instructions was successfully processed
    # therefore, return the summary as a string
    return process_summary(patients)


def main(argv):
    summary = process_file(argv)
    print(summary)


if __name__ == "__main__":
    main(sys.argv[1])
