#include "Ops.h"

char keywords[] = {
    '+',
    '-',
    '*','%',
    '/',
    '!',
    '^','(', ')',
    sinC,cosC,tanC,sqrtC,nthrtC,sumC,'%','\x00'
};

char basicKeywords[] = {
  '+',
    '-',
    '*',
    '!'
};

char specialFuncs[] = {
  's', 'c', 't', 'S', 'C', 'T',
  'l', '$'
  
};

char nonKeywords[] = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
    'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'O', 'P', 'Q', 'U', 'V', 'W', 'X', 'Y', 'Z', '\x00'
};

char alphabet[] = {
  'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
  'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
};
