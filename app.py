import re
import random
import string
import streamlit as st

def check_password_strength(password):
    """
    Analyze password strength and return score and feedback
    """
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    
    # Check for uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters")
    
    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one number")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*)")
    
    # Check for common patterns
    common_passwords = ['password123', '12345678', 'qwerty123']
    if password.lower() in common_passwords:
        score = 1
        feedback.append("This is a commonly used password. Please choose something more unique")
    
    return score, feedback

def generate_strong_password(length=12):
    """
    Generate a strong random password
    """
    characters = string.ascii_letters + string.digits + '!@#$%^&*'
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        score, _ = check_password_strength(password)
        if score >= 4:
            return password

def main():
    st.title("Password Strength Meter")
    st.write("Check your password strength or generate a secure password!")
    
    # Create two tabs
    tab1, tab2 = st.tabs(["Check Password", "Generate Password"])
    
    with tab1:
        password = st.text_input("Enter your password", type="password")
        if password:
            score, feedback = check_password_strength(password)
            
            # Display results
            if score <= 2:
                st.error("Password Strength: Weak")
            elif score == 3:
                st.warning("Password Strength: Moderate")
            else:
                st.success("Password Strength: Strong")
            
            # Show feedback if password is not strong
            if score < 4:
                st.write("Suggestions for improvement:")
                for suggestion in feedback:
                    st.write(f"- {suggestion}")
            else:
                st.success("Great! Your password meets all security criteria.")
    
    with tab2:
        length = st.slider("Password Length", min_value=8, max_value=32, value=12)
        if st.button("Generate Strong Password"):
            suggested_password = generate_strong_password(length)
            st.code(suggested_password)
            st.info("Copy this password and keep it secure!")

if __name__ == "__main__":
    main()
