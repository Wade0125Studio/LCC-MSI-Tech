import math

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("輸入無效，請嘗試再次輸入。")

def calculate(x, y, operator):
    try:
        if operator == '+':
            return x + y
        elif operator == '-':
            return x - y
        elif operator == '*':
            return x * y
        elif operator == '/':
            if y == 0:
                return "除數不能為零"
            return x / y
        elif operator == '**':
            return x ** y
        elif operator == 'sqrt':
            return math.sqrt(x)
        elif operator == 'cbrt':
            return x ** (1/3)
        elif operator == '%':
            if y == 0:
                return "除數不能為零"
            return x % y
        elif operator == 'exp':
            return math.exp(x)
        elif operator == 'sin':
            return math.sin(math.radians(x))
        elif operator == 'cos':
            return math.cos(math.radians(x))
        elif operator == 'tan':
            return math.tan(math.radians(x))
        else:
            return "無效的操作符"
    except ValueError:
        return "輸入無效"

while True:
    print("選擇運算:")
    print("1. 加法")
    print("2. 減法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 次方計算")
    print("6. 平方根")
    print("7. 立方根")
    print("8. 餘數計算")
    print("9. e的次方")
    print("10. 科學計數法輸入")
    print("11. 正弦值")
    print("12. 余弦值")
    print("13. 正切值")
    print("14. 退出")

    choice = input("請選擇 (1/2/3/4/5/6/7/8/9/10/11/12/13/14): ")

    if choice == '14':
        print("程式已退出")
        break

    if choice in ('1', '2', '3', '4', '5', '8', '9', '10'):
        if choice != '6' and choice != '7' and choice != '10':
            num1 = get_number_input("輸入第一個數: ")
        if choice != '6' and choice != '7' and choice != '10':
            num2 = get_number_input("輸入第二個數: ")

        if choice in ('1', '2', '3', '4', '5', '8', '9'):
            operator = ''
            if choice == '1':
                operator = '+'
            elif choice == '2':
                operator = '-'
            elif choice == '3':
                operator = '*'
            elif choice == '4':
                operator = '/'
            elif choice == '5':
                operator = '**'
            elif choice == '8':
                operator = '%'
            elif choice == '9':
                operator = 'exp'

            result = calculate(num1, num2, operator)
            print("結果: ", result)
        
        elif choice == '6':
            result = calculate(num1, None, 'sqrt')
            print("結果: ", result)
        
        elif choice == '7':
            result = calculate(num1, None, 'cbrt')
            print("結果: ", result)
        
        elif choice == '10':
            num = input("輸入一個數 (科學計數法表示): ")
            try:
                num = float(num)
                print("結果: ", num)
            except ValueError:
                print("輸入無效")
    
    elif choice in ('11', '12', '13'):
        num = float(input("輸入角度: "))
        operator = ''
        if choice == '11':
            operator = 'sin'
        elif choice == '12':
            operator = 'cos'
        elif choice == '13':
            operator = 'tan'
        
        result = calculate(num, None, operator)
        print(f"結果: {operator}({num}) = {result}")
    
    else:
        print("無效的選擇")

    continue_choice = input("是否繼續？(輸入 'y' 繼續，否則案任意鍵退出退出): ")
    if continue_choice.lower() != 'y':
        print("程式已退出")
        break
