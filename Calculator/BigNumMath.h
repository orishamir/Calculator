#ifndef BigNumMath_h
#define BigNumMath_h

#include "Arduino.h"
#include "BigNumber.h"


BigNumber Sin(const BigNumber x, BigNumber precision);
BigNumber Cos(const BigNumber x, BigNumber precision);
BigNumber Tan(const BigNumber x, BigNumber precision);
BigNumber Log(BigNumber base, BigNumber a);
BigNumber factorial(BigNumber x);
BigNumber nthRoot(BigNumber base, BigNumber x);
BigNumber arcsin(BigNumber x, int mx=5);
BigNumber arccos(BigNumber x);
BigNumber arctan(BigNumber x);


BigNumber ln(BigNumber x);

BigNumber Abs(BigNumber x);

BigNumber Round(BigNumber x, int p);
BigNumber Floor(BigNumber x);
BigNumber Ceil(BigNumber x);
#endif
