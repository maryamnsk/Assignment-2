from Room_Invoice_Payment import Invoice

def test_invoice_generation():
    try:
        # Test: Generate invoice with user input
        print("Invoice Generation Test:")
        total_amount = float(input("Enter total amount: "))
        discounts = float(input("Enter discounts: "))
        invoice = Invoice(total_amount, discounts)
        print(f"Generated Invoice: {invoice}")

        # Test: Generate invoice with no discounts
        total_amount = float(input("Enter total amount: "))
        invoice_no_discount = Invoice(total_amount)
        print(f"Generated Invoice without Discounts: {invoice_no_discount}")

    except ValueError as e:
        print(f"ValueError in Invoice Generation Test Case: {e}")
    except Exception as e:
        print(f"Error in Invoice Generation Test Case: {e}")

if __name__ == "__main__":
    test_invoice_generation()
