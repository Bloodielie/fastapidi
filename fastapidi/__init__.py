__version__ = "0.1.2"

from typing import Any, overload, Type, TypeVar

from fastapi import FastAPI, params
from pyject import Container, IContainer
from starlette.requests import Request

T = TypeVar("T")


class FastAPIDI(FastAPI):
    container: IContainer = Container()


@overload
def get_dependency(annotation: Type[T]) -> T:
    ...


@overload
def get_dependency(annotation: Any) -> Any:
    ...


def get_dependency(annotation):
    async def depends_wrapper(request: Request):
        return request.app.container.get(annotation)
    return params.Depends(dependency=depends_wrapper, use_cache=True)


@overload
def get_all_dependencies(annotation: Type[T]) -> T:
    ...


@overload
def get_all_dependencies(annotation: Any) -> Any:
    ...


def get_all_dependencies(annotation):
    async def depends_wrapper(request: Request):
        return request.app.container.get_all(annotation)
    return params.Depends(dependency=depends_wrapper, use_cache=True)


def get_container() -> params.Depends:
    async def depends_wrapper(request: Request) -> IContainer:
        return request.app.container
    return params.Depends(dependency=depends_wrapper, use_cache=True)
