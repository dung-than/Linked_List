
def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
        str1(string), str2(string): Strings to be checked
    Returns:
        bool: Indicates whether strings are anagrams
    """
    clean_str1 = str1.replace(" ", "").lower()
    clean_str2 = str2.replace(" ", "").lower()

    if len(clean_str1) == len(clean_str2):
        if sorted(clean_str1) == sorted(clean_str2):
            return True
    return False


print("Pass" if (anagram_checker('rat', 'art')) else "Fail")
print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")
