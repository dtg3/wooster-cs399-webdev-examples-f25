/*
    A simple JSON object stored in the variable colors

    The object consists of an array named colors with each
    element in the array being a dictionary with two elements
    name (the string that represents the color) and hex_value
    (a string represetnting the hexidecimal value of the color)
*/
const colors = [
    {"name":"Select a Color"},
    {"name":"red", "hex_value":"#db2929ff"},
    {"name":"green", "hex_value":"#48c248ff"},
    {"name":"blue", "hex_value":"#3958e0ff"},
    {"name":"black", "hex_value":"#3c3a3aff"}
];

// Get DOM elements that will be used with the JS
const color_select = document.getElementById("text_color");
const color_text = document.getElementById("color_text");
const messagebox = document.getElementById("txt_msg");
const msg_list = document.getElementById("messages");


function load() {
    console.log("Run with loaded page!");
    setup_color_list();
}

function setup_color_list() {
    // Loop over the indexes of the colors in the JSON array
    for (let index = 0; index < colors.length; ++index) {
        // Create an option element to be added to the select element
        let option = document.createElement("option");
        // Assign the text shown to the use as the option
        option.innerHTML = colors[index].name;
        if (colors[index].name == "Select a Color") {
            // Setup the default option so people know to select it
            option.selected = true;
            option.value = null;
            option.disabled = true;
        }
        else {
            // Add the value that actually represents that option
            option.value = colors[index].hex_value;
        }
        // Add the option element to the select element
        color_select.appendChild(option);
    }
}

// Function to trigger when the onchange event occurs for the
//  select element for changing the text color
function change_color(event) {
    // Determine the target of the event
    let selectElement = event.target;
    // Modify the elements color style
    color_text.style.color = selectElement.value;
}

function save_message() {
    if (messagebox.value == '') {
        alert("No message entered!")
        return
    }
    message = document.createElement("li");
    message.innerHTML = messagebox.value
    messagebox.value = "";
    msg_list.appendChild(message);
    messagebox.focus()
}