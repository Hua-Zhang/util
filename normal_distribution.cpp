/*
 * 产生服从高斯的分布的随机数方法主要有四种:
 * 1、中心极限定理法
 * 2、Box-Muller算法
 * 3、Marsaglia polar算法
 * 4、Ziggurat算法
 *
 * 参考：http://blog.skyoung.org/2013/08/27/generate-random-number/
 */

#include <cstdlib>
#include <cmath>
#include <iostream>

// 中心极限定理法
double random_guassian_central_limit() {
	const int N = 20;
	double sum = 0;
	for( int i = 0; i < N; ++i) {
	    sum += (double)rand()/RAND_MAX;
	}
	sum -= N/2.0;
	sum /= sqrt(N/12.0);

	return sum;
}

// Box-Muller算法
#define PI 3.1415926
double random_guassian_box_muller() {
    static double  U1, U2;
    double Z;
    int flag = 0;
    
    if(flag == 0) {
		U1 = (double)rand()/RAND_MAX;
		U2 = (double)rand()/RAND_MAX;
		Z = sqrt(-2*log(U1))*sin(2*PI*U2);
    } else {
		Z = sqrt(-2*log(U1))*cos(2*PI*U2);
	}

    flag = 1 - flag;
    return Z;
}

/*
 * Marsaglia polar算法
 * 这样生成的高斯分布随机数序列的期望为0.0，方差为1.0。
 * 若指定期望为E，方差为V，则只需增加：X = X * V + E;
 */
double random_guassian_marsaglia_polar() {
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
		std::cout << random_guassian_central_limit() << "\t" << random_guassian_box_muller() << "\t" << random_guassian_marsaglia_polar() << std::endl;
	}
	return 0;
}
