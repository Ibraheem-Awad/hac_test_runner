import os
import glob
import subprocess as sp


class bcolors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    CYELLOW = '\033[33m'


def get_tests_info():
    all_tests = []  # string array for tests
    test_counter = 0

    for file in glob.glob("*.in"):
        name = convert(file)  # convert it to string
        all_tests.append(name)  # add to string
        test_counter += 1

    if test_counter <= 1:
        print(bcolors.FAIL + "Not enough .in files\n" + bcolors.ENDC)
        return all_tests, test_counter

    else:
        all_tests.sort()

    return all_tests, test_counter


def convert(char):

    # initialization of string to ""
    new = ""

    # traverse in the string
    for ch in char:
        new += ch

    # return string
    return new


def menu_msg():
    answer = input(
        "What would you like to do ?\n" +
        "1) Make tests\n" +
        "2) Diff in tests\n" +
        "3) Tar you files \n" +
        "4) About \n" +
        "0) Exit\n"
    )
    return answer


def test_msg():
    answer = input(
        "Would you like to make tests for (0 to return to menu):\n" +
        "1) School Tests \n" +
        "2) Your Tests\n" +
        "3) Both\n"
    )
    return answer


def make_tests():
    all_tests, test_counter = get_tests_info()

    if test_counter >= 1:
        any_test = all_tests[0]
        ex_num = any_test[2]
        prog_num = any_test[3]

        print(bcolors.OKCYAN + "\nFound " +
              str(test_counter) + " test files" + bcolors.ENDC)
        answer = test_msg()
        option_tests(answer, all_tests, ex_num, prog_num)
    else:
        return


def option(answer):

    if answer == '0':
        print(bcolors.CYELLOW +
              "Thank you for using my program\nGood Luck..." + bcolors.ENDC)
        return

    elif answer == '1':
        make_tests()
        answer = menu_msg()
        option(answer)

    elif answer == '2':
        make_diff()
        answer = menu_msg()
        option(answer)

    elif answer == '3':
        make_tar()
        answer = menu_msg()
        option(answer)

    elif answer == '4':
        print(bcolors.HEADER + "Programmed by Ibraheem ,using Python\n" + bcolors.ENDC)
        answer = menu_msg()
        option(answer)

    else:
        print("Wrong Choice")
        answer = input()
        return option(answer)


def option_tests(answer, all_tests, targil_num, prog_num):
    if answer == '1':
        school_test(all_tests, targil_num, prog_num)
        print("\n")
        return
    elif answer == '2':
        my_test(all_tests, targil_num, prog_num)
        print("\n")
        return
    elif answer == '0':
        print("\n")
        return
    elif answer == '3':
        school_test(all_tests, targil_num, prog_num)
        my_test(all_tests, targil_num, prog_num)
        print("\n")
        return
    else:
        print("Wrong Choice")
        answer = input()
        return option_tests(answer, all_tests, targil_num, prog_num)


def school_test(all_tests, targil_num, prog_num):
    out_test, in_test = 0, 0
    exist = False
    if os.path.isfile("ex" + targil_num + prog_num + "sol"):
        exist = True
    else:
        print(bcolors.FAIL + "School SOL doesn't exist" + bcolors.ENDC)
        return

    if exist is True:
        while in_test < len(all_tests):
            run_command = './ex' + targil_num + prog_num + 'sol < ' + \
                all_tests[in_test] + ' > test' + str(out_test) + '.out'
            out_test += 1
            in_test += 1
            os.system(run_command)  # execute command line

        print(bcolors.OKGREEN + str(out_test) +
              " Out files were made using school executable" + bcolors.ENDC)


def my_test(all_tests, targil_num, prog_num):
    out_test, in_test = 0, 0
    exist = False
    if os.path.isfile("ex" + targil_num + prog_num):
        exist = True
    else:
        print(bcolors.FAIL + "Your SOL doesn't exist" + bcolors.ENDC)
        return

    if exist is True:
        while in_test < len(all_tests):
            run_command = './ex' + targil_num + prog_num + ' < ' + \
                all_tests[in_test] + ' > test' + str(out_test) + '_me.out'
            os.popen(run_command)
            output = sp.getoutput(run_command)
            
            if output != "":
                print(bcolors.WARNING + "Problem in " +
                      all_tests[in_test] + bcolors.ENDC)
            
            out_test += 1
            in_test += 1
            output = ""

        print(bcolors.OKGREEN + str(out_test) +
              " Out files were made using your executable" + bcolors.ENDC)


def make_diff():
    out_test = []
    ind_school, ind_me, file_count, done = 0, 1, 0, 0
    sub_string = "--"
    problem = False
    for out_file in glob.glob("*.out"):
        name = convert(out_file)  # convert it to string
        out_test.append(name)
        file_count += 1

    if file_count < 2:
        print(bcolors.FAIL + "Not enough .out files\n" + bcolors.ENDC)
        return

    else:
        file_count /= 2
        out_test.sort()

        while file_count < len(out_test):
            run_command = 'diff ' + \
                out_test[ind_school] + ' ' + out_test[ind_me]
            os.popen(run_command)
            output = sp.getoutput(run_command)

            if sub_string in output:
                print(bcolors.WARNING + "Problem in " +
                      out_test[ind_school] + bcolors.ENDC)
                problem = True
            ind_school += 2
            ind_me += 2
            file_count += 1
            done += 1
            output = ""
        if problem is False:
            print(bcolors.OKCYAN +
                  "\nNo problems were found, Good job :)" + bcolors.ENDC)
        print(bcolors.OKGREEN + str(done) +
              " Diffs were made\n" + bcolors.ENDC)


def make_tar():
    print("\nNOTE: Place it where you want to tar your files with README")

    files = []
    file_count = 0
    read_me_exists = False
    isValid = False
    for file in glob.glob("*.cc"):
        name = convert(file)
        files.append(name)
        file_count += 1

    read_me_exists = os.path.exists('README')
    if read_me_exists is True:
        files.append('README')
        file_count += 1
        files.sort()

    if file_count < 4:
        print(bcolors.FAIL + "Not enough files to tar\n" +
              bcolors.ENDC + "Make sure all files exist\n")
        return

    isValid = check_for_80(files)
    ValidNames = check_for_name(files)
    if ValidNames is False:
        print(bcolors.FAIL + "Tar failure\n" +
              bcolors.ENDC + "Check your files names\n")
        return
    if isValid is True:
        get_ex = files[1]
        targil_num = get_ex[2]
        run_command = 'tar czvf ex' + targil_num + '.tgz ex'+targil_num + \
            'a.cc ex'+targil_num+'b.cc ex'+targil_num+'c.cc README'
        os.system(run_command)
        print(bcolors.OKGREEN + "Tar was successfully made\n" + bcolors.ENDC)

    else:
        print(bcolors.FAIL + "Tar failure\nMake sure you don't have 80+ characters " +
              "in a line, in all of your files\n" + bcolors.ENDC)


def check_for_80(files):
    cur_file = 0
    sub_str = ""
    to_ret = True
    while cur_file < len(files):
        run_command = "grep '.\{79,\}' " + files[cur_file]
        os.popen(run_command)
        sub_str = sp.getoutput(run_command)

        if sub_str != "":
            print(bcolors.WARNING +
                  "80+ characters was found in " + files[cur_file] + bcolors.ENDC)
            to_ret = False

        sub_str = ""
        cur_file += 1
    return to_ret


def check_for_name(files):
    to_ret = True
    get_ex = files[1]
    targil_num = get_ex[2]

    if files[0] != "README":
        to_ret = False

    if files[1] != "ex" + targil_num + "a.cc":
        to_ret = False

    if files[2] != "ex" + targil_num + "b.cc":
        to_ret = False

    if files[3] != "ex" + targil_num + "c.cc":
        to_ret = False

    return to_ret


# ----------------------------------------------------------------------------
check_for_user_command = 'whoami'
os.popen(check_for_user_command)
username = sp.getoutput(check_for_user_command)

if username == "ibraheem":
    run_command = 'pwd'
    os.popen(run_command)
    path = sp.getoutput(run_command)
    answer = menu_msg()
    option(answer)
else:
    print(bcolors.FAIL + "You are not allowed to use the program\n" + bcolors.ENDC +
          "Please contact the developer.")
