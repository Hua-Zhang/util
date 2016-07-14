#include <string.h>
#include <stdio.h>

int main(void){
  char input[16] = "abc,d";
  char *p;
  p = strtok(input, ",");
  while(p) { //p != NULL
    printf("%s\n",p);
    p = strtok(NULL,",");
  }
  return 0;
}
