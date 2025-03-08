#include <stdio.h>
#include <time.h>

int maint(){
    struct timespec res;
    clock_getres(CLOCK_MONOTONIC, &res);
    printf("clock resolution: %;d sec, %ld ns\n", res.tv_sec, res.tv_nsec);
    return 0;
}