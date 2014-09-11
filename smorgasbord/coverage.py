class Coverage(float):

    @property
    def percentage(self):
        return '{0:.0%}'.format(self)
