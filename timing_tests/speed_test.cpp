// C++ speed test
// Note that optimizations (-O0 to -O3) give very different results

#include <iostream>
#include <chrono>

long sum_of_array(int* array, int len) {
    volatile long sum = 0;
    for (int i = 0; i < len; i++) {
        sum += array[i];
    }
    return sum;
}


int main() {

    int len = 100000;
    int array[len] {};
    for (int i = 0; i < len; i++) {
        array[i] = i;
    }

    volatile long sum;    

    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < 10000; i++) {
        
        sum = sum_of_array(array, len);
        
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    int time = duration.count();
    time /= 10000;

    std::cout << "Sum: " << sum << std::endl;
    
    std::cout << "Average execution time: " << time << " microseconds." << std::endl;

    return 0;

}