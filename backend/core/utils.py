from abc import ABCMeta


def abstract_class(cls):
    cls.__metaclass__ = ABCMeta

    def abstract_init(self, **kwargs) -> None:
        if self.__class__ is cls:
            raise Exception(f'{cls.__name__} cannot be instantiated')
        super(cls, self).__init__(**kwargs)

    cls.__init__ = abstract_init

    return cls
