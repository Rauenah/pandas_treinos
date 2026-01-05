import luigi

class HelloLuigi(luigi.Task):
    def output(self):
        return luigi.LocalTarget("hello.txt")

    def run(self):
        with self.output().open("w") as f:
            f.write("Olá, Luigi rodando no VS Code!")