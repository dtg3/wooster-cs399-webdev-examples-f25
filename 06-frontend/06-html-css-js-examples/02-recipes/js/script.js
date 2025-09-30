// Temporary storage for our recipes
let recipes = [
    {
        name: "Spaghetti Carbonara",
        imageURL: "https://images.unsplash.com/photo-1622973536968-3ead9e780960?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ingredients: ["Spaghetti", "Eggs", "Pecorino cheese", "Guanciale", "Black pepper"]
    },
    {
        name: "Classic Pancakes",
        imageURL: "https://plus.unsplash.com/premium_photo-1692193552660-233948b757a4?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        ingredients: ["Flour", "Milk", "Egg", "Baking powder", "Sugar", "Salt"]
    }
];


const recipeContainer = document.getElementById('recipe-container');
const recipeForm = document.getElementById('recipe-form');

// Function to render all recipes to the page
function renderRecipes() {
    recipeContainer.innerHTML = ''; // Clear existing cards
    recipes.forEach((recipe, index) => {
        const recipeCard = document.createElement('div');
        recipeCard.className = 'recipe-card';
        recipeCard.dataset.index = index;

        const ingredientsList = recipe.ingredients.map(ingredient => `<li>${ingredient}</li>`).join('');

        recipeCard.innerHTML = `
            <img src="${recipe.imageURL}" alt="${recipe.name}">
            <h3>${recipe.name}</h3>
            <ul>${ingredientsList}</ul>
            <button class="delete-btn">&times;</button>
        `;

        recipeContainer.appendChild(recipeCard);
    });
}

// Function to handle adding a new recipe
function addRecipe(e) {
    e.preventDefault(); // Prevent page reload

    const name = document.getElementById('recipe-name').value;
    const imageURL = document.getElementById('recipe-image').value;
    const ingredients = document.getElementById('recipe-ingredients').value.split(',').map(item => item.trim());

    const newRecipe = {
        name,
        imageURL,
        ingredients
    };

    recipes.push(newRecipe);
    renderRecipes(); // Re-render the cards to show the new one
    recipeForm.reset(); // Clear the form
}

// Function to handle deleting a recipe
function deleteRecipe(e) {
    if (e.target.classList.contains('delete-btn')) {
        const card = e.target.closest('.recipe-card');
        const index = card.dataset.index;
        recipes.splice(index, 1);
        renderRecipes(); // Re-render the cards
    }
}

// Event listeners
document.addEventListener('DOMContentLoaded', renderRecipes);
recipeForm.addEventListener('submit', addRecipe);
recipeContainer.addEventListener('click', deleteRecipe);