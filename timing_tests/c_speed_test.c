// C speed test
// Note that optimizations (-O0 to -O3) give very different results

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_SIZE 100000

// Function to get high-resolution time
double get_time() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1e6 + ts.tv_nsec / 1e3;  // Convert to microseconds
}

int main() {
    int *arr = malloc(ARRAY_SIZE * sizeof(int));
    if (!arr) {
        perror("Memory allocation failed");
        return 1;
    }

    // Fill the array with values
    for (int i = 0; i < ARRAY_SIZE; i++) {
        arr[i] = i;
    }

    printf("%i\n", arr[ARRAY_SIZE - 1]);

    // Start timing
    double start_time = get_time();

    // Sum the array
    int num_iterations = 10000;
    volatile long sum;
    for (int i = 0; i < num_iterations; i++) {
        sum = 0;
        for (int i = 0; i < ARRAY_SIZE; i++) {
            sum += arr[i];
        }
    }

    // End timing
    double end_time = get_time();

    double result = (end_time - start_time) / num_iterations;

    printf("Sum: %ld\n", sum);
    printf("Time taken: %.2f microseconds\n", result);

    free(arr);  // Free allocated memory
    return 0;
}
