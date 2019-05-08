#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <cmath>

using namespace std;

const float pi=3.141519265359;
const float epsilon=0.7;
const float dt=0.01;
const float dx=0.01;
const float beta=epsilon*dt/dx;
const float T=2;
const float L=1;
const int Nt=T/dt + 1;
const int Nx=L/dx + 1;

void solucion(void);

int main(){
    solucion();
    return 0;
}

void solucion(void){
    float U[Nx][Nt]={0};
    for(int i=1; i<Nx-1; i++){
            U[i][0]=0.05*sin(pi*i*4/(Nx-1));
    }
    for(int j=0; j<Nt-1; j++){
        for(int i=1; i<Nx-1; i++){
            U[i][j+1]=U[i][j]-0.25*beta*(U[i+1][j]*U[i+1][j] - U[i-1][j]*U[i-1][j]) + 0.125*beta*beta*((U[i+1][j] + U[i][j])*(U[i+1][j]*U[i+1][j] - U[i][j]*U[i][j])-(U[i][j] + U[i-1][j])*(U[i][j]*U[i][j] - U[i-1][j]*U[i-1][j]));
        }
    }
    ofstream outfile;
    outfile.open("datos.txt");
    for(int j=0; j<Nt;j++){
        for(int i=0;i<Nx;i++){
                outfile<<U[i][j]<<endl;
        }
    }
    outfile.close();
    

}