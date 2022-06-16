#include "Calc.h"
#include "BigNumMath.h"
#include "BigNumber.h"
#include "Simplifier.h"
#include "Simplifier.h"
#include "displayFuncs.h"
#include "CharsDef.h"
#include <Adafruit_GFX.h>
#include <TouchScreen.h>
#include <Adafruit_TFTLCD.h>

//SPI Communication
#define LCD_CS A3
#define LCD_CD A2
#define LCD_WR A1
#define LCD_RD A0
// optional
#define LCD_RESET A4

//Color Definitons
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
////////////////////////////////////////////////

extern BigNumber calc(String expr);
extern String approximate(BigNumber num);
//extern String moveCursor(String expr, int dir);
String expr = "";
Adafruit_TFTLCD tft(LCD_CS, LCD_CD, LCD_WR, LCD_RD, LCD_RESET);
int X = 0;
int Y = 0;

int curPos = 0;

void setup() {
  Serial.begin(9600);
  BigNumber::begin (50);
  BigNumber n = BigNumber(80);

  BigNumber result = nthRoot(BigNumber(9), n);
  Serial.println(result);
  
  tft.reset();
  tft.begin(tft.readID());
  tft.setRotation(5);
  // Background color
  tft.fillScreen(BLACK);
  //Serial.println(moveCursor("l(_2,8)", -1));
  //drawThing();
}

void loop() {
  /*
  short x = analogRead(A15);
  short y = analogRead(A14);
  
  if(x < 390 && x > 350 && y < 390 && y > 350)
    goto cont;
  // top left
  if(x > 600)
    Y += 36;
  if(x < 200)
    Y -= 36;

  if(y > 600)
    X -= 36;
  if(y < 200)
    X += 36;
  */
  tft.fillRect(0,0,340,280,BLACK);
  //tft.fillScreen(BLACK);
  drawThing();
  cont:
  ;
}

void drawThing(){
//  countPixels("l(2,8)*3", 10+X, 130+Y, 2, WHITE,tft);
}
