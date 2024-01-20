import "@testing-library/cypress/add-commands";

// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

Cypress.Commands.add("fillFirstStep", (volunteerType) => {
  cy.findByLabelText(/Primeiro nome/i)
    .type(`Voluntaria ${volunteerType}`)
    .should("have.value", `Voluntaria ${volunteerType}`);
  cy.findByLabelText(/Sobrenome/i)
    .type("Teste")
    .should("have.value", "Teste");
  cy.findByLabelText(/Seu melhor e-mail/i)
    .type("test@email.com")
    .should("have.value", "test@email.com");
  cy.findByLabelText(/CEP de atendimento/i)
    .type("01303020")
    .should("have.value", "01303-020");
  cy.wait(1500);
  cy.findByLabelText(/Estado/i).should("have.value", "SP");
  cy.findByLabelText(/Cidade/i).should("have.value", "SAO PAULO");
  cy.findByLabelText(/Bairro/i).should("have.value", "CONSOLAÇÃO");
});

Cypress.Commands.add("fillSecondStep", () => {
  cy.findByLabelText(/cor/i).select("Parda").should("have.value", "brown");
  cy.findByLabelText(/identidade de gênero/i)
    .select("Mulher cisgênero")
    .should("have.value", "cis_woman");
  cy.findByLabelText(/whatsapp para contato/i)
    .type("11911991199")
    .should("have.value", "(11) 9 1199-1199");
  cy.findByLabelText(/data de nascimento/i)
    .type("05091998")
    .should("have.value", "05/09/1998");
});

Cypress.Commands.add("fillPsychologistSecondStep", () => {
  cy.fillSecondStep();
  cy.findByLabelText(/crp/i).type("12312312").should("have.value", "12/312312");
});

Cypress.Commands.add("fillLawyerSecondStep", () => {
  cy.fillSecondStep();
  cy.findByLabelText(/oab/i).type("123123").should("have.value", "123123");
});

Cypress.Commands.add("fillThirdStep", () => {
  cy.findByLabelText(/vagas para atendimento/i)
    .select("2")
    .should("have.value", 2);
  cy.findByLabelText(/modalidade de atendimento/i)
    .select("Deixo à escolha da acolhida")
    .should("have.value", "both");
  cy.findByLabelText("Atende em linguagem de sinais (libras)").select("Sim");
});

Cypress.Commands.add("fillFourthStep", () => {
  cy.findByRole("radio", { name: /menos de 1 ano/i })
    .click()
    .should("have.value", "Menos de 1 ano");
});

Cypress.Commands.add("fillPsychologistFifthStep", () => {
  cy.findByRole("checkbox", { name: /saúde mental/i })
    .check()
    .should("be.checked")
    .and("have.value", "Saúde mental");
  cy.findByRole("checkbox", { name: /psicologia social/i })
    .check()
    .should("be.checked")
    .and("have.value", "Psicologia social");
});

Cypress.Commands.add("fillLawyerFifthStep", () => {
  cy.findByRole("checkbox", { name: /violência de gênero/i })
    .check()
    .should("be.checked")
    .and("have.value", "Violência de Gênero");
  cy.findByRole("checkbox", { name: /cível/i })
    .check()
    .should("be.checked")
    .and("have.value", "Cível");
});

Cypress.Commands.add("fillPsychologistSixthStep", () => {
  cy.findByRole("radio", { name: /humanismo/i })
    .click()
    .and("have.value", "Humanismo");
});

Cypress.Commands.add("acceptTerms", () => {
  cy.findByRole("heading", { name: /termo do voluntariado/i }).should(
    "be.visible"
  );
  cy.findByText(/Termo de Voluntariado e Diretrizes da organização/i).should(
    "be.visible"
  );
  cy.findByRole("button", { name: /continuar/i }).click();
  cy.findByRole("button", { name: "Aceito" }).click();
  cy.wait(1000);
  cy.findByRole("button", { name: "Aceito" }).click();
  cy.wait(1000);
  cy.findByRole("button", { name: "Aceito" }).click();
  cy.wait(1000);
  cy.findByRole("button", { name: "Aceito" }).click();
});

Cypress.Commands.add("onlineCourse", () => {
  cy.findByRole("heading", { name: /capacitação online/i }).should(
    "be.visible"
  );
  cy.findByRole("button", { name: /salvar/i }).click();
});
