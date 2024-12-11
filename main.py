import random
from textwrap import wrap

quiz = {
    "Part 1: vba operators": {
        "Operator used to join two strings": "&",
        "Greater than operator": ">",
        "Greater than or equal operator": ">=",
        "Less than operator": "<",
        "Less than or equal operator": "<=",
        "Equal operator": "=",
        "Not equal operator": "<>",
        "Conditional logical operator where a single true makes the result true": "or",
        "Conditional logical operator where a single false makes the result false": "and",
        "Logical operator where truth value is converted to the opposite truth value": "not",
        "Floating point division operator": "/",
        "Integer division operator": "\\",
        "Power operator": "^"
    },
    "Part 2: Data Types": {
        "True or False": "Boolean",
        "January 1, 100, to December 31, 9999": "Date",
        "double-precision floating-point": "Double",
        "-32,768 to 32,767": "Integer",
        "-2,147,483,648 to 2,147,483,647": "Long",
        "-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807": "LongLong",
        "“This is an example”": "String",
        "Holds any particular type": "Variant"
    },
    "Part 3: General questions": {
        "Write an if statement along with the other parts of it. Use “statements” and “condition” when you write it out.": ["If condition Then", "statements", "ElseIf condition Then", "statements", "Else", "statements", "End If"],
        "Write a For loop. Use “counter”, “start”, “end”, “step”, and “statements” when you write it out.": ["For counter = start To end Step step", "statements", "Next"],
        "What statement breaks out of a for loop?": "Exit For",
        "Write a while loop. Use “condition” and “statements”.": ["While condition", "statements", "Wend"],
        "Write out the function statement format. Use “[a | b]” to indicate the user can choose either a or b. Also, use “func_name”, “varname”, “type”, “defaultvalue”, “statements”, “func_return_val”. Include two parameters, where the first one is required and the next one is not.": ["Function func_name([ByVal | ByRef] varname As type, Optional [ByVal | ByRef] varname As type = defaultvalue) As type", "statements", "func_name = func_return_val", "End Function"],
        "What statement exits a function?": "Exit Function",
        "Write out the subroutine statement format. Use “[a | b]” to indicate the user can choose either a or b. Also, use “sub_name”, “varname”, “type”, “defaultvalue”, “statements”. Include two parameters, where the first one is required and the next one is not.": ["Sub sub_name([ByVal | ByRef] varname As type, Optional [ByVal | ByRef] varname As type = defaultvalue)", "statements", "End Sub"],
        "What statement exits a subroutine?": "Exit Sub",
        "Given that a subroutine has been defined as “MyProc” and that it has a single parameter, write a statement that calls this procedure with an argument of 0.": "Call MyProc(0)",
        "What code converts a variable “var” to a date type?": "CDate(var)",
        "What code converts a variable “var” to a double type?": "CDbl(var)",
        "What code converts a variable “var” to an integer type?": "CInt(var)",
        "What code converts a variable “var” to a long type?": "CLng(var)",
        "What code converts a variable “var” to a string type?": "CStr(var)",
        "What is the symbol for a single line comment?": "'",
        "Write the code to declare variable “var” as a long data type.": "Dim var As Long",
        "Declare a dynamic array variable “var” whose upper bound is 10 and whose data type is double.": ["Dim var() as Double", "ReDim Preserve var(10)"]
    }
}

def add_line_breaks(string, every=80):
    return '\n'.join(wrap(string, every))

def check_answer(question, expected_answer):
    if isinstance(expected_answer, list):
        for i, ans in enumerate(expected_answer):
            user_ans = input(f"Answer line {i+1}: ")
            if user_ans.lower() in ["skip", "skip part"]:
                return user_ans.lower()
            while user_ans.lower() != ans.lower():
                print("There's an error in that line. Please try again.")
                user_ans = input(f"Answer line {i+1}: ")
                if user_ans.lower() in ["skip", "skip part"]:
                    return user_ans.lower()
    else:
        user_ans = input("Answer: ")
        if user_ans.lower() in ["skip", "skip part"]:
            return user_ans.lower()
        while user_ans.lower() != expected_answer.lower():
            print("That's not correct. Please try again.")
            user_ans = input("Answer: ")
            if user_ans.lower() in ["skip", "skip part"]:
                return user_ans.lower()
    return "correct"

for part, questions in quiz.items():
    print("\n" + part + "\n")
    question_items = list(questions.items())
    random.shuffle(question_items)
    for question, answer in question_items:
        print(add_line_breaks(question))
        user_choice = check_answer(question, answer)
        print()
        if user_choice == "skip part":
          break
    if user_choice == "skip part":
        continue
