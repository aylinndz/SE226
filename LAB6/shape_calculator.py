import geometry_utils


def main():
    operations = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }

    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: area, perimeter (e.g., circle_area)")

    choice = input("Enter the operation : ")

    if choice not in operations:
        print("Invalid operation.")
        return

    if "circle" in choice:
        radius = float(input("Enter radius: "))
        if radius <= 0:
            print("Input Error: Dimensions must be strictly positive.")
        else:
            result = operations[choice](radius)
            print("result:", result)

    elif "rectangle" in choice:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))

        if  height <=  0 or width <= 0:
            print("Input Error: Dimensions must be strictly positive.")
        else:
            result = operations[choice](width, height)
            print("result:", result)

    elif "triangle" in choice:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))

        if  height <= 0 or base <= 0 :
            print("Input error: Dimensions must be strictly positive.")
        else:
            result = operations[choice](base, height)
            print("result:", result)


if __name__ == "__main__":
    main()


