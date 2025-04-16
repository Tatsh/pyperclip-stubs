from collections.abc import Callable
from typing import Any, Literal

import typing_extensions

__all__ = ('copy', 'determine_clipboard', 'paste', 'set_clipboard')


class PyperclipException(RuntimeError):
    ...


class PyperclipWindowsException(PyperclipException):
    def __init__(self, message: str) -> None:
        ...


class PyperclipTimeoutException(PyperclipException):
    ...


class CheckedCall:
    def __init__(self, f: Any) -> None:  # _FuncPtr
        ...

    def __call__(self, *args: Any) -> Any:
        ...

    @typing_extensions.override
    def __setattr__(self, key: str, value: Any) -> None:
        ...


CopyCallable: typing_extensions.TypeAlias = Callable[[str], None]
PasteCallable: typing_extensions.TypeAlias = Callable[[], str]


def determine_clipboard() -> tuple[CopyCallable, PasteCallable]:
    ...


def set_clipboard(
    clipboard: Literal['klipper', 'no', 'pbcopy', 'pyobjc', 'qt', 'windows', 'wl-clipboard',
                       'xclip', 'xsel']
) -> None:
    ...


copy: CopyCallable = ...
paste: PasteCallable = ...
