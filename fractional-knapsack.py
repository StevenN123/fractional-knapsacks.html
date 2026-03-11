def fractional_knapsack(items, capacity):
    """
    Solve fractional knapsack problem using greedy approach
    
    Args:
        items: List of tuples (weight, value)
        capacity: Maximum weight capacity
    
    Returns:
        tuple: (maximum_value, items_taken_details)
    """
    # Step 1: Calculate value/weight ratio for each item
    print("Step 1: Calculating value/weight ratios...")
    items_with_ratio = []
    for i, (weight, value) in enumerate(items):
        ratio = value / weight
        items_with_ratio.append((weight, value, ratio, i+1))
        print(f"  Item {i+1}: weight={weight}, value={value}, ratio={ratio:.2f}")
    
    # Step 2: Sort items by ratio in descending order
    print("\nStep 2: Sorting items by ratio (highest first)...")
    items_with_ratio.sort(key=lambda x: x[2], reverse=True)
    for weight, value, ratio, idx in items_with_ratio:
        print(f"  Item {idx}: ratio={ratio:.2f}")
    
    total_value = 0
    remaining = capacity
    items_taken = []
    
    # Step 3: Take items greedily
    print("\nStep 3: Greedy selection process:")
    for weight, value, ratio, idx in items_with_ratio:
        if remaining >= weight:
            # Take whole item
            total_value += value
            remaining -= weight
            items_taken.append(f"Item {idx}: 100% (weight:{weight}, value:{value})")
            print(f"  ✓ Take Item {idx} completely: +{value} value, {remaining} capacity left")
        else:
            # Take fraction of item
            fraction = remaining / weight
            fractional_value = value * fraction
            total_value += fractional_value
            items_taken.append(f"Item {idx}: {fraction:.1%} (weight:{remaining}, value:{fractional_value:.2f})")
            print(f"  → Take {fraction:.1%} of Item {idx}: +{fractional_value:.2f} value, knapsack full")
            break
    
    return total_value, items_taken

def fractional_knapsack_detailed(items, capacity):
    """
    Enhanced version with more detailed output for learning
    """
    print("=" * 60)
    print("FRACTIONAL KNAPSACK ALGORITHM - DETAILED WALKTHROUGH")
    print("=" * 60)
    
    n = len(items)
    print(f"Number of items: {n}")
    print(f"Knapsack capacity: {capacity}")
    print("\nInitial items:")
    print("-" * 40)
    print(f"{'Item':<6} {'Weight':<8} {'Value':<8} {'Ratio':<8}")
    print("-" * 40)
    
    # Calculate ratios
    items_with_info = []
    for i, (w, v) in enumerate(items, 1):
        ratio = v / w
        items_with_info.append((i, w, v, ratio))
        print(f"{i:<6} {w:<8} {v:<8} {ratio:<8.2f}")
    
    # Sort by ratio
    items_with_info.sort(key=lambda x: x[3], reverse=True)
    
    print("\n" + "=" * 60)
    print("STEP 1: SORT ITEMS BY VALUE/WEIGHT RATIO")
    print("=" * 60)
    print(f"{'Item':<6} {'Weight':<8} {'Value':<8} {'Ratio':<8}")
    print("-" * 40)
    for i, w, v, ratio in items_with_info:
        print(f"{i:<6} {w:<8} {v:<8} {ratio:<8.2f}")
    
    print("\n" + "=" * 60)
    print("STEP 2: GREEDY SELECTION PROCESS")
    print("=" * 60)
    
    remaining = capacity
    total_value = 0
    selection = []
    
    for i, w, v, ratio in items_with_info:
        if remaining == 0:
            break
            
        if w <= remaining:
            # Take whole item
            total_value += v
            remaining -= w
            selection.append((i, 1.0, w, v))
            print(f"\n✓ Take Item {i} completely:")
            print(f"  Weight: {w} (fits in remaining {remaining + w})")
            print(f"  Value added: +{v}")
            print(f"  Remaining capacity: {remaining}")
        else:
            # Take fraction
            fraction = remaining / w
            fractional_value = v * fraction
            total_value += fractional_value
            selection.append((i, fraction, remaining, fractional_value))
            print(f"\n→ Take {fraction:.2%} of Item {i}:")
            print(f"  Weight taken: {remaining} (all remaining capacity)")
            print(f"  Value added: +{fractional_value:.2f}")
            remaining = 0
            print(f"  Remaining capacity: {remaining}")
            break
    
    print("\n" + "=" * 60)
    print("FINAL RESULTS")
    print("=" * 60)
    print(f"Total value achieved: {total_value:.2f}")
    print("\nItems taken:")
    for item in selection:
        if item[1] == 1.0:
            print(f"  • Item {item[0]}: 100% (weight: {item[2]}, value: {item[3]})")
        else:
            print(f"  • Item {item[0]}: {item[1]:.1%} (weight: {item[2]}, value: {item[3]:.2f})")
    
    return total_value

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic example
    items1 = [(10, 60), (20, 100), (30, 120)]
    capacity1 = 50
    
    max_value, taken = fractional_knapsack(items1, capacity1)
    
    print("\n" + "=" * 60)
    print("BASIC EXAMPLE RESULTS")
    print("=" * 60)
    print(f"Maximum value: {max_value}")
    print("Items taken:")
    for item in taken:
        print(f"  {item}")
    
    # Test case 2: More complex example
    print("\n" + "=" * 60)
    print("TEST CASE 2: More Items")
    print("=" * 60)
    items2 = [(5, 30), (10, 40), (15, 45), (22, 77), (25, 90)]
    capacity2 = 60
    
    max_value2, taken2 = fractional_knapsack(items2, capacity2)
    print(f"\nMaximum value: {max_value2}")
    
    # Run detailed walkthrough
    fractional_knapsack_detailed(items1, capacity1)
