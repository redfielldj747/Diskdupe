import subprocess


def main ():

    command = 'sudo mkdir -p /media/ubuntu/WriteTo'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error != None:
        command = 'notify-send -u normal -t 600 "External drive mounted"'
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output)
    else:
        command = 'notify-send -u normal -t 600 "External drive failed to mount"'
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

    # command = 'sudo mkdir -p /media/ubuntu/WriteTo'
    # process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()
    # print(output)
    #
    # command = 'sudo mkdir -p /media/ubuntu/WriteTo'
    # process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()
    # print(output)
    #
    # command = 'sudo mkdir -p /media/ubuntu/WriteTo'
    # process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()
    # print(output)
    #
    # command = 'sudo mkdir -p /media/ubuntu/WriteTo'
    # process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()
    # print(output)


if __name__ == "__main__":
    main()