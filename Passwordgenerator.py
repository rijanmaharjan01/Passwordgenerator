#include <stdio.h>
#include <stdlib.h>

int main()
{
    int choice, pin, amount, balance = 5000;
    int firstTime = 1;

    printf("Welcome to the Decision Bank ATM\n");
    printf("Please insert your card\n");
    if (firstTime)
{
        printf("Is this your first time using this ATM? (1 for yes, 0 for no)");
        scanf("%d", &firstTime);

        if (firstTime)
{
            printf("Please create a new PIN: ");
            scanf("%d", &pin);
            printf("Your PIN has been created successfully.\n");
            return 0;
        }
    }
     while (1)
        {
        printf("Please enter your PIN: ");
        scanf("%d", &pin);

        if (pin != 1234) {
            printf("Invalid PIN. Please try again.\n");
            continue;
        }

        printf("Welcome to your account\n");
        printf("Please select an option\n");
        printf("1. Check Balance\n");
        printf("2. Withdraw\n");
        printf("3. Exit\n");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                printf("Your current balance is: %d\n", balance);
                break;
            case 2:
                printf("Please enter the amount you would like to withdraw: ");
                scanf("%d", &amount);

                if (amount > balance)
                    {
                    printf("Insufficient funds.\n");
                }
                else
                {
                    balance -= amount;
                    printf("Please collect your cash.\n");
                    printf("Your current balance is: %d\n", balance);
                }
                break;
            case 3:
                printf("Thank you for using the ATM\n");
                return 0;
                break;
            default:
                printf("Invalid option. Please try again.\n");
                break;
        }
    }
    return 0;
}
