class LoginPage:
    URL = "https://local-eats-unisenac.vercel.app/static/login.html"

    def __init__(self, page):
        self.page = page
        # a página tem dois formulários então uso o ID pra não pegar o campo errado
        self.email = page.locator("#loginEmail")
        self.senha = page.locator("#loginPassword")
        self.botao_entrar = page.locator("#loginForm button[type='submit']")

    def acessar(self):
        self.page.goto(self.URL)

    def realizar_login(self, email, senha):
        self.email.fill(email)
        self.senha.fill(senha)
        self.botao_entrar.click()

    def clicar_entrar(self):
        self.botao_entrar.click()

    def mensagem_visivel(self, texto):
        return self.page.get_by_text(texto).is_visible()
