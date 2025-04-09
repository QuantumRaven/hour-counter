# hour-counter

The purpose of this repository is to simply count and give a total of the respective weekly_hours and weekly_minutes fields in the hours.csv file. I created this so I could quickly figure out how many toatl hours I worked at Uber.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installation

To use this on your own system(s), clone the repository:

```
git clone https://github.com/QuantumRaven/hour-counter.git
```

## Usage

Modify the following lines at the end of count_hours.py

```
file_name = "./hours.csv" # <--- Replace with your file name.
column_num = 0 <--- No change
column_sum = sum_csv(file_name, column_num) # <--- No change
print(column_sum) # <--- No change
```

Then simply call the file with:

```
python3 count_hours.py
```

