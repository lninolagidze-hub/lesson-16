# 1.
# შექმენით ბანკის სისტემა, რომელიც შეიცავს მომხმარებლებს და მათ ანგარიშებს. სისტემაში უნდა გამოიყენოთ:
#    კლასის ატრიბუტები:
#    	bank_name - ბანკის დასახელება
#    	total_accounts(private) - ანგარიშების რაოდენობა(ყოველი ანგარიშის გახსნის შემდეგ ავტომატურად უნდა გაიზარდოს)

# Class BankAccount:
#     bank_name="MyBank"
#     _Total_acount=0
#    ინსტანსის ატრიბუტები:
# 	owner (protected) — ანგარიშის მფლობელის სახელი
# 	balance (private) — ანგარიშზე არსებული თანხა
# 	account_number (private) — უნიკალური ანგარიში(ეს არ უნდა გადაეცეს ობიექტის შექმნის დროს, უნდა დაგენერირდეს
# 	ავტომატურად შემდეგი პრინციპით: პირველი ექაუნთის ნომერი იქნება AN0001, მეორესი AN0002 და ა.შ.

#    მეთოდები:
#    	__init__(self, owner, balance) — მნიშვნელობების მინიჭება

# 	deposit(self, amount) - ბალანსზე თანხის დამატება

# 	withdraw(self, amount) - ბალანსიდან თანხის გამოტანა

# 	check_balance(self) — აბრუნებს ბალანსს

# 	get_account_number(self) — აბრუნებს ანგარიშის ნომერს

# 	change_owner(self, new_owner) — ცვლის owner მნიშვნელობას

#    კლასის მეთოდი:
#    	get_total_accounts(): — აბრუნებს ანგარიშების რაოდენობას

#    სტატიკური მეთოდი:
#    	validate_amount(amount): — აბრუნებს True, თუ თანხა დადებითია
#    	ეს მეთოდი უნდა გამოიყენოთ __init__-ში ბალანსის შემოწმებისას და ისე გაუკეთოთ ბალანსს ინიციალიზაცია. ასევე, 	deposit და withdraw დროსაც ეს გამოიყენეთ რომ ვალიდაცია გაუკეთოთ amount-ს და ისე დაუმატოთ ან გამოიტანოთ თანხა

# ობიექტი დაბეჭდვისას გამოჩნდეს შემდეგი სახით, მაგალითად: "Account: AN0002 | Owner: Nino Beridze"




class BankAccount:
    bank_name = "MyBank"
    __total_accounts = 0

    def __init__(self, owner, balance):
        self._owner = owner

        if BankAccount.validate_amount(balance):
            self.__balance = balance
        else:
            self.__balance = 0

        BankAccount.__total_accounts += 1
        self.__account_number = f"AN{BankAccount.__total_accounts:04d}"

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.__balance += amount

    def withdraw(self, amount):
        if BankAccount.validate_amount(amount):

            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("არასაკმარისი თანხა")

    def check_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def change_owner(self, new_owner):
        self._owner = new_owner

    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts

    @staticmethod
    def validate_amount(amount):
        return amount > 0

# 2.
# შექმენით მეტაკლასი, რომელიც სხვა კლასზე გამოყენების შემთხვევაში შეამოწმებს ამ კლასის მეთოდის სახელებს,
#    შემდეგი სახით: თუ მეთოდი იწყება _ ეს მეთოდი ვალიდური იქნება, თუ არ იწყება _, მაშინ აღზევდეს
#    ValueError. მაგ: _test() - ეს მეთოდი იქნება ვალიდური, test() - ეს მეთოდი არ იქნება ვალიდური
#    და გამოიწვევს ValueError-ს. გაითვალისწინეთ რომ მეტაკლასმა უნდა შეამოწმოს მხოლოდ მეთოდები და არა ატრიბუტები!



class MethodValidator(type):

    def __new__(cls, name, bases, attrs):

        for attr_name, attr_value in attrs.items():
            if callable(attr_value):

                if not attr_name.startswith("_"):
                    raise ValueError(f"{attr_name} უნდა იწყებოდეს _ ით")

        return super().__new__(
            cls,
            name,
            bases,
            attrs
        )
