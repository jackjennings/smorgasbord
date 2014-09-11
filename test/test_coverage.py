from smorgasbord.coverage import Coverage

class TestCoverage(object):

    def test_percentage_int(self):
        covered = Coverage(0)
        assert covered.percentage == '0%'

    def test_percentage_float(self):
        covered = Coverage(0.5)
        assert covered.percentage == '50%'
