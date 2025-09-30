// Form controls for the Custom API Example
// Controls
let custom_email_control = document.getElementById("custom-email");
let custom_password_control = document.getElementById("custom-password");
let custom_form_control = document.getElementById("custom-validation");
// Error Spans
const email_error = document.getElementById("email-error");
const password_error = document.getElementById("password-error");
// Event Listener that checks each time the control receives input
custom_email_control.addEventListener("input", custom_email_validator);
custom_password_control.addEventListener("input", custom_password_validator);
custom_form_control.addEventListener("submit", custom_form_validator);

// Custom Validator
function custom_email_validator(event) {
    if (custom_email_control.validity.valid) {
        email_error.textContent = "";
        email_error.className = "error";
    }
    else {
        show_email_error();
    }
}

function custom_password_validator(event) {
    clear_password_errors();
    let error_message = custom_valid_password_check(custom_password_control.value);
    if (custom_password_control.validity.valid && !error_message) {
        password_error.textContent = "";
        password_error.className = "error";
    }
    else {
        show_password_error(error_message);
    }
}

function custom_form_validator(event) {
    if (!custom_email_control.validity.valid) {
        show_email_error();
        event.preventDefault();
    }
    clear_password_errors();
    let error_message = custom_valid_password_check(custom_password_control.value);
    if (!custom_password_control.validity.valid || error_message) {
        show_password_error(error_message);
        event.preventDefault();
    }
}

function show_email_error() {
    if (custom_email_control.validity.valueMissing) {
        // If the field is empty,
        // display the following error message.
        email_error.textContent = "You need to enter an e-mail address";
    } else if (custom_email_control.validity.typeMismatch) {
        // If the field doesn't contain an email address,
        // display the following error message.
        email_error.textContent = "Entered value is not a valid e-mail address";
    }
    email_error.className = "error active";
}

function clear_password_errors() {
    while(password_error.firstChild) {
        password_error.removeChild(password_error.firstChild);
    }
}

function show_password_error(error_message) {
    password_error.appendChild(error_message);
    password_error.className = "error active";
}

function custom_valid_password_check(password_string) {
    const special_characters = `\`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~`;
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const digits = "0123456789";
    
    let error_message = null;
    let unordered_list = document.createElement('ul');

    if (custom_password_control.validity.valueMissing) {
        let list_element = document.createElement("li");
        list_element.textContent = "cannot be empty";
        unordered_list.appendChild(list_element);
    }
    if (password_string.length < custom_password_control.minLength) {
        let list_element = document.createElement("li");
        list_element.textContent = `must be at least ${custom_password_control.minLength} characters`;
        unordered_list.appendChild(list_element);
    }
    if (!check_contents(password_string, special_characters)) {
        let list_element = document.createElement("li");
        list_element.textContent = "needs at least one special character";
        unordered_list.appendChild(list_element);
    }
    if (!check_contents(password_string, characters.toLowerCase())) {
        let list_element = document.createElement("li");
        list_element.textContent = "needs at least one lowercase character";
        unordered_list.appendChild(list_element);
    }
    if (!check_contents(password_string, characters)) {
        let list_element = document.createElement("li");
        list_element.textContent = "needs at least one uppercase character";
        unordered_list.appendChild(list_element);
    }
    if (!check_contents(password_string, digits)) {
        let list_element = document.createElement("li");
        list_element.textContent = "needs at least one digit";
        unordered_list.appendChild(list_element);
    }
    
    if (unordered_list.getElementsByTagName("li").length > 0) {
        error_message = unordered_list;
    }

    return error_message;
}

function check_contents(input_string, compare_string) {
    return compare_string.split('').some(compare_string => {
        return (!input_string.includes(compare_string));
    });
}