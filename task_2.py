def find_max_divide_conquer(arr, start=0, end=None):
    
    if end is None:
        end = len(arr) - 1
    
    
    if start > end:
        raise ValueError("Список пуст, максимум не определён")
    
    
    if start == end:
        return arr[start]
    
    
    mid = (start + end) // 2
    
    
    max_left = find_max_divide_conquer(arr, start, mid)
    max_right = find_max_divide_conquer(arr, mid + 1, end)
    
    
    return max(max_left, max_right)


if __name__ == "__main__":
    sample_list = [3, 7, 2, 9, 1, 8, 5]
    result = find_max_divide_conquer(sample_list)
    print(f"Максимальный элемент: {result}")  