def get_ED(name, emp_id, dep, salary):
    """Returns a formatted string containing employee details."""
    return(
        f"Employee Name:{name},\n"
        f"Employee ID:{emp_id},\n"
        f"Department:{dep},\n"
        f"Salary:{salary:.2f}"
    )
#Example usage (optional)
if __name__ == "__main__":
    print(get_ED("Sahana","Bca202","BCA",20000))