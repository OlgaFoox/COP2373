import re

def validate_phone_number(phone):
    """Validate phone number ( formats: 123-456-7890, (123) 456-7890, 1234567890)."""
    pattern = re.compile(r'^(?:\(\d{3}\)\s?|\d{3}-)?\d{3}-\d{4}$')
    return bool(pattern.match(phone))

def validate_ssn(ssn):
    """Validate social security number (format: 123-45-6789)."""
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return bool(pattern.match(ssn))

def validate_zip_code(zip_code):
    """Validate zip code (5-digit or 5-4 digit format)."""
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return bool(pattern.match(zip_code))

def main():
    """Main function to get user input and validate it."""
    phone = input("Enter a phone number (e.g., 123-456-7890): ")
    ssn = input("Enter a social security number (e.g., 123-45-6789): ")
    zip_code = input("Enter a zip code (e.g., 12345 or 12345-6789): ")

    print("\nValidation Results:")
    
    if validate_phone_number(phone):
        print(f"Phone number '{phone}' is valid.")
    else:
        print(f"Phone number '{phone}' is invalid.")

    if validate_ssn(ssn):
        print(f"Social Security Number '{ssn}' is valid.")
    else:
        print(f"Social Security Number '{ssn}' is invalid.")

    if validate_zip_code(zip_code):
        print(f"Zip code '{zip_code}' is valid.")
    else:
        print(f"Zip code '{zip_code}' is invalid.")

if __name__ == "__main__":
    main()
