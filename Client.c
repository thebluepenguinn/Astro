#include <windows.h>
#include <stdio.h>
#include <string.h>

#define PIPE_NAME L"\\\\.\\pipe\\serverPipe"
#define BUFFER_SIZE 1024

int main(void){
    HANDLE hPipe;
    DWORD dwWritten, dwRead;
    char buffer[BUFEER_SIZE];
    const char *message = //INCLUDE A DYNAMIC WAY TO MESSAGE HERE

    //try to connect to pipe
    hPipe = CreateFile(PIPE_NAME, GENERIC_READ |
        GENERIC_WRITE, 0, NULL, OPEN_EXISTING, 0, NULL);

    if (hPipe == INVALID_HANDLE_VALUE) {
        fprint(stderr, "Could not connect to pipe");
        return 1;
    }

    printf("Connected.\n")

    //send data
    WriteFile (hPipe, message, strlen(message) + 1, dwWritten, NULL);

    if(success && dwRead > 0)
    {buffer[dwRead] = '\0'; //nullterminate
    printf("Received: %s\n", buffer);}
    else
    {fprintf(stderr, "ReadFile failed or server closed connection.\n");}

    //close pipe handle
    CloseHandle(Pipe);
    return 0;
}