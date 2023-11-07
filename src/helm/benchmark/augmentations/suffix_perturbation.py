from dataclasses import dataclass
from random import Random
from typing import List

from .perturbation import TextPerturbation
from .perturbation_description import PerturbationDescription


class SuffixPerturbation(TextPerturbation):
    """
    Appends modifications to the end of the text. Example:

    A picture of a dog -> A picture of a dog, picasso, happy
    """

    @dataclass(frozen=True)
    class Description(PerturbationDescription):
        modifications: str = ""

    name: str = "style"

    def __init__(self, modifications: List[str]):
        self._modifications: List[str] = modifications

    @property
    def description(self) -> PerturbationDescription:
        return SuffixPerturbation.Description(name=self.name, modifications=",".join(self._modifications))

    def perturb(self, text: str, rng: Random) -> str:
        modifications: str = "" if len(self._modifications) == 0 else f", {', '.join(self._modifications)}"
        return text + modifications
