#include <iostream>
using namespace std;

int main() {
    // Pointer declaration
    int *ptr;
    // Dynamic memory allocation
    ptr = new int;

    // Assigning value to allocated memory
    *ptr = 42;
    cout << "Value pointed by ptr: " << *ptr << endl;

    // Freeing allocated memory
    delete ptr;
    return 0;
}
