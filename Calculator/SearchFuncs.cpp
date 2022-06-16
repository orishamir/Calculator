#include "SearchFuncs.h"
#include "Arduino.h"
#include "Operators.h"

bool isIn(char c, char arr[]){
  for (byte i = 0; i < strlen(arr); i++){
    if (arr[i] == c)
      return true;
  }
  return false;
}

byte count(String s, char c){
  byte n = 0;
  for(byte i = 0; i < s.length(); i++){
    if (s[i] == c)
      n++;
  }
  return n;
}

bool isClosingAbs(String expr, unsigned i){
    if (i == 0)
        return false;
    if (i == expr.length()-1)
        return true;

    char left = expr[i-1];
    char right = expr[i+1];
    
    if (right == '|')
      return isClosingAbs(expr, i+1);
    if (left == '|')
      return isClosingAbs(expr, i-1);

    if(isIn(left, keywords)) // for sure
      return false;

    // for sure
    if (isIn(left, nonKeywords)) // (canConvertToInt((String)left))
      return true;
    if (isIn(left, nonKeywords) && isIn(right, nonKeywords))
      return false;
    if (isIn(right, keywords) && right != '-' && right != '+')
      return true;

    return false;
}

int searchSplittingComma(String expr, int idxLog){
  byte logCounter = 0;
  byte parCounter = 0;
  for (byte i = idxLog+2; i < expr.length(); i++){
    if (expr[i] == logC || expr[i] == sumC)
      logCounter++;
    else if(expr[i] == '(')
      parCounter++;
    else if(expr[i] == ')'){
      if (parCounter == 1)
        logCounter--;
      parCounter--;
    }
    else if (expr[i] == ',' && logCounter == 0)
      return i;
  }
  return -1;
}

String splitSigma(String expr, int idxSum){
  byte sigmaCounter = 0;
  int a = -1;
  int b = -1;
  int parCounter = 0;
  for (byte i = idxSum+2; i < expr.length()-1; i++){
    if (b != -1)
      break;
    if (expr[i] == sumC || expr[i] == logC){
      sigmaCounter += 1;
    }
    else if (expr[i] == '('){
      parCounter += 1;
    }
    else if (expr[i] == ')'){
      if (parCounter == 1){
          sigmaCounter -= 1;
      }
      parCounter -= 1;
    }
    else if (expr[i] == ',' && sigmaCounter == 0){
      if(a == -1)
        a = i;
      else
        b = i;
    } 
  }

  // the x=3 part
  String varVal = expr.substring(2, a);
  String End = expr.substring(a+1, b);
  String func = expr.substring(b+1, expr.length()-1);
  
  // var
  String var = varVal.substring(0, varVal.indexOf('='));
  String Val = varVal.substring(varVal.indexOf('=')+1);

  //_var = var;
  //_start = Val;
  //_end = End;
  //_func = func;
  return var + " " + Val + " " + End + " " + func;
}

int searchSigma(String expr){
  byte parCount = 0;
  byte absCounter = 0;
  
  for(byte i = 0; i < expr.length(); i++){
    if (expr[i] == ')')
      parCount++;
    else if(expr[i] == '(')
      parCount--;
    else if (expr[i] == '|'){
      if (isClosingAbs(expr, i))
        absCounter -= 1;
      else
        absCounter += 1;
    }
    else if(expr[i] == sumC && parCount == 0 && absCounter == 0 &&
        ((expr[i-1] != '+' &&
        expr[i-1] != '-' &&
        expr[i-1] != '*' &&
        expr[i-1] != '/' &&
        expr[i-1] != '^' ) ||
        i == 0))
      return i;
  }
 return -1;
}

int searchChar(String expr, char c){
  byte parCount = 0;
  byte absCounter = 0;
  
  for(int i = expr.length()-1; i >= 0; i--){
    if (expr[i] == ')')
      parCount++;
    else if(expr[i] == '(')
      parCount--;
    else if (expr[i] == '|'){
      if (isClosingAbs(expr, i))
        absCounter -= 1;
      else
        absCounter += 1;
    }
    else if(expr[i] == c && parCount == 0 && absCounter == 0 &&
        (expr[i-1] != '+' &&
        expr[i-1] != '-' &&
        expr[i-1] != '*' &&
        expr[i-1] != '/' && (
        expr[i-1] != '^' ||
        i == 0)))
      return i;
  }
 return -1;
}
