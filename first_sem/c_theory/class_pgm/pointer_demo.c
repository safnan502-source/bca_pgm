#include<stdio.h>

int main(){
    int x=10;   //integer variable x which stores 10
    int*p;
    p=&x;

    printf("%d\n",x);
    printf("%p\n",&x);
    printf("%p\n",p);
}
