from data_package import strip_whitespaces, remove_duplicates, calculate_mean, find_maximum, find_minimum

def main():
    raw = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8, 21): ")

    stringlist = raw.split(',')

    cleaned = strip_whitespaces(stringlist)

    try:
        numlist = [float(num) for num in cleaned if num]
    except ValueError:
        print("Data Error: Please make sure you only enter numbers separated by commas.")
        return

    unique_data = remove_duplicates(numlist)

    print("Cleaned and unique data:", unique_data)
    print("Mean:", calculate_mean(unique_data))
    print("Maximum:", find_maximum(unique_data))
    print("Minimum:", find_minimum(unique_data))

if __name__ == "__main__":
    main()
