import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase): # класс TournamentTest, наследованный от TestCase
    @classmethod # декоратор
    def setUpClass(cls): # метод, где создаётся атрибут класса all_results
        cls.all_results = [] #словарь в который будут сохраняться результаты всех тестов

    def setUp(self): # метод, где создаются 3 объекта
        self.runner1 = rt.Runner(name='Усейн', speed=10)
        self.runner2 = rt.Runner(name='Андрей', speed=9)
        self.runner3 = rt.Runner(name='Ник', speed=3)

    @classmethod # декоратор
    def tearDownClass(cls): # метод, где выводятся all_results по очереди в столбец
        for i, elem in enumerate(cls.all_results):
            print(elem)

    def test_tournament1(self): # методы тестирования забега между Усейн и Ник
        t1 = rt.Tournament(90, self.runner1, self.runner3)
        t1_result = {k: str(v) for k, v in t1.start().items()}
        TournamentTest.all_results.append(t1_result) # запись результатов в словарь all_results
        self.assertTrue(t1_result[2], 'Ник') # сравнивается последний объект из all_results и предполагаемое имя последнего бегуна (Ник)

    def test_tournament2(self): # методы тестирования забега между Андрей и Ник
        t2 = rt.Tournament(90, self.runner2, self.runner3)
        t2_result = {k: str(v) for k, v in t2.start().items()}
        TournamentTest.all_results.append(t2_result) # запись результатов в словарь all_results
        self.assertTrue(t2_result[2], 'Ник') # сравнивается последний объект из all_results и предполагаемое имя последнего бегуна (Ник)

    def test_tournament3(self):
        t3 = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        t3_result = {k: str(v) for k, v in t3.start().items()}
        TournamentTest.all_results.append(t3_result) # запись результатов в словарь all_results
        self.assertTrue(t3_result[3], 'Ник') # сравнивается последний объект из all_results и предполагаемое имя последнего бегуна (Ник)


if __name__ == '__main__':
    unittest.main()
