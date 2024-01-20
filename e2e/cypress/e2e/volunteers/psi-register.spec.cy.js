describe("Psychologist form", () => {
  describe("Happy path", () => {
    before(() => {
      cy.viewport(1800, 800, "portrait");
    });
    beforeEach(() => {
      cy.visit("http://127.0.0.1:8000/logout?next=/");
      cy.wait(500);
      cy.findByRole("button", { name: /Sou psicóloga/i }).click();
    });

    it("should correctly fill out the whole form", () => {
      // dados pessoais
      cy.fillFirstStep("psi");
      cy.findByRole("button", { name: /Continuar/i }).click();

      // dados pessoais
      cy.fillPsychologistSecondStep();
      cy.findByRole("button", { name: /Continuar/i }).click();

      // disponibilidade
      cy.fillThirdStep();
      cy.findByRole("button", { name: /Continuar/i }).click();

      // experiencia
      cy.fillFourthStep();
      cy.findByRole("button", { name: /Continuar/i }).click();

      // campo de atuação
      cy.fillPsychologistFifthStep();
      cy.findByRole("button", { name: /Continuar/i }).click();

      // abordagem
      cy.fillPsychologistSixthStep();
      cy.findByRole("button", { name: /Continuar/i }).click();

      // termos
      cy.acceptTerms();

      // capacitação
      cy.onlineCourse();
    });
  });

  describe("Unhappy paths", () => {});
});
