#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <openssl/rand.h>

#include "crypto.h"
#include "common.h"


#define LEDGER_FILE "ledger.bin"
#define PERMISSIONS (S_IRUSR | S_IWUSR)

int crack_key_hash(unsigned char fd_key_hash[]) {
	int i, j, k;
	unsigned char hash[4], *temp, *key_hash;

	for (i = 0; i < 256; i++) {
		hash[0] = i;
		for (j = 0; j < 256; j++) {
			hash[1] = j;

			for (k = 0; k < 256; k++) {
    			hash[2] = k;
    			hash[3] = '\0';

    			temp = md5_hash(hash, 3);
        		memset(temp + 2, 0, 14);
        		key_hash = md5_hash(temp, 2);

    			if (memcmp(key_hash, fd_key_hash, 16) == 0) {

    				printf("%s", hash);
    				return 0;
    			}
			}
		}
	}

	return 1;
}

int main(int argc, char **argv) {
	unsigned char fd_key_hash[16];
    int fd;

    fd = open(LEDGER_FILE, O_RDONLY, PERMISSIONS);
    read(fd, fd_key_hash, 16);


	close(fd);
	crack_key_hash(fd_key_hash);

	return 0;
}
