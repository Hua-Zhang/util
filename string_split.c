/*
strtok是一个线程不安全的函数，因为它使用了静态分配的空间来存储被分割的字符串位置
*/
#include <string.h>
#include <stdio.h>

int main(void){
  char input[16] = "abc,d";
  char *p;
  /*strtok places a NULL terminator
    infront of the token,if found*/
  p = strtok(input, ",");
  while(p) { //p != NULL
    printf("%s\n",p);
    /*Asecond call to strtok using a NULL
        as the first parameter returns a pointer
        to the character following the token*/
    p = strtok(NULL,",");
  }
  return 0;
}
