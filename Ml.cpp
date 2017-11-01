#include "Ml.h"
#include <Arduino.h>

void Ml::clear_all()
{
  _cnt = 0;
  _sum = 0;
  _min = 0.0;
  _max = 0.0;
}

void Ml::append(float f)
{
  if(_cnt==0)
  {
    _min = f;
    _max = f;
  }
  else{
    if (f < _min){
      _min = f;
    }
    if (f > _max){
      _max = f;
    }
  }
  _sum += f;
  _cnt++;
  SerialUSB.print("Count : ");
  SerialUSB.println(_cnt);
  SerialUSB.print("Minimum Value : ");
  SerialUSB.println(_min);
  SerialUSB.print("Maximum Value : ");
  SerialUSB.println(_max);
  SerialUSB.print("Sum : ");
  SerialUSB.println(_sum);
  SerialUSB.print("Average : ");
  SerialUSB.println(_sum/_cnt);
  SerialUSB.println(" ");
}

