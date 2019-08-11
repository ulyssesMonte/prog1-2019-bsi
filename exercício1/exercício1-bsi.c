#include <stdio.h>

int main(void) {
  int x;
  printf("digite um número ");
  scanf("%d",&x);
  if ((x % 2) == 0){
    printf("PAR");
  }
  else{
    printf("IMPAR");
  }
  return 0;
}