#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<time.h>
#include<windows.h>
int main()
{
unsigned int i=1;
int num;
int fact=1;
printf("Enter a number to find its factorial: ");
scanf("%d",&num);
while(i<=num){
	fact=fact*i;
	i++;
}
if (num>0){
	printf("good",num);
}else{
	printf("not food",num);
}
printf("The factorial is %d",fact);
return 0;
}