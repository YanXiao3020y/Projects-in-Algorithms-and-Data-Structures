# Algorithmic Experiments of Real-World Phenomena

### Overview

Evaluating different graph algorithms through experiments to uncover
properties of real-world network models.

### Phase 1 - Source Code 

-   **Objective:** Implement graph algorithms.

-   **Algorithms to Implement:**

    1.  **Diameter Algorithm:** Determine the length of the longest path
        in the graph.

    2.  **Clustering-Coefficient Algorithm:** Calculate the ratio of three times the number of triangles over the number of paths of length 2.

    3.  **Degree-Distribution Algorithm:** Count the number of vertices
        for each possible degree in the graph.

-   **Graph Types:**

    1.  Erdos-Renyi random graphs G(n,p)  p = 2(ln n)/n ​.

    2.  Barabasi-Albert random graphs with d=5 (number of
        neighbors each new vertex chooses).

### Phase 2 - Report

-   **Objective:** Analyze the performance of implemented algorithms and
    study graph properties.

-   **Experiments:**

    -   **Diameter and Clustering Coefficients:** Test these on multiple
        random graphs of varying sizes n, and plot the average values
        on a lin-log scale. Determine how these values change (grow, decrease, or remain constant) with n, and if they grow proportionally to logn or at a
        different rate (grows faster or slower).

    -   **Degree Distribution:** For graphs vertices with n=1,000, n=10,000, and n=100,000, plot the degree distribution on both lin-lin and
        log-log scales. Determine if the distribution follows a power
        law, and find the slope of the power law if applicable.

### More Info
For additional details, please refer to the specification folder.