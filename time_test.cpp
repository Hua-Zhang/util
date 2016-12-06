#include <time.h>
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
  clock_t start, now;
  start = clock();
  for(int i = 0; i <= 10000; ++i) {
  }
  now = clock();
  double time_length = (double)(now - start + 1) / (double)CLOCKS_PER_SEC * 1000;
  cout << "耗时: " << time_length << "s" << endl;
  return 0;
}
