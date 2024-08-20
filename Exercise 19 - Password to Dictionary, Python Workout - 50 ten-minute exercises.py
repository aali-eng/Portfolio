# In this exercise, write a function, passwd_to_dict, that reads
# from a Unix-style “password file,” commonly stored as /etc/passwd,
# and returns a dict based on it. Each line is one user record, divided
# into colon-separated fields. The first field (index 0) is the username,
# and the third field (index 2) is the user’s unique ID number. (In the
# system from which I took the /etc/passwd file, nobody has ID -2, root
# has ID 0, and daemon has ID 1.) For our purposes, you can ignore all
# but these two fields. Sometimes, the file will contain lines that
# fail to adhere to this format. For example, we generally ignore lines
# containing nothing but whitespace. Some vendors (e.g., Apple) include
# comments in their /etc/passwd files, in which the line starts with
# a # character. The function passwd_to_dict should return a dict based
# # on /etc/passwd in which the dict’s keys are usernames and the values
# # are the users’ IDs.

#Book solution:

def passwd_to_dict(filename):
    users = {}
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])


    return users

print(passwd_to_dict('7647d1af56cc8c6a9744-4a0968a11a0a30e34466030a203b5f91493beac5/passwd.txt'))

