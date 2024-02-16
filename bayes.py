import numpy as np

# Declare variables
outlook = np.zeros((5, 7))  # Initialize a NumPy array for outlook
yes = float(input("P(YES)\n"))
no = float(input("P(NO)\n"))

# Assign probabilities to outlook array
outlook[1, 1] = 2/9.0  # Sunny_Yes
outlook[1, 2] = 3/5.0  # Sunny_NO
outlook[1, 3] = 4/9.0  # Overcast_Yes
outlook[1, 4] = 0.0    # Overcast_No
outlook[1, 5] = 3/9.0  # Rain_Yes
outlook[1, 6] = 2/5.0  # Rain_NO

outlook[2, 1] = 2/9.0  # Hot_Yes
outlook[2, 2] = 2/5.0  # HOt_NO
outlook[2, 3] = 4/9.0  # Mild_Yes
outlook[2, 4] = 2/5.0  # Mild_No
outlook[2, 5] = 3/9.0  # Cool_Yes
outlook[2, 6] = 1/5.0  # Cool_NO

outlook[3, 1] = 3/9.0  # High_Yes
outlook[3, 2] = 4/5.0  # High_NO
outlook[3, 3] = 6/9.0  # Normal_Yes
outlook[3, 4] = 1/5.0  # Normal_No

outlook[4, 1] = 3/9.0  # True_Yes
outlook[4, 2] = 3/5.0  # True_NO
outlook[4, 3] = 6/9.0  # False_Yes
outlook[4, 4] = 2/5.0  # False_NO

# Get user input for conditions
out = input("Enter the Outlook\n")
temp = input("Enter the Temperature\n")
hu = input("Enter the Humidity\n")
wi = input("Enter the windluy\n")

# Update probabilities based on conditions
if out == "sunny":
   yes *= outlook[1, 1]
   no *= outlook[1, 2]
elif out == "overcast":
   yes *= outlook[1, 3]
   no *= outlook[1, 4]
elif out == "rainy":  # Corrected from "humidity"
   yes *= outlook[1, 5]
   no *= outlook[1, 6]

if temp == "hot":
   yes *= outlook[2, 1]
   no *= outlook[2, 2]
elif temp == "mild":
   yes *= outlook[2, 3]
   no *= outlook[2, 4]
elif temp == "cool":
   yes *= outlook[2, 5]
   no *= outlook[2, 6]

if hu == "high":
   yes *= outlook[3, 1]
   no *= outlook[3, 2]
elif hu == "normal":
   yes *= outlook[3, 3]
   no *= outlook[3, 4]

if wi == "true":
   yes *= outlook[4, 1]
   no *= outlook[4, 2]
elif wi == "false":
   yes *= outlook[4, 3]
   no *= outlook[4, 4]

# Normalize probabilities
a = yes / (yes + no)
b = no / (yes + no)

# Print results
print("NB(yes)", yes)
print("NB(no)", no)
print("Normalization Form")
print("NB(yes)", a)
print("NB(no)", b)
