describe("Lawyer form", () => {
  describe.only("Happy path", () => {
    before(() => {
      cy.viewport(1800, 800, "portrait");
    });
    beforeEach(() => {
      cy.visit("https://novoqueroacolher.bonde.org/logout?next=/");
      cy.wait(500);
      cy.findByRole("link", { name: /Sou advogada/i }).click();
    });

    it("should correctly fill out the whole form", () => {
      // dados pessoais
      cy.fillFirstStep("adv");
      cy.findByRole("button", { name: /Continuar/i }).click();

      // dados pessoais
      cy.fillLawyerSecondStep();
      cy.findByRole("button", { name: /Continuar/i }).click();

      // disponibilidade
      cy.fillThirdStep();
      cy.findByRole("button", { name: /Continuar/i }).click();

      // experiencia
      cy.fillFourthStep();
      cy.findByRole("button", { name: /Continuar/i }).click();

      // campo de atuação
      cy.fillLawyerFifthStep();
      cy.findByRole("button", { name: /Continuar/i }).click();

      // termos
      cy.acceptTerms();

      // capacitação
      cy.onlineCourse();
    });
  });

  describe("Unhappy paths", () => {});

  describe("Switch between lawyer and psychologist form", () => {
    before(() => {
      cy.viewport(1800, 800, "portrait");
    });
    beforeEach(() => {
      cy.visit("http://127.0.0.1:8000/logout?next=/");
      cy.wait(500);
    });

    it("should switch forms and fields according to the user selection", () => {
      cy.findByRole("button", { name: /Sou psicóloga/i }).click();
      cy.fillFirstStep("psi");
      cy.findByRole("button", { name: /continuar/i }).click();
      cy.findByLabelText(/crp/i).should("be.visible");

      cy.findByRole("button", { name: /voltar/i }).click();
      cy.findByRole("button", { name: /voltar/i }).click();

      // nao deveria aparecer a msg para trocar de forms antes de clicar no botao novamente?
      cy.findByRole("button", { name: /Sou advogada/i }).click();
      cy.wait(500);
      cy.findByRole("link", { name: /aqui/i }).click();
      cy.findByRole("button", { name: /Sou advogada/i }).click();

      cy.fillFirstStep("adv");
      cy.findByRole("button", { name: /continuar/i }).click();
      cy.findByLabelText(/oab/i).should("be.visible");
    });
  });
});
