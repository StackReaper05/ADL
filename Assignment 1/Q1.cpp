#include <iostream>
using namespace std;
int MP_Neuron(int inputs[], int weights[], int n, int threshold)
{
    int sum = 0;

    for (int i = 0; i < n; i++)
    {
        sum = sum + inputs[i] * weights[i];
    }
    if (sum >= threshold)
        return 1;
    else
        return 0;
}

// AND Gate
int AND(int x1, int x2)
{
    int inputs[] = {x1, x2};
    int weights[] = {1, 1};

    return MP_Neuron(inputs, weights, 2, 2);
}

// OR Gate
int OR(int x1, int x2)
{
    int inputs[] = {x1, x2};
    int weights[] = {1, 1};

    return MP_Neuron(inputs, weights, 2, 1);
}

// NOR Gate
int NOR(int x1, int x2)
{
    int inputs[] = {x1, x2};
    int weights[] = {-1, -1};

    return MP_Neuron(inputs, weights, 2, 0);
}

// NOT Gate
int NOT(int x)
{
    int input[] = {x};
    int weight[] = {-1};

    return MP_Neuron(input, weight, 1, 0);
}

int main()
{
    cout << "AND Gate" << endl;
    cout << "0 AND 0 = " << AND(0, 0) << endl;
    cout << "0 AND 1 = " << AND(0, 1) << endl;
    cout << "1 AND 0 = " << AND(1, 0) << endl;
    cout << "1 AND 1 = " << AND(1, 1) << endl;

    cout << "\nOR Gate" << endl;
    cout << "0 OR 0 = " << OR(0, 0) << endl;
    cout << "0 OR 1 = " << OR(0, 1) << endl;
    cout << "1 OR 0 = " << OR(1, 0) << endl;
    cout << "1 OR 1 = " << OR(1, 1) << endl;

    cout << "\nNOR Gate" << endl;
    cout << "0 NOR 0 = " << NOR(0, 0) << endl;
    cout << "0 NOR 1 = " << NOR(0, 1) << endl;
    cout << "1 NOR 0 = " << NOR(1, 0) << endl;
    cout << "1 NOR 1 = " << NOR(1, 1) << endl;

    cout << "\nNOT Gate" << endl;
    cout << "NOT 0 = " << NOT(0) << endl;
    cout << "NOT 1 = " << NOT(1) << endl;

    return 0;
}