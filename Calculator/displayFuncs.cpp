#include "displayFuncs.h"
#include "Arduino.h"
#include <Adafruit_GFX.h>
#include <Adafruit_TFTLCD.h>

#define BLACK     0x0000 
#define RED      0xF800
#define GREY      0xCE79
#define LIGHTGREY 0xDEDB
#define BLUE     0x001F
#define GREEN   0x07E0
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE0
#define WHITE   0xFFFF

#define spacing 6

#define LEFT -1
#define RIGHT 1


extern String charZero[9];
extern String charOne[9];
extern String charTwo[9];
extern String charThree[9];
extern String charFour[9];
extern String charFive[9];
extern String charSix[9];
extern String charSeven[9];
extern String charEight[9];
extern String charNine[9];

extern String charX[9];
extern String charL[9];
extern String charO[9];
extern String charG[9];
extern String charS[9];
extern String charI[9];
extern String charN[9];
extern String charC[9];
extern String charT[9];
extern String charA[9];

extern String charFull[9];
extern String charEmpty[9];
extern String charPlus[9];
extern String charMinus[9];
extern String charMul[9];
extern String charSqrt[9];
extern String divisionLine[9];
extern String charSigma[9];
extern String charEqual[9];
extern String charCursor[9];
extern String charOpeningParenthesis[9];
extern String charClosingParenthesis[9];

extern bool canConvertToInt(String expr);

extern int searchChar(String expr, char c);
extern int searchSigma(String expr);
extern String splitSigma(String expr, int idxSum);
extern int searchSplittingComma(String expr, int idxLog);
extern bool isClosingAbs(String expr, unsigned i);
extern bool isIn(char c, char arr[]);

extern char basicKeywords[];
extern char keywords[];
extern char specialFuncs[];

short curX;
short curY;
/*
byte countHeight(String expr, int fontSize){
  unsigned largest = 0;
  unsigned tmp=0;
  byte i = 0;
  byte parCounter = 0;
  while(i < expr.length()){
    tmp = 0;
    if(expr[i] == '/' || expr[i] == 'l' || expr[i] == '$'){
      do{
        if(expr[i] == '(')
          parCounter++;
        else if(expr[i] == ')')
          parCounter--;
        
        else if(expr[i] == '/')
          tmp += fontSize*6;
        else if(expr[i] == 'l')
          tmp += 6*fontSize;
        else if(expr[i] == '$')
          tmp += 6*fontSize;
        i++;
      }while((!isIn(expr[i], basicKeywords) && parCounter != 0) && i < expr.length());
    }
    largest = max(tmp, largest);
    i++;
  }
  return largest;
}

bool isNumOrVar(String expr){
  for(char c: expr)
    if(isIn(c, keywords)){
      return false;
    }
  return true;
}


String moveCursor(String expr, int dir){
    int curpos = expr.indexOf("_");
    char left = expr[(expr.length()+(curpos-1))%expr.length()];
    char right =expr[(expr.length()+curpos+1)%expr.length()];

    if (dir == LEFT && curpos != 0 && (left == ',' || isIn(expr[curpos-2], specialFuncs)))
        dir *= 2;
    else if (dir == RIGHT && isIn(right, specialFuncs) && curpos != expr.length()-1)
        dir *= 2;
    if(curpos == 0 && dir == LEFT)
      curpos = expr.length()-1;
    else if(curpos == expr.length()-1 && dir == RIGHT)
      curpos = 0;
    else
      curpos = (curpos+dir) % expr.length();
    
    expr.replace("_", "");
    String result = "";
    result.concat(expr.substring(0, curpos));
    result.concat("_");
    result.concat(expr.substring(curpos));
    return result;
}

double countPixels(String expr, int x, int y,int fontSize, uint16_t foreColor, Adafruit_TFTLCD tft){
  
  if(isNumOrVar(expr) || expr=="_"){

    for (byte i = 0; i < expr.length(); i++){
      int pos = x+i*8*fontSize+i*fontSize/3;
      switch(expr[i]){
        case '0':
          drawChar(charZero, pos, y, fontSize, foreColor, tft);
        break;
        case '1':
          drawChar(charOne, pos, y, fontSize, foreColor, tft);
        break;
        case '2':
          drawChar(charTwo, pos, y, fontSize, foreColor, tft);
        break;
        case '3':
          drawChar(charThree, pos, y, fontSize, foreColor, tft);
        break;
        case '4':
          drawChar(charFour, pos, y, fontSize, foreColor, tft);
        break;
        case '5':
          drawChar(charFive, pos, y, fontSize, foreColor, tft);
        break;
        case '6':
          drawChar(charSix, pos, y, fontSize, foreColor,tft);
        break;
        case '7':
          drawChar(charSeven, pos, y, fontSize, foreColor,tft);
        break;
        case '8':
          drawChar(charEight, pos, y, fontSize, foreColor,tft);
        break;
        case '9':
          drawChar(charNine, pos, y, fontSize, foreColor,tft);
        break;
        case 'x':
          drawChar(charX, pos, y, fontSize, foreColor,tft);
        break;

        case 'l':
          drawChar(charL, pos, y, fontSize, foreColor,tft);
        break;

        case 'o':
          drawChar(charO, pos, y, fontSize, foreColor,tft);
        break;

        case 'g':
          drawChar(charG, pos, y, fontSize, foreColor,tft);
        break;

        case '=':
          drawChar(charEqual, pos, y, fontSize, foreColor,tft);
        break;
        case '_':
          curX = pos;
          curY = y;
          drawChar(charCursor, pos, y, fontSize, RED, tft);
          break;
      }
    }
    return 8*fontSize*expr.length()+(expr.length()-1)*spacing;
  }
  
  int idxAdd = searchChar(expr, '+');
  int idxSub = searchChar(expr, '-');
  int idxMul = searchChar(expr, '*');
  int idxDiv = searchChar(expr, '/');
  int idxPow = searchChar(expr, '^');
  int idxNthrt = searchChar(expr, 'R');
  
  int idxSin = searchChar(expr, 's');
  int idxCos = searchChar(expr, 'c');
  int idxTan = searchChar(expr, 't');
  
  int idxLog = searchChar(expr, 'l');
  int idxSum = searchSigma(expr);
  
  if (idxAdd != -1){
    String left = expr.substring(0, idxAdd);
    String right = expr.substring(idxAdd+1);
    int pixelsBefore = countPixels(left, x, y, fontSize,foreColor,tft);
    
    drawChar(charPlus,x+pixelsBefore+fontSize,y,fontSize, foreColor, tft);
    return pixelsBefore +spacing*fontSize+fontSize+ countPixels(right, x+pixelsBefore+8*fontSize+fontSize/3,y,fontSize,foreColor,tft);
  }
  else if (idxSub != -1){
    String left = expr.substring(0, idxSub);
    String right = expr.substring(idxSub+1);
    int pixelsBefore = countPixels(left, x, y, fontSize,foreColor,tft);
    
    drawChar(charMinus,x+pixelsBefore+fontSize,y,fontSize, foreColor, tft);
    return pixelsBefore +spacing*fontSize+fontSize*3+ countPixels(right, x+pixelsBefore+8*fontSize+2*fontSize,y,fontSize,foreColor, tft);
  }
  else if (idxMul != -1){
    String left = expr.substring(0, idxMul);
    String right = expr.substring(idxMul+1);
    int pixelsBefore = countPixels(left, x,y,fontSize,foreColor,tft);
    
    drawChar(charMul,x+pixelsBefore+fontSize,y,fontSize, foreColor, tft);
    return pixelsBefore +spacing*fontSize+fontSize*3+ countPixels(right, x+pixelsBefore+8*fontSize+2*fontSize, y,fontSize,foreColor, tft);
  }
  else if (idxDiv != -1){
    String left = expr.substring(0, idxDiv);
    String right = expr.substring(idxDiv+1);
    int height = countHeight(left, fontSize);
    
    int parCount = 0;
    
    for(byte i = 0; i < left.length()-1; i++){
      if(left[i] == '(')
        parCount++;
      else if(left[i] == ')')
        parCount--;
    }
    if (parCount == 1 && left[0] == '(' && left[left.length()-1] == ')')
      left = left.substring(1, left.length()-1);
    
    parCount = 0;
    for(byte i = 0; i < right.length()-1; i++){
      if(right[i] == '(')
        parCount++;
      else if(right[i] == ')')
        parCount--;
    }
    if (parCount == 1 && right[0] == '(' && right[right.length()-1] == ')')
      right = right.substring(1, right.length()-1);
    
    int numeratorPixels = countPixels(left, x, y-6*fontSize-height, fontSize,0xff, tft);
    int denominatorPixels = countPixels(right, x, y+6*fontSize, fontSize,0xff,tft);
    int maxPix = max(numeratorPixels, denominatorPixels);
    
    //countPixels(left, x+maxPix/2-numeratorPixels/2, y-6*fontSize-height, fontSize,foreColor, tft);
    //countPixels(right, x+maxPix/2-denominatorPixels/2, y+6*fontSize, fontSize,foreColor,tft);

    tft.fillRect(x, y+8*fontSize/2, maxPix+2*fontSize, fontSize,foreColor);
    return numeratorPixels+fontSize*5;
  }
  else if (idxPow != -1){
    String left = expr.substring(0, idxPow);
    String right = expr.substring(idxPow+1);
    int x2 = countPixels(left,x,y,fontSize,foreColor,tft);
    return x2 + countPixels(right,x2+x,y-4*fontSize,fontSize/2,foreColor,tft);
  }
  else if(idxNthrt != -1){
    int i = searchSplittingComma(expr, idxNthrt);
    Serial.print("splitcomma: ");
    Serial.println(i);
    // the nth root of x = x^(1/n)
    String left = expr.substring(2, i);
    String right = expr.substring(i+1, expr.length()-1);
    /*
    int parCount = 0;
    
    for(byte i = 0; i < left.length()-1; i++){
      if(left[i] == '(')
        parCount++;
      else if(left[i] == ')')
        parCount--;
    }
    if (parCount == 1)
      left = left.substring(1, left.length()-1);
    
    parCount = 0;
    for(byte i = 0; i < right.length()-1; i++){
      if(right[i] == '(')
        parCount++;
      else if(right[i] == ')')
        parCount--;
    }
    if (parCount == 1)
      right = right.substring(1, right.length()-1);
*/
/*------------------------------------------------------------------------- remove me plz
    int height = countHeight(expr, fontSize);
    int basePixels = countPixels(left, x+5*fontSize, y-5*fontSize-height, fontSize/2,foreColor, tft);
    int numPixels = countPixels(right, x+5*fontSize, y+2*fontSize, fontSize/2, foreColor,tft);
    int maxPix = max(basePixels, numPixels);
    
    drawChar(charSqrt,x,y+height/2,fontSize, foreColor, tft);
    tft.fillRect(x+5*fontSize, y-height, maxPix, fontSize,foreColor);
    tft.fillRect(x+4*fontSize, y-height+fontSize, fontSize,height+2*fontSize,foreColor);
    tft.fillTriangle(x+5*fontSize, y-height, 
                         x+4*fontSize, y-height+fontSize,
                         x+5*fontSize, y-height+fontSize,
                         foreColor);
    return basePixels +4*fontSize+ numPixels;
  }

  else if (idxSin != -1){
    String right = expr.substring(idxSin+1);
    drawChar(charS, x,y,fontSize,foreColor,tft);
    drawChar(charI, x+5*fontSize,y,fontSize,foreColor,tft);
    drawChar(charN, x+12*fontSize,y,fontSize,foreColor,tft);
    
    return 28*fontSize+countPixels(right, x+24*fontSize,y,fontSize,foreColor,tft);
  }
  
  else if (idxCos != -1){
    String right = expr.substring(idxCos+1);
    drawChar(charC, x,y,fontSize,foreColor,tft);
    drawChar(charO, x+7*fontSize+fontSize/3,y,fontSize,foreColor,tft);
    drawChar(charS, x+14*fontSize+2*fontSize/3,y,fontSize,foreColor,tft);
    return 28*fontSize+countPixels(right, x+24*fontSize,y,fontSize,foreColor,tft);
  }
  
  else if (idxTan != -1){
    String right = expr.substring(idxTan+1);
    drawChar(charT, x,y,fontSize,foreColor,tft);
    drawChar(charA, x+7*fontSize+fontSize/3,y,fontSize,foreColor,tft);
    drawChar(charN, x+14*fontSize+2*fontSize/3,y,fontSize,foreColor,tft);
    return 28*fontSize+countPixels(right, x+24*fontSize,y,fontSize,foreColor,tft);
  }
  
  else if (idxLog != -1){
    int i = searchSplittingComma(expr, idxLog);
    String b = expr.substring(2, i);
    String a = expr.substring(i+1, expr.length()-1);
    int zz = 22*fontSize;
    drawChar(charL, x,y,fontSize,foreColor,tft);
    drawChar(charO, x+6*fontSize+fontSize/3,y,fontSize,foreColor,tft);
    drawChar(charG, x+14*fontSize+2*fontSize/3,y,fontSize,foreColor,tft);
    int bb = countPixels(b,x+zz,y+6*fontSize+countHeight(b,fontSize/2)/2,fontSize/2,foreColor,tft);
    return zz+bb + countPixels(a, x+zz+bb+2*fontSize,y,fontSize,foreColor,tft);
  }
  
  else if(idxSum != -1){
    String ret = splitSigma(expr, idxSum);
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
    byte newFont = (fontSize/1.5);
    
    drawChar(charSigma, x, y, fontSize, foreColor,tft);
    //String xxx = _var + (String)"="+_start;
    int heightStart = countHeight(_start, fontSize/2);
    int heightEnd = countHeight(_end, fontSize/2);
    int endLen = countPixels(_end, x, y-10*newFont-heightEnd, newFont, foreColor,tft);
    
    int startLen = countPixels(_start, x+countPixels(_var+"=", x,y+9*fontSize+heightStart/2, fontSize/2,foreColor,tft), y+9*fontSize-heightStart/2, fontSize/2, foreColor,tft);
    
    return max(startLen, endLen)+11*fontSize+countPixels('('+_func+')',max(startLen, endLen)+x+10*fontSize,y+fontSize*2,fontSize/2,foreColor,tft);
  }
  
  else if(expr[0] == '('){
    String zz = expr.substring(1, expr.length()-1);
    drawChar(charOpeningParenthesis, x, y, fontSize, foreColor,tft);
    
    int midPix = countPixels(zz, x+6*fontSize+fontSize/3, y, fontSize, foreColor,tft);
    drawChar(charClosingParenthesis, x+midPix+6*(fontSize-1), y, fontSize, foreColor, tft);
    return 6*fontSize+midPix;
  }
  return 0;
}

void drawChar(String charArr[], int x, int y, int newFont, uint16_t foreColor, Adafruit_TFTLCD tft){
  short resultI;
  short resultJ;
  byte val;
  
  for (byte i = 0; i < 9; i++){
    for (byte j = 0; j < charArr[i].length(); j++){
      val = charArr[i][j]-48;
      resultI = i*newFont;
      resultJ = j*newFont;
      switch(val){
        case 1:
          tft.fillRect(x+resultJ, y+resultI, newFont, newFont, foreColor);
        break;
        case 2:
          tft.fillTriangle(x+resultJ, y+resultI, 
                         x+resultJ+newFont-1, y+resultI,
                         x+resultJ+newFont-1, y+resultI+newFont-1, 
                         foreColor);
        break;

        case 3:
          tft.fillTriangle(x+resultJ, y+resultI, 
                         x+resultJ, y+resultI+newFont-1,
                         x+resultJ+newFont-1, y+resultI+newFont-1,
                         foreColor);
         break;
         case 4:
          tft.fillTriangle(x+resultJ+newFont-1, y+resultI, 
                         x+resultJ, y+resultI+newFont-1,
                         x+resultJ+newFont-1, y+resultI+newFont-1,
                         foreColor);
            break;
         case 5:
           tft.fillTriangle(x+resultJ, y+resultI, 
                         x+resultJ+newFont-1, y+resultI,
                         x+resultJ, y+resultI+newFont-1,
                         foreColor);
            break;
         default:
           
         break;
      }
    }
  }
}
*/
