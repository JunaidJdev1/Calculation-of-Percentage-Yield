def calculate_percent_yield():
    try:
        actual_yield = float(input("Enter Actual Yield: "))
        mass = float(input("Enter Mass: "))
        molar_mass = float(input("Enter Molar Mass: "))
        molar_mass_product = float(input("Enter Molar Mass of Product: "))

        moles = mass / molar_mass
        theoretical_yield = moles * molar_mass_product
        percent_yield = (actual_yield / theoretical_yield) * 100

        print("Percent Yield: {:.2f}%".format(percent_yield))

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    except ZeroDivisionError:
        print("Cannot divide by zero. Please check your inputs.")

calculate_percent_yield()
