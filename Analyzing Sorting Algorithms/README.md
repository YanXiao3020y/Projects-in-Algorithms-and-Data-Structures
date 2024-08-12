# Analyzing Sorting Algorithms

### Overview
Implementing and evaluating different sorting algorithms through experiments to assess their real-world execution times.

### Phase 1 - Source Code 

-   **Objective:** Implement various sorting algorithms.

-   **Algorithms to Implement:**

    1.  **Insertion-sort**

    2.  **Merge-sort**

    3.  **Shellsort (4 versions):**

        -   **Original Shell sequence**

        -   **A083318 sequence**

        -   **A003586 sequence**

        -   **A033622 sequence**

    4.  **Hybrid Sort (Merge-sort and Insertion-sort):**

        - H = n<sup>1/2</sup>
        - H = n<sup>1/4</sup> 
        - H = n<sup>1/6</sup>
       



### Phase 2 - Report

-   **Objective:** Experimentally evaluate the sorting algorithms and
    report the findings.

-   **Experiments:**

    -   Run each algorithm 5 to 10 times for a series of increasing input sizes (e.g., 100, 500, 1000, 2500, 5000, ...), across all input sequence types. 

    -  Calculate the average of the running times for each combination of algorithm, input size, and sequence, and plot the results using log-log plots.


-   **Input Distributions:**

    1.  Uniformly distributed permutations

    2.  Almost-sorted permutations

    3.  Reverse sorted permutation


### More Info
For additional details, please refer to the specification folder.