// Form controls for the Constraint API Example
// Event Listener that checks each time the control receives input
document.getElementById("constraint-email").addEventListener("input", contraint_email_validator);
document.getElementById("constraint-password").addEventListener("input", constraint_password_validator);

// Constraint API Validation
function contraint_email_validator(event) {
    let email_field = event.target;
    if (email_field.validity.typeMismatch) {
        email_field.setCustomValidity("This is not valid email address!");
    }
    else {
        email_field.setCustomValidity("");
    }
}

function constraint_password_validator(event) {
    let password_field = event.target;
    if (password_field.validity.valueMissing) {
        password_field.setCustomValidity("You must enter a password!");
    }
    else if (password_field.validity.tooShort) {
        password_field.setCustomValidity(`Password should be at least ${password_field.minLength} characters!`);
    }
    else {
        let result = valid_password_check(password_field.value);
        if (result == "special") {
            password_field.setCustomValidity("Password must have at least 1 special character!");
        }
        else if (result == "lower") {
            password_field.setCustomValidity("Password must have at least 1 lower case character!");
        }
        else if (result == "upper") {
            password_field.setCustomValidity("Password must have at least 1 upper case characcter!");
        }
        else if (result == "digit") {
            password_field.setCustomValidity("Password must have at least 1 digit!");
        }
        else {
            password_field.setCustomValidity("");
        }
    }
}

function valid_password_check(password_string) {
    const special_characters = `\`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~`;
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const digits = "0123456789";
    
    if (!check_contents(password_string, special_characters)) {
        return "special";
    }
    else if (!check_contents(password_string, characters.toLowerCase())) {
        return "lower";
    }
    else if (!check_contents(password_string, characters)) {
        return "upper";
    }
    else if (!check_contents(password_string, digits)) {
        return "digit";
    }   
    return "none";
}

function check_contents(input_string, compare_string) {
    return compare_string.split('').some(compare_string => {
        return (!input_string.includes(compare_string));
    });
}