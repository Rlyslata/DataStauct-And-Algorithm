// chapter1.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//
#include"生成伪随机数.h"

//线型同余发生器 X[n+1]=(A*X[n]+B)%mod
//生成0~mod-1的mod个伪随机数
int* Linears(int A, int Xi, int B, int mod) {
	int* radom = (int*)malloc((mod)*sizeof(int));
	for (int i = 0; i < mod; i++)
	{
		radom[i] = (A * Xi + B) % mod;
		Xi = radom[i];
	}
	return radom;
}

//随机生成min~max之间的随机数

int* randomXgp(int min ,int max) {
	//
	int A = 1, B = 3, Xi = 0, mod = 10;
	int* numbers = Linears(A,Xi,B,mod);
	for (int i = 0; i < mod; i++)
	{
		numbers[i] = min + (numbers[i] /(float)max) * (max - min);
	}
	return numbers;
}

int main()
{
	int* radom = Linears(7, 0, 5, 11);
	int* random = randomXgp(3, 8);
	for (int i=0;i<10;i++)
	    cout <<radom[i]<< endl;
	cout << "------------------" << endl;
	for (int i = 0; i < 10; i++)
		cout << random[i] << endl;
    cout << "Hello World!\n"; 

}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
