/* 
  These are from the react-icons package
    Install them using: npm install react-icons
    The imports come from: https://react-icons.github.io/react-icons/

    These tend to look nicer than emojis and have a variety
    of styles to match your UI.
*/
import { FaTrashCan,  FaBasketShopping} from "react-icons/fa6";
import { FaRegClock } from "react-icons/fa";

/*
  At last we arrive at our RecipeItem. Each item will recieve the
  prop associated with it's data object, and the onDeleteRecipe handler.
  We will call that function when the delete button is pressed to tell our
  App.jsx to get rid of that specific item.
*/
const RecipeItem = ({ recipe, onDeleteRecipe }) => {
  
  /*
    HOLD UP!

    We can't just go around deleting stuff without a confirmation, ESPECIALLY
    since we have no undo functionailty!

    Here we are making a function that is local to our recipe item, but will
    serve as a wrapper to the onDeleteRecipe function. This handleConfirmDelete
    function will first check with the user to see if they really really want to
    get rid of the item.
  */
  const handleConfirmDelete = () => {
    // This is triggers the native browser confirm() dialog
    const isConfirmed = confirm(`Are you sure you want to delete the recipe for "${recipe.name}"? This action cannot be undone.`);

    // If we said okay, we then call our original function to delete the recipe
    if (isConfirmed) {
      onDeleteRecipe(recipe.id);
    }
  };
  return (
    <div className="recipe-item">
      <h4>{recipe.name}</h4>
      <p>
        <span style={{ fontWeight: 'bold' }}>
          {/* 
            The icons we included are used like react components.
            We just add some inline style to place them in the
            desired location.

            This particular icon gos with the cook time and
            will show a clock.
          */}
          <FaRegClock style={{ marginRight: '5px' }} /> Time: 
        </span>{recipe.prepTime}</p>
      <p>
        <span style={{ fontWeight: 'bold' }}>
          {/* Shopping Cart/List icon */}
          <FaBasketShopping style={{ marginRight: '5px' }} /> Ingredients: 
        </span>{recipe.ingredients}</p>
      
      {/*
        Notice how we call our local handleConfirmDelete function which will
        call the actual delete if they agree to the confirmation. 
      */}
      <button 
        onClick={handleConfirmDelete}
        className="delete-button"
      >
        {/* Trash can for delete */}
        <FaTrashCan style={{ marginRight: '5px' }} />Delete
      </button>
    </div>
  );
};

export default RecipeItem;