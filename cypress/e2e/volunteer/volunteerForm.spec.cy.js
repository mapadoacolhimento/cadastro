
describe('Form Fill and Submission', () => {

  it('Should fill and submit the form successfully', () => {
    cy.viewport(1800, 800, 'portrait');
    cy.visit('http://127.0.0.1:8000/')

    // cy.visit('https://novoqueroacolher.staging.bonde.org')

    cy.get('.gap-3 > .btn-secondary').click();

    // step 1
    cy.get('#id_first_name').type('Nomee');
    cy.get('#id_last_name').type('Sobrenome do Usuário');
    cy.get('#id_email').type('email@emailteste.com');
    cy.get('#id_zipcode').type('52010210'); //CEP válido
    cy.get('#id_state').select('BA');
    cy.get('#id_city').select('Paulo Afonso');
    cy.get('#id_neighborhood').should('exist')

    // Wait for the neighborhood field to exist after filling the ZIP code
    cy.wait(2000);

    cy.get('#continue-btn').click();

    // step 2
    cy.get('#id_color').select('Preta');
    cy.get('#id_gender').select('Mulher cisgênero');
    cy.get('#label_phone').type('1199998888');
    cy.get('#id_birth_date').type('18111996');
    cy.get('#id_document_number').type('65432155');

    cy.get('#continue-btn').click();

    // step 3
    cy.get('#id_availability').select('1');
    cy.get('#id_modality').select('Presencial');
    cy.get('#id_libras').select('Sim');

    cy.get('#continue-btn').click();

    // step 4
    cy.get('#id_years_of_experience_0').click();
    cy.get('#continue-btn').click();

    // step 5
    cy.get('#id_fields_of_work_1').click();
    cy.get('#continue-btn').click();

    // step 6
    cy.get('#id_approach_0').click();
    cy.get('#continue-btn').click();

    // step 7
    cy.get('#continue-btn').click();

    // terms
    cy.get('form > .text-neutral-50').click()

    // terms
    cy.get('form > .text-neutral-50').click()

    // terms
    cy.get('form > .text-neutral-50').click()

    // terms
    cy.get('form > .text-neutral-50').click()

    // Check redirection after accepting terms
    cy.url().should('eq', 'http://127.0.0.1:8000/psicologa/final/');

    // Click on the training button
    cy.get('form > .btn').click()

    // Check if still on the final screen after training
    cy.url().should('eq', 'http://127.0.0.1:8000/psicologa/final/');
  })
})
