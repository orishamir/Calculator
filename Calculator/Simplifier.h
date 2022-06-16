#ifndef Simplifier_h
#define Simplifier_h

#include "Arduino.h"
#include "BigNumber.h"
String toExpr(String expr);
String approximate(BigNumber num);

#endif
