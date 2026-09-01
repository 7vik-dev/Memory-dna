from typing import Callable, List, Optional

from memory_dna.test_case.test_case import RTTurn

CallbackType = Callable[[str, Optional[List[RTTurn]]], RTTurn]
