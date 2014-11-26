Christopher Randin
cdrandin@csu.fullerton.edu

Part 1:

The included files are result.png result.zip. They are both files in which I copied the binary data into.
result.png: Used copy/b *.png + *.zip result.png
result.zip: Used copy/b *.zip + *.png result.zip

1. Explain what is happening. Do some research in order to find out what the above copy command does. 
In your explanation be sure to explain the role of each argument in the above command. 
Also, be sure to explain how Windows handles files which leads the above behavior.
Include the answers to these questions in the README file you submit.

The binaries are being merged together. Which ever is copied first is what is executed and the rest of the binary
whether it be malicious or not.

2. How can this technique be used for hiding malicious codes?

This can be used for hiding maliciouscode by being able to bind the programs together in the same file.
Having the reliable code execute and the malicious code hide in the file waiting to be execute upon instruction.

3. How robust is this technique when in terms of avoiding detection by anti-virus tools? You may need to do some research.
This technique may not be so robust because the file may appear to be larger than usual which can be "obvious" when examining the file.
It can also be used to detect the malicious signatures when examining the files.

Part 2:
Can be executes as follows: 
python binder.py /bin/ls /bin/ps

Then the generate an executable file 'bound' will be created. 
Execute it as follows:
./bound which will then execute both the ls and ps command.