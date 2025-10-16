import { useState } from 'react';

// The App will use the List and Form components
import RecipeList from './components/RecipeList';
import RecipeForm from './components/RecipeForm';

/*
  Some starter data. This will not be persistent
  so if we refresh the page, the JavaScript will
  reload and restore this data back to it's original state.
*/
const initialRecipes = [
  { id: 1, name: "Spaghetti Carbonara", prepTime: "20 min", ingredients: "Pasta, Eggs, Cheese, Bacon" },
  { id: 2, name: "Simple Salad", prepTime: "10 min", ingredients: "Lettuce, Tomato, Vinaigrette" },
];

function App() {
  // State to hold our list of recipes
  const [recipes, setRecipes] = useState(initialRecipes);

  /* 
    We are setting up a function to be our event handler
      for when we click the Add Recipe button. This will get
      passed via props from the parent here down to the child
      component RecipeForm. This is called Prop Drilling. There
      are different ways to work around this, but for now, we'll
      simply pass along this handler so our other component will
      have functionality to update our recipe list.
  */
  const handleAddRecipe = (newRecipe) => {
    /*
      For presentation purposes, I'm adding the newest recipe to the
      top of the list. Since I process them in order, my function
      will update the state by taking the new recipe I've added and
      appending it to the old recipe list using the spread (...) syntax.
    */
    setRecipes((prevRecipes) => [newRecipe, ...prevRecipes]);

    // Console message for simple debugging in the example
    console.log("Recipe added!", newRecipe);
  };

  /*
    Same idea here for removing a recipe except we use the filter function
    to take all objects from our list that do not have the id of the recipe
    that we want to remove.
  */
  const handleDeleteRecipe = (recipeId) => {
    // Update the state will the filtered list
    setRecipes((prevRecipes) => 
      prevRecipes.filter((recipe) => recipe.id !== recipeId)
    );
    console.log(`Recipe ID ${recipeId} deleted.`);
  };

  return (
    <div className="container">
      <h1>Recipe Organizer</h1>

      {/* 
        When we add our RecipeForm component, we pass the handler 
        function down to the form using the onAddRecipe prop. The name
        is not special, but you do need to use the same name when you
        reference this prop in the child components.
      */}
      <RecipeForm onAddRecipe={handleAddRecipe} />

      <hr />

      <h2>Recipe List</h2>
      {/* 
        The list requires two props, one for the recipes and the other
        being the handler function to resolve clicking the delete button.
      */}
      <RecipeList recipes={recipes} onDeleteRecipe={handleDeleteRecipe} />
    </div>
  );
}

export default App;