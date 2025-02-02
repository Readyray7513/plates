## Vanity Plate Validator  

This program checks whether a user-inputted vanity plate meets specific requirements. If the plate follows the rules, the program prints **"Valid"**, otherwise, it prints **"Invalid"**.  

### **Rules for a Valid Plate**  
✅ Must be **between 2 and 6 characters long**  
✅ Must **start with at least two letters**  
✅ Can contain numbers, but **numbers must appear only at the end**  
✅ The first number **cannot be '0'**  
✅ **No punctuation, spaces, or special characters**  

### **How to Use**  
1. Run the program:  
   python plates.py
2. Enter a potential vanity plate when prompted.  
3. The program will return **"Valid"** if it follows the rules, otherwise **"Invalid"**.  

### **Example Inputs & Outputs**  
| Input  | Output  |
|--------|--------|
| `CS50`  | Valid  |
| `H`  | Invalid  |
| `AAA22A`  | Invalid  |
| `OUTATIME`  | Invalid  |
| `PI3.14`  | Invalid  |  

This program ensures vanity plates follow proper format rules before approval! 🚗💨
