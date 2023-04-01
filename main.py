from utils import load_data, sort_data, sort_operations, final_form


def main():
    count_operations = 5
    filtered_empty_from = True

    data = load_data()
    data = sort_data(data, filtered_empty_from)
    data = sort_operations(data, count_operations)
    data = final_form(data)

    for i in data:
        print(i, end='\n')


if __name__ == "__main__":
    main()