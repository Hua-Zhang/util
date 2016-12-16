
unsigned long long next_random = 1;
double get_random() {    //产生0~1之间的随机数
  next_random = next_random * (unsigned long long)25214903917 + 11;
  return (next_random & 0xFFFF) / (real)65536;
}


//产生随机数
double MaxEnt::get_random() {
    int N = 9999;                           //四位小数。
    srand(time(NULL));                      //设置随机数种子，使每次获取的随机序列不同。
    double i = ( rand()%(N+1)/(float)(N+1) ) * 2 - 1;   //生成-1~1间的随机数。
    return i;
}
