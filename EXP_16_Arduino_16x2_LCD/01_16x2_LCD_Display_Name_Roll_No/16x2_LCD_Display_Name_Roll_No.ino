/*
 * Experiment 15 / 16: 16x2 LCD Interfacing using Arduino Development Board
 */
#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup()
{
  lcd.begin(16, 2);
  lcd.print("SNIKITHA");
  lcd.setCursor(0, 1);
  lcd.print("24B81A7745");
}

void loop()
{
  lcd.noDisplay();
  delay(500);
  lcd.display();
  delay(5000);
}
