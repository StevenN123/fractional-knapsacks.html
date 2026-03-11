#  Fractional Knapsack Problem - Greedy Algorithm


A comprehensive implementation of the Fractional Knapsack problem using a greedy approach. This algorithm maximizes value by taking fractions of items based on value-to-weight ratio.

##  Problem Description

Given `n` items, each with a weight `wᵢ` and value `vᵢ`, and a knapsack with capacity `W`, find the maximum total value that can be placed in the knapsack. Unlike the 0/1 knapsack problem, you can take **fractions** of items.


### Example
**Input:**
- Items: (weight, value) = [(10, 60), (20, 100), (30, 120)]
- Capacity: 50

**Output:**
- Maximum value: 240
- Solution: Take item 1 (10,60), item 2 (20,100), and 2/3 of item 3 (20,80)

## ⚙️ Algorithm Analysis

### Time Complexity
- **Sorting:** O(n log n)
- **Greedy selection:** O(n)
- **Overall:** O(n log n)

### Space Complexity
- **Auxiliary Space:** O(1)

## 💻 Complete Python Implementation

### Basic Implementation
```python
def fractional_knapsack(items, capacity):
    """
    Solve fractional knapsack problem using greedy approach
    
    Args:
        items: List of tuples (weight, value)
        capacity: Maximum weight capacity
    
    Returns:
        tuple: (maximum_value, items_taken_details)
    """
    # Calculate value/weight ratio for each item
    items_with_ratio = []
    for weight, value in items:
        ratio = value / weight
        items_with_ratio.append((weight, value, ratio))
    
    # Sort by ratio in descending order
    items_with_ratio.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0
    remaining = capacity
    items_taken = []
    
    # Take items greedily
    for weight, value, ratio in items_with_ratio:
        if remaining >= weight:
            # Take whole item
            total_value += value
            remaining -= weight
            items_taken.append(f"Took whole item (weight:{weight}, value:{value})")
        else:
            # Take fraction of item
            fraction = remaining / weight
            total_value += value * fraction
            items_taken.append(f"Took {fraction:.2f} of item (value:{value * fraction:.2f})")
            break
    
    return total_value, items_taken
