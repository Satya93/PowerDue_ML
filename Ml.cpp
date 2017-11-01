#include "Ml.h"
#include <Arduino.h>

void Ml::clear_all()
{
  _cnt = 0;
  _sum = 0;
  _min = 0.0;
  _max = 0.0;
  _stddev = 0.0;
  _pin = 4;
  randomSeed(5);
}

void Ml::append(float f)
{
  int dev;
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
  _mean = _sum/_cnt;
  dev = f-_mean;
  _stddev = (_stddev+dev)/_cnt;
  //SerialUSB.print("Count : ");
  //SerialUSB.println(_cnt);
  //SerialUSB.print("Minimum Value : ");
  //SerialUSB.println(_min);
  //SerialUSB.print("Maximum Value : ");
  //SerialUSB.println(_max);
  //SerialUSB.print("Sum : ");
  //SerialUSB.println(_sum);
  SerialUSB.print("Mean : ");
  SerialUSB.println(_mean);
  SerialUSB.print("Standard Deviation : ");
  SerialUSB.println(_stddev);
  SerialUSB.println(" ");
}

void Ml::sample(int s)
{
  while(s>0){
    append(get_data());
    s--;
  }
}

int Ml::get_data()
{
  //Insert logic to get data
  //return analogRead(4);
  int randi;
  randi = random(10,100);
  SerialUSB.println(randi);
  return randi;
}

