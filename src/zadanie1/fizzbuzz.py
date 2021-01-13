class MyFizzBuzz:
    def game(self, num):
        if type(num) != int and type(num) != float:
            return "Error in FizzBuzz"
        if num % 5 == 0 and num % 3 != 0 and num % 15 != 0:
            return "Buzz"
        elif num % 3 == 0 and num % 5 != 0 and num % 15 != 0:
            return "Fizz"
        elif num % 15 == 0:
            return "FizzBuzz"
        elif num % 5 != 0 and num % 15 != 0 and num % 3 != 0 and type(num) == int:
            return str(num)
        else:
            return num
