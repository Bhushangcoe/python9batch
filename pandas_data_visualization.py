import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = {
        "Name": ["Bhushan", "Sneha", "Raj", "Priya", "Yash", "Nikita"],
        "Department": ["IT", "HR", "Finance", "IT", "Sales", "IT"],
        "Salary": [45000, 52000, 48000, 60000, 43000, 55000],
    }

    df = pd.DataFrame(data)

    print("Employee Records:")
    print(df)

    average_salary = df["Salary"].mean()
    print(f"\nAverage Salary: {average_salary:.2f}")

    high_salary_employees = df[df["Salary"] >= 50000]
    print("\nEmployees with salary >= 50000:")
    print(high_salary_employees)

    department_total = df.groupby("Department")["Salary"].sum().sort_values(ascending=False)
    print("\nDepartment-wise Salary:")
    print(department_total)

    department_total.plot(kind="bar", color="skyblue", title="Total Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Salary")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
