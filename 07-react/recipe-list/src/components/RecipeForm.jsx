// src/RecipeForm.jsx
import { useState } from 'react';

/*
  When we create this component, we pass along
  the onAddRecipe prop with it's value. In this
  case, that prop holds the function we need to
  save our recipe.
*/
const RecipeForm = ({ onAddRecipe }) => {
  /*
    Here we will hold state for all the data our 
    form controls.
  */
  const [name, setName] = useState('');
  const [prepTime, setPrepTime] = useState('');
  const [ingredients, setIngredients] = useState('');

  /*
    This is the handler for the button click. Since
    our button is a "submit" type, when we click it
    the form will run it's onSubmit event, but the
    default action will be to refresh the page. Since
    we don't have any other page to go to and if we 
    refresh the page, we'll lose the data we just
    entered, we need to tell our function that
    handles that action to tell our event (e) to
    not perform that default behavior.
  */
  const handleSubmit = (e) => {
    e.preventDefault();

    // If the fields are empty, don't add a "blank" recipe
    if (!name || !prepTime) return;

    // Get the data from the state and create a new recipe object
    const newRecipe = {
      id: Date.now(),
      name,
      prepTime,
      ingredients,
    };

    /*
      Now we call the function in our prop to tell our parent to update
      the in memory recipe list.
    */
    onAddRecipe(newRecipe); 

    // Wipe the states for the recipe so we can start "clean"
    setName('');
    setPrepTime('');
    setIngredients('');
  };

  return (
    <form onSubmit={handleSubmit} className="recipe-form">
      <h3>Add New Recipe</h3>
      {/*
        This is a bit counter-intuitive, but notice the 
        onChange events associated with the text controls.
        Each time the value in the text fields changes, we
        call the state function to update the value we hold.
        
        In React, the value of the textboxes are controlled
        by react, notice how the value={name}. If we don't update
        the state for name to match the text in the box, the 
        text won't apear in the box and we won't get the data
        we need. To resolve this, we need to always keep the state
        up-to-date, thus the onChange updates.
      */}
      <input
        type="text"
        placeholder="Recipe Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="Prep Time (e.g., 30 min)"
        value={prepTime}
        onChange={(e) => setPrepTime(e.target.value)}
        required
      />
      <textarea
        placeholder="Ingredients (comma-separated)"
        value={ingredients}
        onChange={(e) => setIngredients(e.target.value)}
      />
      <button type="submit">Add Recipe</button>
    </form>
  );
};

export default RecipeForm;