describe("Fills out volunteer form", () => {
  before(() => {
    cy.viewport(1800, 800, "portrait");
    cy.visit("http://127.0.0.1:8000");
  });

  it("should correctly fill out first step of the form", () => {
    // should find 'psicologa' btn and click
    cy.findByRole("button", { name: /Sou psicóloga/i }).click();
    // should fill out volunteer name
    cy.findByLabelText(/Primeiro nome/i).type("Nome do Usuário");
    // should fill out volunteer last name
    cy.findByLabelText(/Sobrenome/i).type("Sobrenome do Usuário");
    // should fill out volunteer email
    cy.findByLabelText(/Seu melhor e-mail/i).type("gloria@gloria.com");
    // should fill out volunteer zipcode
    cy.findByLabelText(/CEP de atendimento/i).type("01303020");
    // should fill out volunteer state
    cy.findByLabelText(/Estado/i).should("have.value", "SP");
    // should fill out volunteer city
    cy.findByLabelText(/Cidade/i).should("have.value", "SAO PAULO");
    // should fill out volunteer neighborhood and click continue
    cy.findByLabelText(/Bairro/i).should("have.value", "CONSOLAÇÃO");
    cy.findByRole("button", { name: /Continuar/i }).click();
  });

  // it("passes", () => {
  // step 2
  // cy.get("#id_color").select("Preta");
  // cy.get("#id_gender").select("Mulher cisgênero");
  // cy.get("#label_phone").type("1199998888");
  // cy.get("#id_birth_date").type("18111996");
  // cy.get("#id_document_number").type("65432155");
  // cy.findByRole('button', {name: /Continuar/i}).click()
  // // step 3
  // cy.get("#id_availability").select("1");
  // cy.get("#id_modality").select("Presencial");
  // cy.get("#id_libras").select("Sim");
  // cy.findByRole('button', {name: /Continuar/i}).click()
  // // step 4
  // cy.get("#id_years_of_experience_0").click();
  // cy.findByRole('button', {name: /Continuar/i}).click()
  // // step 5
  // cy.get("#id_fields_of_work_1").click();
  // cy.findByRole('button', {name: /Continuar/i}).click()
  // // step 6
  // cy.get("#id_approach_0").click();
  // cy.findByRole('button', {name: /Continuar/i}).click()
  // // step 7
  // cy.findByRole('button', {name: /Continuar/i}).click()
  // // terms
  // cy.get("form > .text-neutral-50").click();
  // // terms
  // cy.get("form > .text-neutral-50").click();
  // // terms
  // cy.get("form > .text-neutral-50").click();
  // // terms
  // cy.get("form > .text-neutral-50").click();
  // // training
  // cy.get("form > .btn").click();
  // });
});
