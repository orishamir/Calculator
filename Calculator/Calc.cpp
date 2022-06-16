#include "Calc.h"
#include "Arduino.h"
#include "SearchFuncs.h"
#include "Ops.h"
#include "BigNumMath.h"
#include "BigNumber.h"
#define precision 45

bool canConvertToInt(String expr){
  for(byte i = 0; i < expr.length(); i++)
    if ((expr[i] < 48 || expr[i] > 57) && expr[i] != '.')
      return false;
  return true;
}

BigNumber calc(String expr){
  if (canConvertToInt(expr))
    return BigNumber(expr.c_str());

  int idxAdd = searchChar(expr, '+');
  int idxSub = searchChar(expr, '-');
  int idxMul = searchChar(expr, '*');
  int idxDiv = searchChar(expr, '/');
  int idxMod = searchChar(expr, '%');
  int idxPow = searchChar(expr, '^');
  int idxFac = searchChar(expr, '!');
  int idxSqrt = searchChar(expr, sqrtC);
  int idxNthrt = searchChar(expr, nthrtC);
  int idxSin = searchChar(expr, sinC);
  int idxCos = searchChar(expr, cosC);
  int idxTan = searchChar(expr, tanC);
  int idxArcsin = searchChar(expr, arcsinC);
  int idxArccos = searchChar(expr, arccosC);
  int idxArctan = searchChar(expr, arctanC);
  int idxLog = searchChar(expr, logC);
  int idxSum = searchSigma(expr);

  if (idxAdd != -1){
    String left = expr.substring(0, idxAdd);
    String right = expr.substring(idxAdd+1);

    return calc(left) + calc(right);
  }
  else if (idxSub != -1){
    String left = expr.substring(0, idxSub);
    String right = expr.substring(idxSub+1);

    return calc(left) - calc(right);
  }
  else if (idxMul != -1){
    String left = expr.substring(0, idxMul);
    String right = expr.substring(idxMul+1);

    return calc(left) * calc(right);
  }

  else if (idxDiv != -1){
    String left = expr.substring(0, idxDiv);
    String right = expr.substring(idxDiv+1);

    return calc(left) / calc(right);
  }

  else if(idxMod != -1){
    String left = expr.substring(0, idxMod);
    String right = expr.substring(idxMod+1);
    return calc(left) % calc(right);
  }

  else if (idxPow != -1){
    String left = expr.substring(0, idxPow);
    String right = expr.substring(idxPow+1);
    return calc(left).pow(calc(right));
  }

  else if (idxFac != -1){
    String left = expr.substring(0, idxFac);
    // round cuz maybe we got like 1.99 and in that case im big sad
    return factorial(Round(calc(left), 0));
  }
  
  else if (idxSqrt != -1){
    String right = expr.substring(idxSqrt+1);
    return calc(right).sqrt();
  }
  else if(idxNthrt != -1){
    int i = searchSplittingComma(expr, idxNthrt);
    // the nth root of x = x^(1/n)
    String b = expr.substring(2, i);
    String a = expr.substring(i+1, expr.length()-1);
    String x1 = calc(b).toString();
    String x2 = calc(a).toString();

    if(x1.toFloat() == 2)
      return calc(a).sqrt();
    return pow((double)(x2.toFloat()), 1.0/x1.toFloat());
  }
  
  else if (idxSin != -1){
      String right = expr.substring(idxSin+1);
      BigNumber pi ("3.1415926535897932384626433832795028841971693993751058209749445923078164062862");
      return Sin(calc(right)*(pi/BigNumber(180)), precision);
  }
  
  else if (idxCos != -1){
    String right = expr.substring(idxCos+1);
    BigNumber pi ("3.1415926535897932384626433832795028841971693993751058209749445923078164062862");
    return Cos(calc(right)*(pi/BigNumber(180)), precision);
  }
  
  else if (idxTan != -1){
    String right = expr.substring(idxTan+1);
    BigNumber pi ("3.1415926535897932384626433832795028841971693993751058209749445923078164062862");
    return Tan(calc(right)*(pi/BigNumber(180)), precision);
  }
  
  else if(idxArcsin != -1){
    String right = expr.substring(idxArcsin+1);
    BigNumber pi ("3.1415926535897932384626433832795028841971693993751058209749445923078164062862");
    return arcsin(calc(right))/(pi/BigNumber(180));
  }

  else if(idxArccos != -1){
    String right = expr.substring(idxArccos+1);
    BigNumber pi ("3.1415926535897932384626433832795028841971693993751058209749445923078164062862");
    return arccos(calc(right))/(pi/BigNumber(180));
  }

  else if(idxArctan != -1){
    String right = expr.substring(idxArctan+1);
    BigNumber pi ("3.1415926535897932384626433832795028841971693993751058209749445923078164062862");
    return arctan(Round(calc(right), 30))/(pi/BigNumber(180));
  }
  
  else if (idxLog != -1){
    int i = searchSplittingComma(expr, idxLog);
    String b = expr.substring(2, i);
    String a = expr.substring(i+1, expr.length()-1);
    //Serial.println("b: " + b);
    //Serial.println("a: " + a);
    return Log(calc(b), calc(a));
  }
  
  else if(idxSum != -1){
    String ret = splitSigma(expr, idxSum);
    // get all the shit

    // var + "\n" + Val + "\n" + End + "\n" + func
    String _var = ret.substring(0, ret.indexOf(" "));
    String _start = "";
    String _end = "";
    String _func = "";
    int prevI = ret.indexOf(" ");
    for(byte i = ret.indexOf(" ")+1; i < ret.length();i++){
      if(ret[i] == ' '){
        if (_start == "")
          _start = ret.substring(prevI+1, i);
        else if(_end == ""){
          _end = ret.substring(prevI+1, i);
          _func = ret.substring(i+1);
          break;
        }
        prevI = i;
      }
    }
    // Serial.println("var: "+_var);
    // Serial.println("start: "+_start);
    // Serial.println("end: "+_end);
    // Serial.println("func: "+_func);
    
    // `ceil` because if for example:
    // calc(log(2,4)) would equal 2, but stored as 1.999997
    // and (int) would fuck it up.
    
    int s = Round(calc(_start), 0);
    int e = Round(calc(_end), 0);
    
    // Serial.println(s);
    // Serial.println(e);
    // iterate through the possibilites,
    // then replace the variable with its val
    // and calculate it.
    BigNumber Sum = 0;
    String tmp = _func;
    String vstr = "";
    //Serial.println("expr=" + expr);
    for (int v = s; v <= e; v++){
      //Serial.print("v=");
      //Serial.println(v);
      vstr.concat(v);
      tmp.replace(_var, vstr);
      vstr = "";
      Sum += calc(tmp);
      tmp = _func;
    }
    return Sum;
  }
  
  else if(expr[0] == '|'){
    return Abs(calc(expr.substring(1, expr.length()-1)));
  }
  
  else if(expr[0] == '('){
    return calc(expr.substring(1, expr.length()-1));
  }
  Serial.println("Somehow reached end of string");
  return BigNumber("69.420");
}
