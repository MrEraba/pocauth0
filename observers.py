from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):

    @abstractmethod
    def update(self, subject: "Response") -> None:
        pass


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Response:
    def __init__(self):
        self.companies: List[str] = []


class HookSubject(Subject):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify(self) -> Response:
        response = Response()
        for observer in self._observers:
            observer.update(response)

        return response


class CompanyObserver(Observer):

    def __init__(self, company_name):
        self.name = company_name

    def update(self, response: Response) -> None:
        response.companies.append(self.name)


def company_subject_factory(*args: str) -> HookSubject:
    subject = HookSubject()
    for company in args:
        subject.attach(CompanyObserver(company))

    return subject
