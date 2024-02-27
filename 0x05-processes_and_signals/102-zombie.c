#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - this is a infinity loop
 *
 * Return: the value of zero
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - this is a main funv
 *
 * Return: the value of return
 */
int main(void)
{
	pid_t pid;
	char count = 0;

	while (count < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			count++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
