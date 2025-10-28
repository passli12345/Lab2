def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 69, 32)")

def get_user_input():
    user_input = input()
    str_list = user_input.split(",")
    float_list = [float(num.strip()) for num in str_list]
    return float_list

def calc_average_temperature(temp_list):
    return sum(temp_list) / len(temp_list)

def calc_min_max_temperature(temp_list):
    return [min(temp_list), max(temp_list)]

def sort_temperature(temp_list):
    return sorted(temp_list)

def calc_median_temperature(temp_list):
    sorted_list = sort_temperature(temp_list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]

def main():
    print("ET0735 Lab2")
    display_main_menu()
    temp_list = get_user_input()
    
    avg = calc_average_temperature(temp_list)
    min_max = calc_min_max_temperature(temp_list)
    sorted_list = sort_temperature(temp_list)
    median = calc_median_temperature(temp_list)

    print(f"Average Temperature: {avg:.2f}")
    print(f"Minimum Temperature: {min_max[0]}")
    print(f"Maximum Temperature: {min_max[1]}")
    print(f"Sorted Temperatures: {sorted_list}")
    print(f"Median Temperature: {median:.2f}")

def calc_median_temperature(temp_list):
    sorted_list = sorted(temp_list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        median = sorted_list[mid]
    return median

if __name__ == "__main__":
    main()