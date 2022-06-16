#include "Simplifier.h"
#include "Arduino.h"
#include "SearchFuncs.h"
#include "BigNumMath.h"
#include "BigNumber.h"

extern char nonKeywords[];
extern char alphabet[];
extern bool isIn(char c, char arr[]);
BigNumber ten(10);
BigNumber one(1);

String toExpr(String expr){
  String result = "";
  char left;
  char c;
  char right;
  
  for(byte i = 1; i < expr.length()-1; i++){
    left = expr[i-1];
    c = expr[i];
    right = expr[i+1];

    if(c == '('){
      if (isIn(left, nonKeywords)){
        result.concat(expr.substring(0, i));
        result.concat("*");
        result.concat(expr.substring(i));
        return toExpr(result);
      }
    }else if(c == ')'){
      if (isIn(right, nonKeywords)){
        result.concat(expr.substring(0, i+1));
        result.concat("*");
        result.concat(expr.substring(i+1));
        return toExpr(result);
      }
    }else if (isIn(c, alphabet)){
      if(isIn(left, nonKeywords)){
        result.concat(expr.substring(0, i));
        result.concat("*");
        result.concat(expr.substring(i));
        return toExpr(result);
      }else if(isIn(right, nonKeywords)){
        result.concat(expr.substring(0, i+1));
        result.concat("*");
        result.concat(expr.substring(i+1));
        return toExpr(result);
      }
    }
  }
  return expr;
}

String approximate(BigNumber num){

  int p = 6;
  BigNumber left[2] = {Floor(num), one};
  BigNumber right[2] = {Ceil(num), one};
  BigNumber midVal;

  num = Round(num, p);
  BigNumber mid[2];
  
  for(int i = 0; i < 3000; i++){
    mid[0].~BigNumber();
    mid[1].~BigNumber();
    
    mid[0] = left[0]+right[0];
    mid[1] = left[1]+right[1];
    midVal.~BigNumber();
    midVal = Round(mid[0]/mid[1], p);

    if(num < midVal){
      right[0].~BigNumber();
      right[1].~BigNumber();
      right[0] = mid[0];
      right[1] = mid[1];
    }
      
    else if(num > midVal){
      left[0].~BigNumber();
      left[1].~BigNumber();
      left[0] = mid[0];
      left[1] = mid[1];
    }
    else{
      String res = "";
      res += mid[0];
      //res.concat(mid[0]);
      res += '/';
      res += mid[1];
      return res;
    }
  }
  return "nope";
}
