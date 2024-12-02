print('sinh vien: Nguyễn Danh Ánh')
print('mssv:235752021610023')
print('##########')
class RomanToInteger:
    def __init__(self, roman):
        self.roman = roman
        self.roman_to_int_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def convert(self):
        total = 0
        prev_value = 0
        
        for char in reversed(self.roman):
            current_value = self.roman_to_int_map[char]
           
            if current_value < prev_value:
                total -= current_value
            
            else:
                total += current_value
            
            prev_value = current_value
        
        return total
    
roman_number = "ILV"  

converter = RomanToInteger(roman_number)

print("Số nguyên của", roman_number, "là:", converter.convert())

