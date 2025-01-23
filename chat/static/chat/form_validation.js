document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("signup-form");
    const username = document.getElementById("username");
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirm-password");
    const terms = document.getElementById("terms");
    const submitButton = form.querySelector("button[type='submit']");
    
    const usernameError = document.getElementById("username-error");
    const emailError = document.getElementById("email-error");
    const passwordError = document.getElementById("password-error");
    const confirmPasswordError = document.getElementById("confirm-password-error");
    
    // Utility function for validation
    function showError(input, errorElement, message) {
        input.classList.add("error");
        errorElement.textContent = message;
        errorElement.style.display = "block";
    }

    function clearError(input, errorElement) {
        input.classList.remove("error");
        errorElement.textContent = "";
        errorElement.style.display = "none";
    }

    // Username validation
    username.addEventListener("input", () => {
        const usernameValue = username.value.trim();
        if (!/^[a-zA-Z0-9]{3,}$/.test(usernameValue)) {
            showError(username, usernameError, "Username must be at least 3 alphanumeric characters.");
        } else {
            clearError(username, usernameError);
        }
    });

    // Email validation
    email.addEventListener("input", () => {
        const emailValue = email.value.trim();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(emailValue)) {
            showError(email, emailError, "Please enter a valid email address.");
        } else {
            clearError(email, emailError);
        }
    });

    // Password validation
    password.addEventListener("input", () => {
        const passwordValue = password.value.trim();
        const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;
        if (!passwordRegex.test(passwordValue)) {
            showError(
                password,
                passwordError,
                "Password must be at least 8 characters, include uppercase, lowercase, number, and special character."
            );
        } else {
            clearError(password, passwordError);
        }
    });

    // Confirm password validation
    confirmPassword.addEventListener("input", () => {
        if (confirmPassword.value.trim() !== password.value.trim()) {
            showError(confirmPassword, confirmPasswordError, "Passwords do not match.");
        } else {
            clearError(confirmPassword, confirmPasswordError);
        }
    });

    // Form submission validation
    form.addEventListener("submit", (event) => {
        let isValid = true;

        // Validate username
        if (usernameError.textContent || username.value.trim() === "") {
            showError(username, usernameError, "Username is required.");
            isValid = false;
        }

        // Validate email
        if (emailError.textContent || email.value.trim() === "") {
            showError(email, emailError, "Email is required.");
            isValid = false;
        }

        // Validate password
        if (passwordError.textContent || password.value.trim() === "") {
            showError(password, passwordError, "Password is required.");
            isValid = false;
        }

        // Validate confirm password
        if (confirmPasswordError.textContent || confirmPassword.value.trim() === "") {
            showError(confirmPassword, confirmPasswordError, "Confirm password is required.");
            isValid = false;
        }

        // Check terms
        if (!terms.checked) {
            alert("You must agree to the Terms of Service and Privacy Policy.");
            isValid = false;
        }

        // Prevent form submission if validation fails
        if (!isValid) {
            event.preventDefault();
        }
    });
});

// Toggle left menu visibility
function toggleMenu() {
    const leftMenu = document.getElementById('leftMenu');
    leftMenu.style.left = leftMenu.style.left === '0px' ? '-250px' : '0px';
}




