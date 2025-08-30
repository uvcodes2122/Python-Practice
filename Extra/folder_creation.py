import os

# Parent folder where folders will be created
parent_folder = "C:/Users/VASANT/Desktop/PythonPro/Python_Practice"  # change path as needed
os.makedirs(parent_folder, exist_ok=True)

# Function to add ordinal suffix
def ordinal(n):
    if 11 <= n % 100 <= 13:
        return f"{n}th"
    else:
        return f"{n}{['th','st','nd','rd','th','th','th','th','th','th'][n % 10]}"

# Loop for September 1st to 30th
for i in range(1, 31):
    folder_name = f"{ordinal(i)} Sept 2025"
    folder_path = os.path.join(parent_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created: {folder_path}")
