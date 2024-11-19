// Concatenate ingredients into the hidden input before submission
function concatenateIngredients() {
    const ingredientInputs = document.querySelectorAll('input[name="ingredient"]');
    const ingredientsArray = Array.from(ingredientInputs).map(input => input.value).filter(value => value); // Filter out empty values
    const concatenatedIngredients = ingredientsArray.join(', '); // Join with a comma
    document.getElementById('concatenated_ingredients').value = concatenatedIngredients; // Set the hidden input value
}

// Concatenate amounts into the hidden input before submission
function concatenateIngredientsCount() {
    const ingredientCountsInputs = document.querySelectorAll('input[name="amount"]');
    const ingredientCountsArray = Array.from(ingredientCountsInputs).map(input => input.value).filter(value => value);
    const concatenatedIngredientsCounts = ingredientCountsArray.join(', ');
    document.getElementById('concatenated_ingredients_counts').value = concatenatedIngredientsCounts;
    // document.getElementById('concatenated_ingredients_counts').value = "1, 1, 2";
}

// Concatenate procedures into the hidden input before submission
function concatenateProcedures() {
    const procedureInputs = document.querySelectorAll('input[name="procedure"]');
    const proceduresArray = Array.from(procedureInputs).map(input => input.value).filter(value => value);
    const concatenatedProcedures = proceduresArray.join(', '); // Join with a comma
    document.getElementById('concatenated_procedures').value = concatenatedProcedures; // Set the hidden input value
}

function onFormSubmit() {
    concatenateIngredients(); // Concatenate ingredients before submission
    concatenateIngredientsCount(); // Concatenate amounts before submission
    concatenateProcedures(); // Concatenate procedures before submission
    // updateHiddenProcedureField();

    return true;
}
