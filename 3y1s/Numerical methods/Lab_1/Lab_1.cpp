#include <iostream>
#include "config.h"
#include <cmath>

const int RowAm = 3;

void gaussianElimination(double A[RowAm][RowAm], double B[RowAm])
{
    double Multi1, Multi2;
    double Result[RowAm];

    std::cout << "Разложение ХолецкогоGaussian elimination" << std::endl;
    std::cout << std::endl;

    for(int i = 0; i < RowAm; i++) {
        for(int j = 0; j < RowAm; j++) {
            std::cout << A[i][j] << "\t";
        }
        std::cout << B[i] << std::endl;
    }
    std::cout << std::endl;

    for(int k = 0; k < RowAm; k++) {
        for(int j = k + 1; j < RowAm; j++) {
            Multi1 = A[j][k] / A[k][k];
            for(int i = k; i < RowAm; i++) {
                A[j][i] = A[j][i] - Multi1 * A[k][i];
            }
            B[j] = B[j] - Multi1 * B[k];
        }
    }

    for(int k = RowAm - 1; k >= 0; k--) {
        Multi1 = 0;
        for(int j = k; j < RowAm; j++) {
            Multi2 = A[k][j] * Result[j];
            Multi1 += Multi2;
        }
        Result[k] = (B[k] - Multi1) / A[k][k];
    }

    std::cout << std::endl;
    for(int i = 0; i < RowAm; i++) {
        for(int j = 0; j < RowAm; j++) {
            std::cout << round(A[i][j] * 10000) / 10000 << "\t";
        }
        std::cout << std::endl;
    }

    for(int i = 0; i < RowAm; i++) {
        std::cout << "X[" << i + 1 << "]=" << round(Result[i] * 10000) / 10000 << std::endl;
    }
}

void choleskyDecomposition(double A[RowAm][RowAm], double B[RowAm])
{
    double V [RowAm][ RowAm];
    double  C[RowAm][RowAm];
    double Y  [RowAm];
    double X [RowAm];

    std::cout << "Cholesky decomposition" << std::endl;
    std::cout << std::endl;

    for(int i = 0; i < RowAm; i++) {
        for(int j = 0; j < RowAm; j++) {

            std::cout << A[i][j] << "\t";
        }
        std::cout << B[i] << std::endl;
    }
    V[0][ 0] = A[0][0];
    C[0][0] = 1;
    C[0][1] = A[0][1] / A[0][0];
    C[0][2] = A[0][2] / A[0][0];
    V[1][0] = A[1][0];
    V[1][1] = A[1][1] - A[1][0] * C[0][1];
    C[1][1] = 1;
    C[1][2] = (A[1][2] - (V[1][0] * C[0][2])) / V[1][1];
    V[2][0] = A[2][0];
    V[2][1] = A[2][1] - (A[2][0] * C[0][1]);
    V[2][2] = A[2][2] - (A[2][0] * C[0][2] + V[2][1] * C[1][2]);
    C[2][2] = 1;
//    Console.WriteLine();
//    Console.WriteLine("Матрица B:");
    for(int i = 0; i < RowAm; i++) {
        for(int j = 0; j < RowAm; j++) {
            std::cout << round(V[i][j] * 1000) / 1000 << "\t";
        }
        std::cout << std::endl;
    }
//    Console.WriteLine();
//    Console.WriteLine("Матрица C:");
    for(int i = 0; i < RowAm; i++) {
        for(int j = 0; j < RowAm; j++) {

            std::cout << round(C[i][j] * 1000) / 1000 << "\t";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
//    Console.WriteLine("Вычисляем значения Yi");
    Y[0] = B[0] / V[0][0];
    Y[1] = (B[1] - (V[1][0] * Y[0])) / V[1][1];
    Y[2] = (B[2] - V[2][0] * Y[0] - V[2][1] * Y[1]) / V[2][2];
    for(int i = 0; i < RowAm; i++) {
        std::cout << "Y[" << i + 1 << "]=" << round(Y[i] * 1000) / 1000;
    }
    std::cout << std::endl;
//    Console.WriteLine("Вычисляем значения Xi");
    X[0] = Y[2];
    X[1] = Y[1] - (C[1][2] * Y[2]);
    X[2] = Y[0] - (C[0][1] * X[1] + C[0][2] * Y[2]);

    for(int i = 0; i < RowAm; i++) {
        std::cout <<  "X[" << i + 1 << "]=" << round(X[i] * 1000) / 1000;
    }
}

int main(int argc, char **argv) {
	std::cout << "Hello World!" << std::endl;
	std::cout << "Version " << Lab_1_VERSION_MAJOR << "." << Lab_1_VERSION_MINOR << std::endl;

	double A[RowAm][RowAm] = { { 1.54, 1.70, 1.62 }, { 3.69, 3.73, 3.59 }, { 2.45, 2.43, 2.25 } };
	double B[RowAm] = { -1.97, -3.74, -2.26 };
	gaussianElimination(A, B);
	choleskyDecomposition(A,B);

	return 0;
}
