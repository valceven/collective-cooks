function selectCategory(button) {
    // Remove 'selected' class from all buttons
    const buttons = document.querySelectorAll('.btn-category');
    buttons.forEach(btn => {
        btn.classList.remove('bg-accent1', 'text-white');
        btn.classList.add('bg-white', 'border-accent1', 'text-accent1', 'dark:bg-slate-800');
    });
    
    // Add 'selected' class to the clicked button
    button.classList.add('bg-accent1', 'text-white');
    button.classList.remove('bg-white', 'border-accent1', 'text-accent1', 'dark:bg-slate-800');

    // Set the hidden input value to the selected category
    document.getElementById('selected_category').value = button.innerText;
}


let ingredientCount = document.querySelectorAll('.ingredient-row').length || 1;

function addIngredientRow(button) {
    ingredientCount++;

    // Create a new ingredient row div
    const newRowDiv = document.createElement('div');
    newRowDiv.classList.add('grid', 'grid-cols-1', 'md:grid-cols-2', 'gap-4', 'ingredient-row', 'mb-2');

    // Create new ingredient input
    const newIngredientInput = document.createElement('input');
    newIngredientInput.type = 'text';
    newIngredientInput.classList.add('bg-gray-200', 'border', 'border-gray-400', 'p-2', 'w-full', 'rounded', 'dark:bg-slate-400', 'dark:placeholder-white');
    newIngredientInput.placeholder = `Ingredient ${ingredientCount}...`;
    newIngredientInput.name = 'ingredient';

    // Create new div for amount input and buttons
    const amountDiv = document.createElement('div');
    amountDiv.classList.add('flex', 'items-center', 'space-x-2');

    // Create new amount input
    const newAmountInput = document.createElement('input');
    newAmountInput.type = 'text';
    newAmountInput.classList.add('bg-gray-200', 'border', 'border-gray-400', 'p-2', 'w-2/3', 'rounded', 'dark:bg-slate-400', 'dark:placeholder-white');
    newAmountInput.placeholder = 'Amount';
    newAmountInput.name = 'amount';

    // Create new + button
    const newAddButton = document.createElement('button');
    newAddButton.type = 'button';
    newAddButton.classList.add('ml-2', 'bg-confirm', 'text-white', 'rounded-full', 'w-8', 'h-8', 'flex', 'items-center', 'justify-center');
    newAddButton.innerText = '+';
    newAddButton.setAttribute('onclick', 'addIngredientRow(this)');

    // Create new - button
    const removeButton = document.createElement('button');
    removeButton.type = 'button';
    removeButton.classList.add('appearance-none', 'ml-2', 'bg-cancel', 'text-white', 'rounded-full', 'w-8', 'h-8', 'flex', 'items-center', 'justify-center');
    removeButton.innerText = '-';
    removeButton.setAttribute('onclick', 'removeIngredientRow(this)');

    // Append new amount input and buttons to the amountDiv
    amountDiv.appendChild(newAmountInput);
    amountDiv.appendChild(newAddButton);
    amountDiv.appendChild(removeButton);

    // Append new ingredient input and amountDiv to the newRowDiv
    newRowDiv.appendChild(newIngredientInput);
    newRowDiv.appendChild(amountDiv);

    // Insert the new row into the ingredients-container
    const ingredientsContainer = document.getElementById('ingredients-container');
    ingredientsContainer.appendChild(newRowDiv);

    // Update button visibility for all rows
    updateButtonVisibility();

    // Renumber all rows after adding
    renumberIngredients();
}

function removeIngredientRow(button) {
    const ingredientRows = document.querySelectorAll('.ingredient-row');

    // Ensure that at least one row remains
    if (ingredientRows.length > 1) {
        const rowToRemove = button.closest('.ingredient-row');
        rowToRemove.remove();

        // Update button visibility for all rows
        updateButtonVisibility();

        // Renumber all rows after removal
        renumberIngredients();
    }
}

function renumberIngredients() {
    const ingredientInputs = document.querySelectorAll('.ingredient-row input[name="ingredient"]');
    ingredientInputs.forEach((input, index) => {
        input.placeholder = `Ingredient ${index + 1}...`;
    });
}

function updateButtonVisibility() {
    const rows = document.querySelectorAll('.ingredient-row');

    rows.forEach((row, index) => {
        const addButton = row.querySelector('button[onclick^="addIngredientRow"]');
        const removeButton = row.querySelector('button[onclick^="removeIngredientRow"]');

        // Ensure the first row has no - button
        if (removeButton) {
            removeButton.style.display = index === 0 ? 'none' : 'inline-flex';
        }

        // Ensure only the last row has a visible + button
        if (addButton) {
            addButton.style.display = index === rows.length - 1 ? 'inline-flex' : 'none';
        }
    });
}

// Initialize the button visibility on page load
document.addEventListener('DOMContentLoaded', updateButtonVisibility);




function addProcedureStep(button) {
    stepCount++;

    // Create a new procedure step div
    const newProcedureDiv = document.createElement('div');
    newProcedureDiv.classList.add('procedure-step', 'flex', 'mb-2', 'space-x-2'); // Added space-x-2 for spacing between buttons
    
    // Create new step input
    const newStepInput = document.createElement('input');
    newStepInput.type = 'text';
    newStepInput.classList.add('bg-gray-200', 'border', 'border-gray-400', 'p-2', 'w-5/6', 'rounded', 'dark:bg-slate-400', 'dark:placeholder-white');
    newStepInput.placeholder = `Step ${stepCount}...`;
    newStepInput.name = 'procedure';

    // Create new + button
    const newButton = document.createElement('button');
    newButton.type = 'button';
    newButton.classList.add('ml-2', 'bg-confirm', 'text-white', 'rounded-full', 'w-8', 'h-8', 'flex', 'items-center', 'justify-center');
    newButton.innerText = '+';
    newButton.setAttribute('onclick', 'addProcedureStep(this)');

    // Create new - button (only for subsequent rows)
    const removeButton = document.createElement('button');
    removeButton.type = 'button';
    removeButton.classList.add('appearance-none', 'ml-2', 'bg-cancel', 'text-white', 'rounded-full', 'w-8', 'h-8', 'flex', 'items-center', 'justify-center');
    removeButton.innerText = '-';
    removeButton.setAttribute('onclick', 'removeProcedureStep(this)');

    // Append new step input and buttons to the newProcedureDiv
    newProcedureDiv.appendChild(newStepInput);
    newProcedureDiv.appendChild(newButton);
    newProcedureDiv.appendChild(removeButton);

    // Insert the new procedure step into the procedure-container
    const procedureContainer = document.getElementById('procedure-container');
    procedureContainer.appendChild(newProcedureDiv);

    // Renumber all procedure steps after adding a new one
    renumberProcedure();
}

function removeProcedureStep(button) {
    const procedureSteps = document.querySelectorAll('.procedure-step');

    // Ensure that at least one row remains (the first row can't be deleted)
    if (procedureSteps.length > 1) {
        const rowToRemove = button.closest('.procedure-step');
        rowToRemove.remove();

        // Renumber all steps after removing one
        renumberProcedure();

        // Make sure the + button is visible on the last row after removal
        const lastRow = document.querySelectorAll('.procedure-step')[document.querySelectorAll('.procedure-step').length - 1];
        const lastAddButton = lastRow.querySelector('button[onclick^="addProcedureStep"]');
        if (lastAddButton) {
            lastAddButton.style.display = 'inline-flex'; // Show the + button again
        }
    }
}

// Function to renumber the procedure steps after addition or removal
function renumberProcedure() {
    const procedureInputs = document.querySelectorAll('.procedure-step input[name="procedure"]');
    procedureInputs.forEach((input, index) => {
        input.placeholder = `Step ${index + 1}...`; // Renumber based on the index
    });
}


// Call initialization functions when the page loads
document.addEventListener('DOMContentLoaded', function() {
    initIngredients("{{ recipe.ingredients|default:'' }}");
    initProcedures("{{ recipe.procedures|default:'' }}");
});
