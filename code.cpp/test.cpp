#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

void test(int *ap, int *bp)
{
    *ap += 1;
    *bp += 2;
}
int main()
{
    int a = 1, b = 2;
    int *ap = &a, *bp = &b;
    test(ap, bp);
    return 0;
}


