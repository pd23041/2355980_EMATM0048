# Project Description:
    This project implements a coffee shop management system by writing several Python classes.

    Includes five modules: Barista Management System, Raw Material Control Labor Management System, Supplier System, Shop Operation Simulation System, and Input Judgment Script.

    Realize the following functions: 
      1. Barista Recruitment and Termination System, control the number of recruits and terminators to ensure that there is at least one person on the job, and at the same time, ensure that the number of people is entered correctly.
      2. Input monthly sales demand and make real-time adjustments based on labor and costs, while ensuring that the input is within the correct range.
      3. Update month end warehouse inventory based on monthly sales. Update the material inventory at the beginning of the next month based on losses, and use this as a basis for determining the price of the ingredients to be purchased.
      4. Calculate month-end cash balances based on income, rent, personnel expenses, purchasing expenses, storage costs, and coffee revenue factors. Judge next month's purchasing expenses against last month's cash balance to determine if the business can continue.

# Environmental Dependency
    python 3.10

# Project Structure
    ├── README.md                      // help
    ├── Barista.py                     // Barista management
    ├── Materials.py                   // Materials and labour management
    ├── SupplierCost.py                // Supplier Management
    ├── coffee_shop.py                 // Coffee Operation Simulation
    ├── InputJudgment.py               // Judgment Input Functions
    └── main.py                        // Running Scripts

# Version Update
    V1.0.0：
      1. Realization of basic functions.
      2. Missing automatic simulation operation function.
    V1.0.1:
      1. Updated recruitment barista judgment logic to prevent interruptions caused by null values.
