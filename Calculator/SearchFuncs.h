#ifndef SearchFuncs_h
#define SearchFuncs_h

#include "Arduino.h"
#include "Ops.h"

int searchChar(String expr, char c);
int searchSigma(String expr);
String splitSigma(String expr, int idxSum);
int searchSplittingComma(String expr, int idxLog);
bool isClosingAbs(String expr, unsigned i);

#endif
