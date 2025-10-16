import RecipeItem from './RecipeItem';

/*
  While the Recipe list obviously needs the list of all
  recipes, it might be unclear why we also needed a prop
  for the function to delete recipes (onDeleteRecipe). This
  is the idea of Prop Drilling in action. I need access to 
  the data the Parent holds to delete items so to get that
  functionaily from the parent so I can request it to delete
  a recipe, I need to pass that delete function to the parent
  components along the way. The next immediate parent is the
  RecipeList component. 
*/
const RecipeList = ({ recipes, onDeleteRecipe }) => {
  // Message if we have no recipes to display
  if (recipes.length === 0) {
    return <p>No recipes added yet! Use the form above.</p>;
  }
  
  return (
    <div className="recipe-list">
      {/*
        We will take each object in our recipe list and create a 
        RecipeItem component for it. The component will take the recipe
        itself as a prop and the function to tell our parent App.jsx to 
        remove the items when we click the delete button in the item.

        There is however one special prop named key. This is an internal
        prop used by react and NOT the RecipeItem component. This key must
        be unique for all the items in the list and is used for two purposes:
        
        * With a unique as the key, React can use this to update the Virtual DOM
          by re-rendering ONLY that item and not the entire list. This allows for
          a more efficient update to the UI.
        * We also need to consider state preservation. If we have a list or collection
          of things we want the IDs to be consistent and stable such that React always
          knows the specific element to which we are referring. This means we use this
          for data that can be added, removed, or reorded (which is why our other
          controls don't need it).
      */}
      {recipes.map((recipe) => (
        <RecipeItem 
          key={recipe.id} 
          recipe={recipe} 
          onDeleteRecipe={onDeleteRecipe} // Pass the handler down
        />
      ))}
    </div>
  );
};

export default RecipeList;