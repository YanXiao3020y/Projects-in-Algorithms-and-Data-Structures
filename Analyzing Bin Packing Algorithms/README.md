# Analyzing Bin Packing Algorithms

### Overview

Evaluating different bin packing algorithms through experiments to
assess the quality of the solutions they generate.

### 

### Phase 1 - Source Code 

-   **Objective:** Implement various bin-packing algorithms.

-   **Algorithms to Implement:**

    1.  **Next Fit (NF)**

    2.  **First Fit (FF)**

    3.  **Best Fit (BF)**

    4.  **First Fit Decreasing (FFD)**

    5.  **Best Fit Decreasing (BFD)**

-   **Requirements:**

    1.  Implement each algorithm using a balanced binary search tree
        known as a **zip-zip tree**.

    2.  Ensure that First Fit and Best Fit methods (including their
        decreasing versions) run in expected time.


### Phase 2 - Report 

-   **Objective:** Experimentally evaluate the performance of the
    implemented bin-packing algorithms and analyze the quality of their
    solutions.

-   **Experiments:**

    -   Test each algorithm on lists of floating-point numbers between
        0.0 and 0.7, generated uniformly at random.

    -   Use bins of size 1.0.

    -   Determine the waste W(A) for each algorithm A as a
        function of nnn, where:

        -   W(A) = Number of bins used by algorithm A -(minus) Total
            size of all items in the list.

    -   Perform multiple tests for each input size n, allow n to
        grow, and plot the results on a log-log scale.

    -   Analyze if a best-fit line can be determined and calculate its
        slope.


### More Info
For additional details, please refer to the specification folder.