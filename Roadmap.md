python
1. from typing import List

def calculate_total_cost(items: List[float]) -> float:
    """
    Calculate the total cost of items.
    
    Parameters:
    - items (List[float]): A list of item costs.
    
    Returns:
    - float: The total cost of the items.
    """
    return sum(items)

if __name__ == "__main__":
    # Example usage
    expenses = [10.5, 24.9, 37.8]
    print(f"The total cost is: ${calculate_total_cost(expenses)}")