#include <stdio.h>

int main() {
    int num1, num2, sum;
    printf("请输入第一个数：");
    scanf("%d", &num1);
    printf("请输入第二个数：");
    scanf("%d", &num2);
    sum = num1 + num2;
    printf("两个数的和是：%d\n", sum);
    return 0;
}
