#include "BigNumMath.h"
#include "BigNumber.h"

const BigNumber one (1);
const BigNumber two (2);
const BigNumber three (3);
const BigNumber four (4);
const BigNumber ten (10);
BigNumber half ("0.5");
// BigNumber e("2.7182818284590452353602874713526624977572470936999595749669676277240766303535");
// BigNumber E  ("2.7182818284590452353602874713526624977572470936999595749669676277240766303535");
// BigNumber pi ("3.1415926535897932384626433832795028841971693993751058209749445923078164062862");


// calculate sine of x with 'precision' iterations
BigNumber Sin(const BigNumber x, BigNumber precision)
{
  BigNumber val (1);
  while (precision > 0)
  {
    val = one - val * x * x / (two * precision) / (two * precision + one);
    precision--;
  }
  val = x * val;
  return val;
} 

BigNumber Cos(const BigNumber x, BigNumber precision)
{
  BigNumber val (1);
  val -= Sin(x, precision)*Sin(x, precision);
  val = val.sqrt();
  return val;
}

BigNumber Tan(const BigNumber x, BigNumber precision)
{
  return Sin(x, precision)/Cos(x, precision);
}

BigNumber ln(BigNumber x)
{
   
  // if x <= 0.5 or >= 2 take the square root and double the result  
  if (x <= half || x >= two)
    {
    BigNumber e = ln (x.sqrt());
    return e * two;
    }  // end of  x <= 0.5 or >= 2

  // some big numbers
  BigNumber a = (x - one) / (x + one);
  BigNumber e;
  BigNumber t = a;
  
  BigNumber i = one;
  BigNumber E;
  
  do
  { 
    E = e;
    e += t / i;
    t *= a * a;
    i += two;
  } while (e != E);

  return e * two;
}

BigNumber Log(BigNumber base, BigNumber a)
{
  return ln(a)/ln(base);
}

BigNumber factorial(BigNumber x){
  if(x == 0)
    return one;
  BigNumber result (1);

  x++;
  while(x-- > 1)
    result *= x;
  return result;
}

BigNumber arcsin(BigNumber x, int mx=5){
  BigNumber res (0);
  res += x;
  
  for (BigNumber n (0); n < mx; n++){
    BigNumber zz(2*n+1);
    //BigNumber(2*n+1)
    res += (factorial(zz-one)/(factorial(n).pow(2)*two.pow(2*n)*zz))*x.pow(2*n+1);
  }
  return res;
}

BigNumber arccos(BigNumber x){
  BigNumber pi ("3.1415926535897932384626433832795028841971693993751058209749445923078164062862");
  return pi/two-arcsin(x);
}

BigNumber arctan(BigNumber x){
  return arcsin(x/((one+x.pow(2)).sqrt()), 15);
}

BigNumber nthRoot(BigNumber n, BigNumber a){
  // calculate using newton's method
  // initial guess is 2 for now.
  /*
   formula:
   x_k+1 = 1/n*[(n-1)*x_k+a/x_k^(n-1)] 
   
   */
  //BigNumber prec("0.1");
  BigNumber x0(2);
  //while(Abs(a-x0.pow(n)) > prec)
  // 4 iterations
  for(int _ = 0; _ < 4; _++)
    x0 = one/n*((n-one)*x0+a/x0.pow(n-one));
  return x0;
}

BigNumber Abs(BigNumber x){
  if (x.isNegative())
    return x*BigNumber("-1");
  return x;
}

BigNumber Round(BigNumber x, int p){
  String t = x.toString();
  if (t.indexOf('.') < 0)
    return x;
  String t2 = t.substring(0, t.indexOf('.')+p+1);
  BigNumber newX (t2.c_str());

  int lastDigit = t[t2.length()]-48;
  if (lastDigit > 5){
    newX *= ten.pow(p);
    newX += 1;
    newX /= ten.pow(p);
    
  }
  newX.setScale(p);
  return newX;
}

BigNumber Floor(BigNumber x){
  String str = x.toString();
  return BigNumber(str.substring(0,str.indexOf('.')).c_str());
}

BigNumber Ceil(BigNumber x){
  return Floor(x+one);
}
