Christopher Randin
cdrandin@csu.fullerton.edu

node32.ecs.fullerton.edu
usr: cpsc
passwd: KillerKiller5

** NOTICE **
Ubuntu12.04 is the attacker VM

Ubuntu12.04[Clone1] & Ubuntu12.04[Clone2] are the victim VMs

The attacker has a script which auto mounts the VM to the shared folder to the node

The victims have an alias which cleans up the mess when you want to remove files and recover some after the worm has run its mess
command: 'clean'
ex: cpsc@cpsc-virtualbox:~$ clean

* ignore the error messages 
*************

The program is expected to run using python2.7

Typical way to run the worms

cd ~/Desktop/shared
python2.7 [filename] [args]

** 
The attacking VM will contain fresh copies of the worms. So, it would just need to be executed.
It is located at ~/Desktop/shared/
**
