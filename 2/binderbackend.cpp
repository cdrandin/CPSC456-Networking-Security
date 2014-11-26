#include <string>
#include "codearray.h"
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <vector>
#include <sys/stat.h>
#include <sys/types.h>
#include <fstream>

using namespace std;

int main()
{
	/* The child process id */
	pid_t childProcId = -1;
	char * fileName;

	/* Go through the binaries */
	for(int progCount = 0; 	progCount < NUM_BINARIES; ++progCount)
	{
			
		//TODO: Create a temporary file you can use the tmpnam() function for this.
		fileName = tmpnam(NULL);
		ofstream outfile(fileName);

		//TODO: Open the file and write the bytes of the first program to the file.
		//These bytes are found in codeArray[progCount]
		for (int i = 0; i < programLengths[progCount]; ++i)
		{
			outfile << codeArray[progCount][i];
		}
		outfile.close();
		
		//TODO: Make the file executable: this can be done using chmod(fileName, 0777)
		chmod(fileName, 0777);

		//TODO: Create a child process using fork
		childProcId = fork();

		/* I am a child process; I will turn into an executable */
		if(childProcId == 0)
		{
			//TODO: use execlp() in order to turn the child process into the process
			//running the program in the above file.	
			execlp(fileName, fileName, NULL);
		}
	}
	
	/* Wait for all programs to finish */
	for(int progCount = 0; progCount < NUM_BINARIES; ++progCount)
	{
		/* Wait for one of the programs to finish */
		if(wait(NULL) < 0)
		{
			perror("wait");
			exit(-1);
		}	
	}
}
