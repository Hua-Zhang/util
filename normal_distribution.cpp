/*
 * 这样生成的高斯分布随机数序列的期望为0.0，方差为1.0。
 * 若指定期望为E，方差为V，则只需增加：X = X * V + E;
 *
 */

#include <cstdlib>
#include <cmath>
#include <iostream>

double gaussrand() {
    static double V1, V2, S;
    static int phase = 0;
    double X;
    double U1, U2;
 
    if ( phase == 0 ) {
        do {
            U1 = (double)rand() / RAND_MAX;
            U2 = (double)rand() / RAND_MAX;
             
            V1 = 2 * U1 - 1;
            V2 = 2 * U2 - 1;
            S = V1 * V1 + V2 * V2;
        } while(S >= 1 || S == 0);
         
        X = V1 * sqrt(-2 * log(S) / S);
    } else {
        X = V2 * sqrt(-2 * log(S) / S);
        }
    phase = 1 - phase;
 
    return X;
}

int main(int argc, char * argv[]) {
        for (int i = 0; i < 10; ++ i) {
                std::cout << gaussrand() << std::endl;
        }
        return 0;
}
