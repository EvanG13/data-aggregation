import sys


def process_summary(patients):
    """
    process a summary of all the patient records: names, id and exam count
    :param patients: dictionary containing the existing patients
    :return: a string that is a list of all the patient records,
            returns empty string if 0 patients on record
    ex:
        Name: PATIENT_NAME, Id: PATIENT_ID, Exam Count: EXAM_COUNT
        Name: John Doe, Id: 1, Exam Count 2
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


def add_exam(patients, exams, patient_id, exam_id):
    """
    add a new exam record
    used by command : ADD EXAM
    :param exams: dict of exams
    :param patients: dict of patients
    :param patient_id: patient id
    :param exam_id: exam id
    """

    # check if the patient id is in the patients dict
    # only want to add an exam for patients who exist
    # if patient exists, add the exam id to their exam_id set
    # uses a set to hold exam ids in order to prevent duplicates
    if patient_id in patients and exam_id not in exams:
        patients[patient_id][1].add(exam_id)
        exams[exam_id] = patient_id


def delete_patient(patients, exams, patient_id):
    """
    delete patient from the dict of patients
    used by command : DEL PATIENT
    :param exams: dict of exam id
    :param patients: dict of patients
    :param patient_id:  patient id
    """

    # check if the given patient id is in the patients dict
    # need to check in order to ensure that we only attempt to delete a patient that exists
    # if they do exist, delete the patient
    # otherwise, do not delete
    if patient_id in patients:
        # iterate through all the exam ids that are in the patient's exam set()
        # then delete them from the exam record's dict
        for exam_id in patients[patient_id][1]:
            exams.pop(exam_id)

        # delete the patient from the patients record dict
        patients.pop(patient_id)


def delete_exam(patients, exams, exam_id):
    """
    delete the given exam
    :param exams: dict of exam ids
    :param patients: dict of patients
    :param exam_id: exam id
    """

    # check if an exam with that id exists
    # if the exam exists, delete the exam from patient's set who
    #   owns that exam and the general record of exam ids\
    # otherwise, continue processing
    if exam_id in exams:
        patient_id = exams.get(exam_id)
        if patient_id in patients:
            patients[patient_id][1].remove(exam_id)
        exams.pop(exam_id)


def process_instruction(patients, exams, instr_list):
    """
    process the passed in valid instruction
    :param exams: dict of exam ids
    :param patients: dict of patients
    :param instr_list: valid instruction as a list
    """

    # the command and record at index 0 and 1 of the instruction list
    # for EVERY valid instruction
    command = instr_list[0]
    record = instr_list[1]

    # start processing instructions
    # rest of instruction changes depending on the command and record
    # ADD PATIENT patient_id name
    if command == "ADD" and record == "PATIENT":
        patient_id = instr_list[2]
        patient_name = ' '.join(instr_list[3:])
        add_patient(patients, patient_id, patient_name)
    # ADD EXAM patientID examID
    elif command == "ADD" and record == "EXAM":
        patient_id = instr_list[2]
        exam_id = instr_list[3]
        add_exam(patients, exams, patient_id, exam_id)
    # DEL PATIENT patient_iD
    elif command == "DEL" and record == "PATIENT":
        patient_id = instr_list[2]
        delete_patient(patients, exams, patient_id)
    # DEL EXAM exam_id
    elif command == "DEL" and record == "EXAM":
        exam_id = instr_list[2]
        delete_exam(patients, exams, exam_id)


def process_file(file_name):
    """
    process the given file of Patient and Exam records
    :param file_name: name of input file
    :return: a summary of the successfully processed file as a string
    """

    # set of all valid command actions and records
    valid_command = {"ADD", "DEL"}
    valid_record = {"PATIENT", "EXAM"}

    # dictionary containing all patient records
    # patient id as key so that patients have unique ids
    # set to hold exam ids to prevent a patient having multiple exams with the same exam_id
    #   key = patient_id
    #   val = [name, set() of exam ids]
    patients = {}

    # dictionary containing all exam records
    # used to prevent multiple patients from having the same exam id
    #   key = exam_id
    #   value = patient_id
    exams = {}

    # parse file line by line
    try:
        file = open(file_name)
        for line in file:
            # line_seg[0] = command
            # line_set[1] = record
            line_list = line.split()

            # check if line is a valid instruction
            # if valid it is a valid instruction, then process the instruction
            # otherwise, continue processing the file
            if line_list[0] in valid_command and line_list[1] in valid_record:
                # valid instruction
                # therefore, process the instruction
                process_instruction(patients, exams, line_list)
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
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("command line argument : input .txt file containing list of instructions")
        print("usage example: python main.py data1")
        sys.exit(1)
    main(sys.argv[1])
