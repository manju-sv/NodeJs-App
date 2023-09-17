# Define a list of wordy versions for numbers from 10 to 100
wordy_numbers = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "one hundred"]

# Loop through numbers from 0 to 100
for i in range(101):
    if i % 10 == 0 and i != 0:
        # Print the wordy version for every tenth number
        print(wordy_numbers[i // 10])
    else:
        # Print the number itself for other numbers
        print(i)
