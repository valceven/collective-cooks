function selectCategory(button) {
    // Removing 'selected' class from all buttons
    const buttons = document.querySelectorAll('.btn-category');
    buttons.forEach(btn => {
        btn.classList.remove('bg-orange-600', 'text-white');
        btn.classList.add('bg-white', 'border-orange-600', 'text-orange-600');
    });
    
    // Adding 'selected' class to the clicked button
    button.classList.add('bg-orange-600', 'text-white');
    button.classList.remove('bg-white', 'border-orange-600', 'text-orange-600');

    // Set the hidden input value to the selected category
    document.getElementById('selected_category').value = button.innerText;
}

let stepCount = 1;
    
function addProcedureStep(button) {
    stepCount++;

    // Create a new ingredient row div
    const newProcedureDiv = document.createElement('div');
    newProcedureDiv.classList.add('procedure-step', 'flex','mb-2');
    
    // Create new step input
    const newStepInput = document.createElement('input');
    newStepInput.type = 'text';
    newStepInput.classList.add('border', 'border-gray-300', 'p-2', 'w-full', 'rounded');
    newStepInput.placeholder = `Step ${stepCount}...`;
    newStepInput.name = 'procedure';

    // Create new + button
    const newButton = document.createElement('button');
    newButton.type = 'button';
    newButton.classList.add('ml-2', 'bg-green-600', 'text-white', 'rounded-full', 'w-8', 'h-8', 'flex', 'items-center', 'justify-center');
    newButton.innerText = '+';
    newButton.setAttribute('onclick', 'addProcedureStep(this)');

    // Create new - button (only for subsequent rows)
    const removeButton = document.createElement('button');
    removeButton.type = 'button';
    removeButton.classList.add('ml-2', 'bg-red-600', 'text-white', 'rounded-full', 'w-8', 'h-8', 'flex', 'items-center', 'justify-center');
    removeButton.innerText = '-';
    removeButton.setAttribute('onclick', 'removeProcedureStep(this)');

    // Append new amount input and buttons to the amountDiv
    newProcedureDiv.appendChild(newStepInput);
    newProcedureDiv.appendChild(newButton);
    newProcedureDiv.appendChild(removeButton);

    // Insert the new row into the ingredients-container
    const ingredientsContainer = document.getElementById('procedure-container');
    ingredientsContainer.appendChild(newProcedureDiv);

    // Renumber all rows after adding a new one
    renumberProcedure();
}
function removeProcedureStep(button) {
    const procedureSteps = document.querySelectorAll('.procedure-step');

    // Ensure that at least one row remains (the first row can't be deleted)
    if (procedureSteps.length > 1) {
        const rowToRemove = button.closest('.procedure-step');
        rowToRemove.remove();

        // Renumber all rows after removing one
        renumberProcedure();

        // Make sure the + button is visible on the last row after removal
        const lastRow = document.querySelectorAll('.procedure-step')[document.querySelectorAll('.procedure-step').length - 1];
        const lastAddButton = lastRow.querySelector('button[onclick^="addProcedureStep"]');
        if (lastAddButton) {
            lastAddButton.style.display = 'inline-flex'; // Show the + button again
        }
    }
}

// Function to renumber the procedure after addition or removal
function renumberProcedure() {
    const procedureInputs = document.querySelectorAll('.procedure-step input[name="procedure"]');
    procedureInputs.forEach((input, index) => {
        input.placeholder = `Step ${index + 1}...`; // Renumber based on the index
    });
}

let ingredientCount = 1;

function addIngredientRow(button) {
    ingredientCount++; 

    // Create a new ingredient row div
    const newRowDiv = document.createElement('div');
    newRowDiv.classList.add('grid', 'grid-cols-1', 'md:grid-cols-2', 'gap-4', 'ingredient-row', 'mb-2');

    // Create new ingredient input
    const newIngredientInput = document.createElement('input');
    newIngredientInput.type = 'text';
    newIngredientInput.classList.add('border', 'border-gray-300', 'p-2', 'w-full', 'rounded');
    newIngredientInput.placeholder = `Ingredient ${ingredientCount}...`;
    newIngredientInput.name = 'ingredient';

    // Create new div for amount input and +, - button
    const amountDiv = document.createElement('div');
    amountDiv.classList.add('flex', 'items-center');

    // Create new amount input (smaller width)
    const newAmountInput = document.createElement('input');
    newAmountInput.type = 'text';
    newAmountInput.classList.add('border', 'border-gray-300', 'p-2', 'w-2/3', 'rounded');
    newAmountInput.placeholder = 'Amount';
    newAmountInput.name = 'amount';

    // Create new + button
    const newButton = document.createElement('button');
    newButton.type = 'button';
    newButton.classList.add('ml-2', 'bg-green-600', 'text-white', 'rounded-full', 'w-8', 'h-8', 'flex', 'items-center', 'justify-center');
    newButton.innerText = '+';
    newButton.setAttribute('onclick', 'addIngredientRow(this)');

    // Create new - button (only for subsequent rows)
    const removeButton = document.createElement('button');
    removeButton.type = 'button';
    removeButton.classList.add('ml-2', 'bg-red-600', 'text-white', 'rounded-full', 'w-8', 'h-8', 'flex', 'items-center', 'justify-center');
    removeButton.innerText = '-';
    removeButton.setAttribute('onclick', 'removeIngredientRow(this)');

    // Append new amount input and buttons to the amountDiv
    amountDiv.appendChild(newAmountInput);
    amountDiv.appendChild(newButton);
    amountDiv.appendChild(removeButton);

    // Append new ingredient input and amountDiv to the newRowDiv
    newRowDiv.appendChild(newIngredientInput);
    newRowDiv.appendChild(amountDiv);

    // Insert the new row into the ingredients-container
    const ingredientsContainer = document.getElementById('ingredients-container');
    ingredientsContainer.appendChild(newRowDiv);
    
    // Renumber all rows after adding a new one
    renumberIngredients();
}

function removeIngredientRow(button) {
    const ingredientRows = document.querySelectorAll('.ingredient-row');

    // Ensure that at least one row remains (the first row can't be deleted)
    if (ingredientRows.length > 1) {
        const rowToRemove = button.closest('.ingredient-row');
        rowToRemove.remove();

        // Renumber all rows after removing one
        renumberIngredients();

        // Make sure the + button is visible on the last row after removal
        const lastRow = document.querySelectorAll('.ingredient-row')[document.querySelectorAll('.ingredient-row').length - 1];
        const lastAddButton = lastRow.querySelector('button[onclick^="addIngredientRow"]');
        if (lastAddButton) {
            lastAddButton.style.display = 'inline-flex'; // Show the + button again
        }
    }
}

// Function to renumber the ingredients after addition or removal
function renumberIngredients() {
    const ingredientInputs = document.querySelectorAll('.ingredient-row input[name="ingredient"]');
    ingredientInputs.forEach((input, index) => {
        input.placeholder = `Ingredient ${index + 1}...`;
    });
}