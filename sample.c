#include<stdio.h>
int main(){
    int b;
    int a=9;
    float c;
    int d;
    float e;
    int f;
    printf("Enter B:\n");
    scanf("%d",&b);
    
    printf("Enter C:\n");
    scanf("%f",&c);
    
    printf("Enter D:\n");
    scanf("%d",&d);
    
    printf("Enter E:\n");
    scanf("%f",&e);
    
    printf("Enter F:\n");
    scanf("%d",&f);

    printf("sum of integers= %d\n",a+b+d+f);
    printf("sum of floats=%f",c+e);

    return 0;
}