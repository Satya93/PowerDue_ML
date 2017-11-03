#include "Ml.h"
#include <Arduino.h>

int *buff = 0;

void Ml::clear_all()
{
  _cnt = 0;
  _sum = 0;
  _min = 0.0;
  _max = 0.0;
  _stddev = 0.0;
  _pin = 4;
  _old = 0;
  randomSeed(48);
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
  //-------------------------------------------------
  //Slope Calculations
  //-------------------------------------------------
  _del = f-_old;
  _old = f;
  /*SerialUSB.print("Count : ");
  SerialUSB.println(_cnt);
  SerialUSB.print("Minimum Value : ");
  SerialUSB.println(_min);
  SerialUSB.print("Maximum Value : ");
  SerialUSB.println(_max);
  SerialUSB.print("Sum : ");
  SerialUSB.println(_sum);
  */SerialUSB.print("Mean : ");
  SerialUSB.println(_mean);/*
  SerialUSB.print("Standard Deviation : ");
  SerialUSB.println(_stddev);*/
  //SerialUSB.print("Change in readings : ");
  //SerialUSB.println(_del);
  //SerialUSB.print("Target Value : ");
  //SerialUSB.println(calc_val);
  //SerialUSB.print("Err : ");
  //SerialUSB.println(_err/_cnt);
  //SerialUSB.println(" ");
}

void Ml::sample(int s)
{
  buff = (int*) malloc(s * sizeof(int));
  int curr_val;
  int mx_cnt = s;
  _mx_cnt = s;
    
  while(s>0){
    curr_val = get_data();
    append(curr_val);
    buff[mx_cnt-s] = curr_val;
    s--;
  }
  int i = 0;
  while(i<mx_cnt-1)
  { 
    SerialUSB.println(buff[i]);
    i++;
  }
}

int Ml::get_data()
{
  //Insert logic to get data
  //return analogRead(4);
  //append(5);
  int randi;
  randi = random(10,100);
  //SerialUSB.println(randi);
  return randi;
}

void Ml::regression()
{
  float err = 1000; 
  float m = 0;
  float c = _mean;
  float calc_val;
  float alpha = 0.0005;
  float err_1;
  float err_0;
  float toterr_0;
  float toterr_1;
  double cost = 1000; // Power and accuracy comparison using double and float
  int i = 0;
  float olderr;
  
  SerialUSB.println("Regression");
  SerialUSB.println(_mx_cnt);
  while(cost>0.0000002){
    olderr = cost;
    cost = 0;
    i = 0;
    toterr_1 = 0;
    toterr_0 = 0;
    while(i<_mx_cnt){
      calc_val = m*(i+1) + c;
      cost = ((calc_val-buff[i])*(calc_val-buff[i]));
      err_0 = (calc_val-buff[i]);
      err_1 = err_0*i;
      toterr_0 += err_0;
      toterr_1 += err_1;
      i++;
    }
    cost = cost/(2*i);
    if(olderr<cost){
      SerialUSB.print("Old Error is : ");
      SerialUSB.println(olderr);
      SerialUSB.print("New Error is : ");
      SerialUSB.println(cost);
      i = 0;
      while(i<_mx_cnt){
      SerialUSB.print("Original Value : ");
      SerialUSB.print(buff[i]);
      SerialUSB.print(" Derived Value : ");
      SerialUSB.println(m*(i+1)+c);
      i++;
      }
      break;
    }
    int boost; 
    if(cost==1000){
      //boost = 0.0001;
    }
    else{
      //boost = abs(olderr - err);  
    }
    m = m - (alpha*boost*toterr_1/i);
    c = c - (alpha*boost*toterr_0/i);
    SerialUSB.print("For Slope : ");
    SerialUSB.print(m);
    SerialUSB.print(" and Intercept : ");
    SerialUSB.print(c);
    SerialUSB.print(", Error is : ");
    SerialUSB.println(cost);
    delay(10);
  }
  i = 0;
  while(i<_mx_cnt){
      SerialUSB.print("Original Value : ");
      SerialUSB.print(buff[i]);
      SerialUSB.print(" Derived Value : ");
      SerialUSB.println(m*(i+1)+c);
      i++;
 }
  
}
